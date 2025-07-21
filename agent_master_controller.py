import logging
import threading
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
from models import Agent, Task, AgentPool, SystemMetrics
from app import db
from ai_providers_enhanced import AIProviderManager
from task_processor import TaskProcessor

class AgentMasterController:
    """
    Core orchestration engine for OperatorOS
    Manages agent pools, task distribution, and system health
    """
    
    def __init__(self):
        self.ai_provider_manager = AIProviderManager()
        self.task_processor = TaskProcessor()
        self.is_running = False
        self.monitoring_thread = None
        self.agent_pools = {}
        self.initialized = False
        
    def _initialize_pools(self):
        """Initialize default agent pools"""
        if self.initialized:
            return
            
        try:
            default_pools = [
                {'name': 'healthcare', 'type': 'healthcare', 'target': 3, 'min': 1, 'max': 10},
                {'name': 'financial', 'type': 'financial', 'target': 3, 'min': 1, 'max': 8},
                {'name': 'sports', 'type': 'sports', 'target': 2, 'min': 1, 'max': 6},
                {'name': 'business', 'type': 'business', 'target': 4, 'min': 1, 'max': 12},
                {'name': 'general', 'type': 'general', 'target': 5, 'min': 2, 'max': 15}
            ]
            
            for pool_config in default_pools:
                existing_pool = AgentPool.query.filter_by(pool_name=pool_config['name']).first()
                if not existing_pool:
                    pool = AgentPool(
                        pool_name=pool_config['name'],
                        pool_type=pool_config['type'],
                        target_agents=pool_config['target'],
                        min_agents=pool_config['min'],
                        max_agents=pool_config['max'],
                        auto_scale=True,
                        health_status='healthy'
                    )
                    db.session.add(pool)
            
            db.session.commit()
            self.initialized = True
            logging.info("✅ Agent pools initialized successfully")
            
        except Exception as e:
            logging.error(f"❌ Failed to initialize pools: {e}")
            db.session.rollback()

    def start(self):
        """Start the agent master controller"""
        if not self.is_running:
            self.is_running = True
            self.monitoring_thread = threading.Thread(target=self._monitoring_loop)
            self.monitoring_thread.daemon = True
            self.monitoring_thread.start()
            logging.info("🚀 Agent Master Controller started")

    def stop(self):
        """Stop the agent master controller"""
        self.is_running = False
        if self.monitoring_thread:
            self.monitoring_thread.join()
        logging.info("⏹️ Agent Master Controller stopped")

    def _monitoring_loop(self):
        """Main monitoring and management loop"""
        while self.is_running:
            try:
                self._update_pool_status()
                self._auto_scale_pools()
                self._collect_metrics()
                time.sleep(30)  # Check every 30 seconds
            except Exception as e:
                logging.error(f"Error in monitoring loop: {e}")

    def _update_pool_status(self):
        """Update the status of all agent pools"""
        try:
            pools = AgentPool.query.all()
            for pool in pools:
                active_agents = Agent.query.filter_by(
                    agent_type=pool.pool_type, 
                    status='active'
                ).count()
                
                total_agents = Agent.query.filter_by(
                    agent_type=pool.pool_type
                ).count()
                
                pool.active_agents = active_agents
                pool.current_agents = total_agents
                pool.updated_at = datetime.utcnow()
                
            db.session.commit()
        except Exception as e:
            logging.error(f"Error updating pool status: {e}")
            db.session.rollback()

    def _auto_scale_pools(self):
        """Automatically scale agent pools based on demand"""
        try:
            pools = AgentPool.query.filter_by(auto_scale=True).all()
            
            for pool in pools:
                # Get pending tasks for this pool type
                pending_tasks = Task.query.filter_by(
                    task_type=pool.pool_type,
                    status='pending'
                ).count()
                
                # Simple scaling logic
                if pending_tasks > pool.current_agents * 2 and pool.current_agents < pool.max_agents:
                    self._scale_pool_up(pool, 1)
                elif pending_tasks == 0 and pool.current_agents > pool.min_agents:
                    # Scale down if no pending tasks and above minimum
                    idle_agents = Agent.query.filter_by(
                        agent_type=pool.pool_type,
                        status='idle'
                    ).count()
                    if idle_agents > 1:
                        self._scale_pool_down(pool, 1)
                        
        except Exception as e:
            logging.error(f"Error in auto-scaling: {e}")

    def _scale_pool_up(self, pool: AgentPool, count: int):
        """Scale up an agent pool"""
        try:
            for _ in range(count):
                if pool.current_agents < pool.max_agents:
                    agent = Agent(
                        name=f"{pool.pool_type}_agent_{pool.current_agents + 1}",
                        agent_type=pool.pool_type,
                        status='idle',
                        provider='openai',
                        model='gpt-4o'
                    )
                    db.session.add(agent)
                    pool.current_agents += 1
                    
            db.session.commit()
            logging.info(f"📈 Scaled up {pool.pool_name} pool by {count} agents")
            
        except Exception as e:
            logging.error(f"Error scaling up pool {pool.pool_name}: {e}")
            db.session.rollback()

    def _scale_pool_down(self, pool: AgentPool, count: int):
        """Scale down an agent pool"""
        try:
            idle_agents = Agent.query.filter_by(
                agent_type=pool.pool_type,
                status='idle'
            ).limit(count).all()
            
            for agent in idle_agents:
                db.session.delete(agent)
                pool.current_agents -= 1
                
            db.session.commit()
            logging.info(f"📉 Scaled down {pool.pool_name} pool by {len(idle_agents)} agents")
            
        except Exception as e:
            logging.error(f"Error scaling down pool {pool.pool_name}: {e}")
            db.session.rollback()

    def _collect_metrics(self):
        """Collect system performance metrics"""
        try:
            # Collect various metrics
            total_agents = Agent.query.count()
            active_agents = Agent.query.filter_by(status='active').count()
            pending_tasks = Task.query.filter_by(status='pending').count()
            completed_tasks_today = Task.query.filter(
                Task.created_at >= datetime.utcnow().date()
            ).filter_by(status='completed').count()
            
            # Calculate success rate
            total_tasks_today = Task.query.filter(
                Task.created_at >= datetime.utcnow().date()
            ).count()
            success_rate = (completed_tasks_today / total_tasks_today * 100) if total_tasks_today > 0 else 100
            
            # Store metrics
            metrics = [
                SystemMetrics(metric_name='total_agents', metric_value=total_agents, metric_unit='count'),
                SystemMetrics(metric_name='active_agents', metric_value=active_agents, metric_unit='count'),
                SystemMetrics(metric_name='pending_tasks', metric_value=pending_tasks, metric_unit='count'),
                SystemMetrics(metric_name='completed_tasks_today', metric_value=completed_tasks_today, metric_unit='count'),
                SystemMetrics(metric_name='success_rate', metric_value=success_rate, metric_unit='percent'),
            ]
            
            for metric in metrics:
                db.session.add(metric)
                
            db.session.commit()
            
        except Exception as e:
            logging.error(f"Error collecting metrics: {e}")
            db.session.rollback()

    def get_system_status(self) -> Dict[str, Any]:
        """Get comprehensive system status for conversational display"""
        try:
            # Get pool status
            pools = AgentPool.query.all()
            pool_status = []
            
            for pool in pools:
                efficiency = 0
                if pool.current_agents > 0:
                    efficiency = (pool.active_agents / pool.current_agents) * 100
                    
                pool_status.append({
                    'name': pool.pool_name,
                    'current': pool.current_agents,
                    'active': pool.active_agents,
                    'idle': pool.current_agents - pool.active_agents,
                    'efficiency': round(efficiency, 1),
                    'health': pool.health_status
                })
            
            # Get task metrics
            total_tasks_today = Task.query.filter(
                Task.created_at >= datetime.utcnow().date()
            ).count()
            
            completed_tasks_today = Task.query.filter(
                Task.created_at >= datetime.utcnow().date(),
                Task.status == 'completed'
            ).count()
            
            failed_tasks_today = Task.query.filter(
                Task.created_at >= datetime.utcnow().date(),
                Task.status == 'failed'
            ).count()
            
            pending_tasks = Task.query.filter_by(status='pending').count()
            processing_tasks = Task.query.filter_by(status='processing').count()
            
            success_rate = (completed_tasks_today / total_tasks_today * 100) if total_tasks_today > 0 else 100
            
            # Calculate average response time (mock for now)
            avg_response_time = 2.3  # This would be calculated from actual task completion times
            
            return {
                'pools': pool_status,
                'tasks': {
                    'total_today': total_tasks_today,
                    'completed_today': completed_tasks_today,
                    'failed_today': failed_tasks_today,
                    'pending': pending_tasks,
                    'processing': processing_tasks,
                    'success_rate': round(success_rate, 1)
                },
                'performance': {
                    'avg_response_time': avg_response_time,
                    'uptime': 99.8  # This would be calculated from system start time
                }
            }
            
        except Exception as e:
            logging.error(f"Error getting system status: {e}")
            return {'error': str(e)}

    def process_task(self, task_id: int) -> Dict[str, Any]:
        """Process a task through the appropriate agent pool"""
        try:
            task = Task.query.get(task_id)
            if not task:
                return {'error': 'Task not found'}
            
            # Find available agent for task type
            agent = Agent.query.filter_by(
                agent_type=task.task_type,
                status='idle'
            ).first()
            
            if not agent:
                # Try to scale up the pool
                pool = AgentPool.query.filter_by(pool_type=task.task_type).first()
                if pool and pool.current_agents < pool.max_agents:
                    self._scale_pool_up(pool, 1)
                    agent = Agent.query.filter_by(
                        agent_type=task.task_type,
                        status='idle'
                    ).first()
            
            if agent:
                # Assign task to agent
                task.agent_id = agent.id
                task.status = 'processing'
                task.started_at = datetime.utcnow()
                agent.status = 'active'
                agent.last_used = datetime.utcnow()
                
                db.session.commit()
                
                # Process task using AI providers
                result = self.task_processor.process_task(task)
                
                return result
            else:
                task.status = 'pending'
                db.session.commit()
                return {'status': 'queued', 'message': 'Task queued - no available agents'}
                
        except Exception as e:
            logging.error(f"Error processing task {task_id}: {e}")
            return {'error': str(e)}

    def scale_pool(self, pool_name: str, direction: str, count: int = 1) -> Dict[str, Any]:
        """Manually scale an agent pool"""
        try:
            pool = AgentPool.query.filter_by(pool_name=pool_name).first()
            if not pool:
                return {'error': f'Pool {pool_name} not found'}
            
            if direction.lower() == 'up':
                if pool.current_agents + count <= pool.max_agents:
                    self._scale_pool_up(pool, count)
                    return {
                        'status': 'success',
                        'message': f'Scaled {pool_name} up by {count} agents',
                        'new_count': pool.current_agents
                    }
                else:
                    return {'error': f'Cannot scale above maximum of {pool.max_agents}'}
            elif direction.lower() == 'down':
                if pool.current_agents - count >= pool.min_agents:
                    self._scale_pool_down(pool, count)
                    return {
                        'status': 'success',
                        'message': f'Scaled {pool_name} down by {count} agents',
                        'new_count': pool.current_agents
                    }
                else:
                    return {'error': f'Cannot scale below minimum of {pool.min_agents}'}
            else:
                return {'error': 'Direction must be "up" or "down"'}
                
        except Exception as e:
            logging.error(f"Error scaling pool {pool_name}: {e}")
            return {'error': str(e)}

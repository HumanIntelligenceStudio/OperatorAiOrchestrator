import logging
import threading
import time
import queue
from datetime import datetime
from typing import Dict, Any, Optional
from models import Task, Agent
from app import db
from agent_pools import SpecializedAgentPools

class TaskProcessor:
    """
    Task queue processing system for OperatorOS
    Handles task distribution, processing, and progress tracking
    """
    
    def __init__(self):
        self.task_queue = queue.PriorityQueue()
        self.processing_threads = []
        self.is_running = False
        self.max_workers = 5
        
        # Initialize specialized agent pools
        self.agent_pools = SpecializedAgentPools()
        
        # Task status tracking
        self.active_tasks = {}
        self.task_lock = threading.Lock()
        
        logging.info("⚙️ Task Processor initialized")

    def start(self):
        """Start task processing threads"""
        if not self.is_running:
            self.is_running = True
            
            # Start worker threads
            for i in range(self.max_workers):
                worker = threading.Thread(target=self._worker_loop, args=(i,))
                worker.daemon = True
                worker.start()
                self.processing_threads.append(worker)
            
            logging.info(f"🚀 Task Processor started with {self.max_workers} workers")

    def stop(self):
        """Stop task processing"""
        self.is_running = False
        logging.info("⏹️ Task Processor stopped")

    def submit_task(self, task: Task) -> Dict[str, Any]:
        """Submit a task for processing"""
        try:
            # Add task to processing queue with priority
            priority = 10 - task.priority  # Lower number = higher priority for queue
            self.task_queue.put((priority, task.id, datetime.utcnow().timestamp()))
            
            logging.info(f"📋 Task {task.id} submitted to queue (priority: {task.priority})")
            
            return {
                'task_id': task.id,
                'status': 'queued',
                'message': 'Task submitted successfully',
                'queue_position': self.task_queue.qsize()
            }
            
        except Exception as e:
            logging.error(f"Error submitting task {task.id}: {e}")
            return {'error': str(e)}

    def process_task(self, task: Task) -> Dict[str, Any]:
        """Process a single task immediately (bypassing queue)"""
        try:
            return self._process_task_internal(task)
        except Exception as e:
            logging.error(f"Error processing task {task.id}: {e}")
            return {'error': str(e)}

    def _worker_loop(self, worker_id: int):
        """Main worker loop for processing tasks"""
        logging.info(f"👷 Worker {worker_id} started")
        
        while self.is_running:
            try:
                # Get task from queue (block for up to 1 second)
                try:
                    priority, task_id, timestamp = self.task_queue.get(timeout=1.0)
                except queue.Empty:
                    continue
                
                # Get task from database
                task = Task.query.get(task_id)
                if not task:
                    logging.error(f"Task {task_id} not found in database")
                    continue
                
                # Process the task
                logging.info(f"👷 Worker {worker_id} processing task {task_id}")
                result = self._process_task_internal(task)
                
                # Mark task as done in queue
                self.task_queue.task_done()
                
            except Exception as e:
                logging.error(f"Worker {worker_id} error: {e}")

    def _process_task_internal(self, task: Task) -> Dict[str, Any]:
        """Internal task processing logic"""
        try:
            # Update task status
            task.status = 'processing'
            task.started_at = datetime.utcnow()
            db.session.commit()
            
            # Track active task
            with self.task_lock:
                self.active_tasks[task.id] = {
                    'started_at': datetime.utcnow(),
                    'status': 'processing'
                }
            
            logging.info(f"🔄 Processing task {task.id}: {task.query[:100]}...")
            
            # Route task to appropriate agent pool
            result = self.agent_pools.route_query(
                query=task.query,
                user_id=task.user_id,
                preferred_pool=task.task_type if task.task_type != 'auto' else None
            )
            
            if result.get('error'):
                # Handle error
                task.status = 'failed'
                task.error_message = result.get('message', 'Unknown error')
                task.completed_at = datetime.utcnow()
            else:
                # Handle success
                task.status = 'completed'
                task.response = result['result']['response']
                task.completed_at = datetime.utcnow()
                task.metadata = {
                    'pool_used': result.get('pool_used'),
                    'ai_metadata': result['result'].get('ai_metadata', {})
                }
            
            # Update agent status if assigned
            if task.agent_id:
                agent = Agent.query.get(task.agent_id)
                if agent:
                    agent.status = 'idle'
                    agent.last_used = datetime.utcnow()
                    # Update performance metrics
                    if not agent.performance_metrics:
                        agent.performance_metrics = {}
                    agent.performance_metrics['last_task_success'] = task.status == 'completed'
                    agent.performance_metrics['total_tasks'] = agent.performance_metrics.get('total_tasks', 0) + 1
            
            db.session.commit()
            
            # Remove from active tasks
            with self.task_lock:
                if task.id in self.active_tasks:
                    del self.active_tasks[task.id]
            
            processing_time = (datetime.utcnow() - task.started_at).total_seconds()
            logging.info(f"✅ Task {task.id} completed in {processing_time:.1f}s")
            
            return {
                'task_id': task.id,
                'status': task.status,
                'response': task.response,
                'processing_time': processing_time,
                'pool_used': result.get('pool_used')
            }
            
        except Exception as e:
            # Handle processing error
            task.status = 'failed'
            task.error_message = str(e)
            task.completed_at = datetime.utcnow()
            
            if task.agent_id:
                agent = Agent.query.get(task.agent_id)
                if agent:
                    agent.status = 'idle'
            
            db.session.commit()
            
            # Remove from active tasks
            with self.task_lock:
                if task.id in self.active_tasks:
                    del self.active_tasks[task.id]
            
            logging.error(f"❌ Task {task.id} failed: {e}")
            raise e

    def get_queue_status(self) -> Dict[str, Any]:
        """Get current queue status"""
        with self.task_lock:
            active_tasks_info = []
            for task_id, info in self.active_tasks.items():
                processing_time = (datetime.utcnow() - info['started_at']).total_seconds()
                active_tasks_info.append({
                    'task_id': task_id,
                    'processing_time': round(processing_time, 1),
                    'status': info['status']
                })
        
        return {
            'queue_size': self.task_queue.qsize(),
            'active_tasks': len(self.active_tasks),
            'active_tasks_details': active_tasks_info,
            'workers_running': len(self.processing_threads),
            'is_processing': self.is_running
        }

    def get_task_progress(self, task_id: int) -> Dict[str, Any]:
        """Get progress information for a specific task"""
        try:
            task = Task.query.get(task_id)
            if not task:
                return {'error': 'Task not found'}
            
            progress_info = {
                'task_id': task_id,
                'status': task.status,
                'created_at': task.created_at.isoformat(),
                'query': task.query,
                'task_type': task.task_type
            }
            
            if task.started_at:
                progress_info['started_at'] = task.started_at.isoformat()
                processing_time = (datetime.utcnow() - task.started_at).total_seconds()
                progress_info['processing_time'] = round(processing_time, 1)
            
            if task.completed_at:
                progress_info['completed_at'] = task.completed_at.isoformat()
                total_time = (task.completed_at - task.created_at).total_seconds()
                progress_info['total_time'] = round(total_time, 1)
            
            if task.response:
                progress_info['response'] = task.response
            
            if task.error_message:
                progress_info['error_message'] = task.error_message
            
            # Add active processing info if currently processing
            with self.task_lock:
                if task_id in self.active_tasks:
                    progress_info['currently_processing'] = True
                    progress_info['processing_stage'] = 'AI analysis in progress...'
            
            return progress_info
            
        except Exception as e:
            logging.error(f"Error getting task progress for {task_id}: {e}")
            return {'error': str(e)}

    def format_task_progress_for_display(self, task_id: int) -> str:
        """Format task progress for conversational display"""
        try:
            progress = self.get_task_progress(task_id)
            
            if progress.get('error'):
                return f"❌ Error getting task progress: {progress['error']}"
            
            status_icons = {
                'pending': '⏳',
                'processing': '🔄',
                'completed': '✅',
                'failed': '❌'
            }
            
            icon = status_icons.get(progress['status'], '❓')
            
            formatted = f"{icon} **Task #{task_id} Progress**\n"
            formatted += "=" * 40 + "\n\n"
            formatted += f"**Status**: {progress['status'].upper()}\n"
            formatted += f"**Query**: {progress['query'][:100]}{'...' if len(progress['query']) > 100 else ''}\n"
            formatted += f"**Type**: {progress['task_type']}\n"
            
            if progress.get('processing_time'):
                formatted += f"**Processing Time**: {progress['processing_time']}s\n"
            
            if progress.get('total_time'):
                formatted += f"**Total Time**: {progress['total_time']}s\n"
            
            if progress.get('currently_processing'):
                formatted += f"\n🔄 **Current Stage**: {progress.get('processing_stage', 'Processing...')}\n"
                
                # Add progress bar animation
                dots = "." * (int(time.time()) % 4)
                formatted += f"**Progress**: Analyzing{dots}\n"
            
            if progress.get('response'):
                formatted += f"\n**Response**:\n{progress['response'][:200]}{'...' if len(progress['response']) > 200 else ''}\n"
            
            if progress.get('error_message'):
                formatted += f"\n❌ **Error**: {progress['error_message']}\n"
            
            formatted += f"\n⏰ **Last Updated**: {datetime.now().strftime('%H:%M:%S')}"
            
            return formatted
            
        except Exception as e:
            logging.error(f"Error formatting task progress: {e}")
            return f"❌ Error formatting progress: {str(e)}"

    def cancel_task(self, task_id: int) -> Dict[str, Any]:
        """Cancel a pending or processing task"""
        try:
            task = Task.query.get(task_id)
            if not task:
                return {'error': 'Task not found'}
            
            if task.status in ['completed', 'failed']:
                return {'error': 'Task already finished'}
            
            # Update task status
            task.status = 'cancelled'
            task.completed_at = datetime.utcnow()
            task.error_message = 'Task cancelled by user'
            
            # Free up assigned agent
            if task.agent_id:
                agent = Agent.query.get(task.agent_id)
                if agent:
                    agent.status = 'idle'
            
            db.session.commit()
            
            # Remove from active tasks
            with self.task_lock:
                if task_id in self.active_tasks:
                    del self.active_tasks[task_id]
            
            logging.info(f"🚫 Task {task_id} cancelled")
            
            return {
                'task_id': task_id,
                'status': 'cancelled',
                'message': 'Task cancelled successfully'
            }
            
        except Exception as e:
            logging.error(f"Error cancelling task {task_id}: {e}")
            return {'error': str(e)}

    def get_performance_metrics(self) -> Dict[str, Any]:
        """Get task processor performance metrics"""
        try:
            # Get task statistics
            from sqlalchemy import func, and_
            from datetime import timedelta
            
            # Today's metrics
            today = datetime.utcnow().date()
            
            tasks_today = Task.query.filter(
                func.date(Task.created_at) == today
            ).count()
            
            completed_today = Task.query.filter(
                and_(
                    func.date(Task.created_at) == today,
                    Task.status == 'completed'
                )
            ).count()
            
            failed_today = Task.query.filter(
                and_(
                    func.date(Task.created_at) == today,
                    Task.status == 'failed'
                )
            ).count()
            
            # Average processing time for completed tasks today
            completed_tasks = Task.query.filter(
                and_(
                    func.date(Task.created_at) == today,
                    Task.status == 'completed',
                    Task.started_at.isnot(None),
                    Task.completed_at.isnot(None)
                )
            ).all()
            
            if completed_tasks:
                total_time = sum([
                    (task.completed_at - task.started_at).total_seconds()
                    for task in completed_tasks
                ])
                avg_processing_time = total_time / len(completed_tasks)
            else:
                avg_processing_time = 0
            
            success_rate = (completed_today / tasks_today * 100) if tasks_today > 0 else 100
            
            return {
                'tasks_today': tasks_today,
                'completed_today': completed_today,
                'failed_today': failed_today,
                'success_rate': round(success_rate, 1),
                'avg_processing_time': round(avg_processing_time, 2),
                'queue_size': self.task_queue.qsize(),
                'active_tasks': len(self.active_tasks),
                'workers_active': self.max_workers if self.is_running else 0
            }
            
        except Exception as e:
            logging.error(f"Error getting performance metrics: {e}")
            return {'error': str(e)}

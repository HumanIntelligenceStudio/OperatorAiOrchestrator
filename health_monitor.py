import logging
import psutil
import threading
import time
from datetime import datetime, timedelta
from typing import Dict, Any, List
from models import SystemMetrics, Agent, Task, AgentPool
from app import db

class HealthMonitor:
    """
    System health monitoring for OperatorOS
    Tracks system performance, agent health, and provides alerts
    """
    
    def __init__(self):
        self.is_monitoring = False
        self.monitoring_thread = None
        self.health_data = {}
        self.alert_thresholds = {
            'cpu_usage': 80,
            'memory_usage': 85,
            'disk_usage': 90,
            'agent_failure_rate': 10,  # percentage
            'response_time_warning': 5.0,  # seconds
            'queue_size_warning': 50
        }
        
        logging.info("🏥 Health Monitor initialized")

    def start_monitoring(self):
        """Start continuous health monitoring"""
        if not self.is_monitoring:
            self.is_monitoring = True
            self.monitoring_thread = threading.Thread(target=self._monitoring_loop)
            self.monitoring_thread.daemon = True
            self.monitoring_thread.start()
            logging.info("🔍 Health monitoring started")

    def stop_monitoring(self):
        """Stop health monitoring"""
        self.is_monitoring = False
        if self.monitoring_thread:
            self.monitoring_thread.join()
        logging.info("⏹️ Health monitoring stopped")

    def _monitoring_loop(self):
        """Main health monitoring loop"""
        while self.is_monitoring:
            try:
                self._collect_system_metrics()
                self._check_agent_health()
                self._check_database_health()
                self._evaluate_alerts()
                time.sleep(60)  # Check every minute
            except Exception as e:
                logging.error(f"Health monitoring error: {e}")

    def _collect_system_metrics(self):
        """Collect system performance metrics"""
        try:
            # CPU and Memory metrics
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            # Store metrics
            metrics = [
                SystemMetrics(
                    metric_name='cpu_usage_percent',
                    metric_value=cpu_percent,
                    metric_unit='percent'
                ),
                SystemMetrics(
                    metric_name='memory_usage_percent',
                    metric_value=memory.percent,
                    metric_unit='percent'
                ),
                SystemMetrics(
                    metric_name='disk_usage_percent',
                    metric_value=disk.percent,
                    metric_unit='percent'
                ),
                SystemMetrics(
                    metric_name='memory_available_mb',
                    metric_value=memory.available / 1024 / 1024,
                    metric_unit='mb'
                )
            ]
            
            for metric in metrics:
                db.session.add(metric)
            
            db.session.commit()
            
            # Update health data cache
            self.health_data['system'] = {
                'cpu_usage': cpu_percent,
                'memory_usage': memory.percent,
                'memory_available_mb': memory.available / 1024 / 1024,
                'disk_usage': disk.percent,
                'timestamp': datetime.utcnow()
            }
            
        except Exception as e:
            logging.error(f"Error collecting system metrics: {e}")

    def _check_agent_health(self):
        """Check health of all agent pools and individual agents"""
        try:
            pools = AgentPool.query.all()
            pool_health = {}
            
            for pool in pools:
                # Count agents by status
                total_agents = Agent.query.filter_by(agent_type=pool.pool_type).count()
                active_agents = Agent.query.filter_by(
                    agent_type=pool.pool_type, 
                    status='active'
                ).count()
                failed_agents = Agent.query.filter_by(
                    agent_type=pool.pool_type, 
                    status='failed'
                ).count()
                
                # Calculate health metrics
                if total_agents > 0:
                    failure_rate = (failed_agents / total_agents) * 100
                    utilization = (active_agents / total_agents) * 100
                else:
                    failure_rate = 0
                    utilization = 0
                
                # Determine health status
                health_status = 'healthy'
                if failure_rate > self.alert_thresholds['agent_failure_rate']:
                    health_status = 'critical'
                elif total_agents < pool.min_agents:
                    health_status = 'warning'
                elif utilization > 90:
                    health_status = 'overloaded'
                
                pool_health[pool.pool_type] = {
                    'total_agents': total_agents,
                    'active_agents': active_agents,
                    'failed_agents': failed_agents,
                    'failure_rate': round(failure_rate, 2),
                    'utilization': round(utilization, 2),
                    'health_status': health_status,
                    'min_agents': pool.min_agents,
                    'max_agents': pool.max_agents
                }
                
                # Update pool health status in database
                pool.health_status = health_status
            
            db.session.commit()
            self.health_data['agents'] = pool_health
            
        except Exception as e:
            logging.error(f"Error checking agent health: {e}")

    def _check_database_health(self):
        """Check database connection and performance"""
        try:
            start_time = time.time()
            
            # Simple database query to test connectivity
            task_count = Task.query.count()
            
            query_time = time.time() - start_time
            
            # Check for recent tasks
            recent_tasks = Task.query.filter(
                Task.created_at >= datetime.utcnow() - timedelta(hours=1)
            ).count()
            
            # Calculate task processing stats
            pending_tasks = Task.query.filter_by(status='pending').count()
            processing_tasks = Task.query.filter_by(status='processing').count()
            
            db_health = {
                'connection_time': round(query_time * 1000, 2),  # milliseconds
                'total_tasks': task_count,
                'recent_tasks_1h': recent_tasks,
                'pending_tasks': pending_tasks,
                'processing_tasks': processing_tasks,
                'status': 'healthy' if query_time < 1.0 else 'slow',
                'timestamp': datetime.utcnow()
            }
            
            self.health_data['database'] = db_health
            
        except Exception as e:
            logging.error(f"Error checking database health: {e}")
            self.health_data['database'] = {
                'status': 'error',
                'error_message': str(e),
                'timestamp': datetime.utcnow()
            }

    def _evaluate_alerts(self):
        """Evaluate health data against thresholds and generate alerts"""
        try:
            alerts = []
            
            # System alerts
            if 'system' in self.health_data:
                system = self.health_data['system']
                
                if system['cpu_usage'] > self.alert_thresholds['cpu_usage']:
                    alerts.append({
                        'type': 'system',
                        'severity': 'warning',
                        'message': f"High CPU usage: {system['cpu_usage']:.1f}%",
                        'timestamp': datetime.utcnow()
                    })
                
                if system['memory_usage'] > self.alert_thresholds['memory_usage']:
                    alerts.append({
                        'type': 'system',
                        'severity': 'critical',
                        'message': f"High memory usage: {system['memory_usage']:.1f}%",
                        'timestamp': datetime.utcnow()
                    })
                
                if system['disk_usage'] > self.alert_thresholds['disk_usage']:
                    alerts.append({
                        'type': 'system',
                        'severity': 'critical',
                        'message': f"High disk usage: {system['disk_usage']:.1f}%",
                        'timestamp': datetime.utcnow()
                    })
            
            # Agent alerts
            if 'agents' in self.health_data:
                for pool_type, pool_data in self.health_data['agents'].items():
                    if pool_data['health_status'] == 'critical':
                        alerts.append({
                            'type': 'agent',
                            'severity': 'critical',
                            'message': f"{pool_type} pool critical: {pool_data['failure_rate']:.1f}% failure rate",
                            'timestamp': datetime.utcnow()
                        })
                    elif pool_data['health_status'] == 'warning':
                        alerts.append({
                            'type': 'agent',
                            'severity': 'warning',
                            'message': f"{pool_type} pool below minimum agents",
                            'timestamp': datetime.utcnow()
                        })
            
            # Database alerts
            if 'database' in self.health_data:
                db_data = self.health_data['database']
                if db_data['status'] == 'error':
                    alerts.append({
                        'type': 'database',
                        'severity': 'critical',
                        'message': f"Database error: {db_data.get('error_message', 'Unknown error')}",
                        'timestamp': datetime.utcnow()
                    })
                elif db_data['status'] == 'slow':
                    alerts.append({
                        'type': 'database',
                        'severity': 'warning',
                        'message': f"Slow database response: {db_data['connection_time']}ms",
                        'timestamp': datetime.utcnow()
                    })
            
            self.health_data['alerts'] = alerts
            
            if alerts:
                logging.warning(f"Health alerts generated: {len(alerts)} alerts")
            
        except Exception as e:
            logging.error(f"Error evaluating alerts: {e}")

    def get_health_report(self) -> Dict[str, Any]:
        """Get comprehensive health report"""
        try:
            # Ensure we have recent data
            if not self.health_data or not self.is_monitoring:
                self._collect_system_metrics()
                self._check_agent_health()
                self._check_database_health()
                self._evaluate_alerts()
            
            # Calculate overall health score
            overall_score = self._calculate_health_score()
            
            return {
                'overall_health': {
                    'status': self._get_overall_status(overall_score),
                    'score': overall_score,
                    'timestamp': datetime.utcnow().isoformat()
                },
                'system_metrics': self.health_data.get('system', {}),
                'agent_health': self.health_data.get('agents', {}),
                'database_health': self.health_data.get('database', {}),
                'active_alerts': self.health_data.get('alerts', []),
                'monitoring_active': self.is_monitoring
            }
            
        except Exception as e:
            logging.error(f"Error generating health report: {e}")
            return {
                'error': str(e),
                'timestamp': datetime.utcnow().isoformat()
            }

    def _calculate_health_score(self) -> float:
        """Calculate overall health score (0-100)"""
        try:
            score = 100.0
            
            # System health impact
            if 'system' in self.health_data:
                system = self.health_data['system']
                score -= max(0, (system['cpu_usage'] - 70) * 0.5)  # Penalize high CPU
                score -= max(0, (system['memory_usage'] - 80) * 0.7)  # Penalize high memory
                score -= max(0, (system['disk_usage'] - 85) * 0.3)  # Penalize high disk
            
            # Agent health impact
            if 'agents' in self.health_data:
                failed_pools = 0
                total_pools = len(self.health_data['agents'])
                
                for pool_data in self.health_data['agents'].values():
                    if pool_data['health_status'] == 'critical':
                        score -= 15
                        failed_pools += 1
                    elif pool_data['health_status'] == 'warning':
                        score -= 5
                    elif pool_data['health_status'] == 'overloaded':
                        score -= 3
                
                if total_pools > 0 and failed_pools / total_pools > 0.5:
                    score -= 20  # Additional penalty if majority of pools failing
            
            # Database health impact
            if 'database' in self.health_data:
                db_data = self.health_data['database']
                if db_data['status'] == 'error':
                    score -= 25
                elif db_data['status'] == 'slow':
                    score -= 10
            
            # Alert impact
            if 'alerts' in self.health_data:
                for alert in self.health_data['alerts']:
                    if alert['severity'] == 'critical':
                        score -= 5
                    elif alert['severity'] == 'warning':
                        score -= 2
            
            return max(0, min(100, score))
            
        except Exception as e:
            logging.error(f"Error calculating health score: {e}")
            return 50.0  # Default score on error

    def _get_overall_status(self, score: float) -> str:
        """Get overall status based on health score"""
        if score >= 90:
            return 'excellent'
        elif score >= 75:
            return 'healthy'
        elif score >= 60:
            return 'warning'
        elif score >= 40:
            return 'degraded'
        else:
            return 'critical'

    def format_health_report_for_display(self) -> str:
        """Format health report for conversational display"""
        try:
            report = self.get_health_report()
            
            if report.get('error'):
                return f"❌ Health report error: {report['error']}"
            
            overall = report['overall_health']
            
            # Status icons
            status_icons = {
                'excellent': '🟢',
                'healthy': '🟢',
                'warning': '🟡',
                'degraded': '🟠',
                'critical': '🔴'
            }
            
            icon = status_icons.get(overall['status'], '❓')
            
            formatted = f"{icon} **OPERATOROS HEALTH REPORT**\n"
            formatted += "=" * 50 + "\n\n"
            
            # Overall health
            formatted += f"**Overall Status**: {overall['status'].upper()} ({overall['score']:.1f}/100)\n\n"
            
            # System metrics
            if 'system_metrics' in report and report['system_metrics']:
                system = report['system_metrics']
                formatted += "🖥️ **System Performance**:\n"
                formatted += f"├── CPU Usage: {system['cpu_usage']:.1f}%\n"
                formatted += f"├── Memory Usage: {system['memory_usage']:.1f}%\n"
                formatted += f"├── Disk Usage: {system['disk_usage']:.1f}%\n"
                formatted += f"└── Available Memory: {system['memory_available_mb']:.0f} MB\n\n"
            
            # Agent health
            if 'agent_health' in report and report['agent_health']:
                formatted += "🤖 **Agent Pool Health**:\n"
                for pool_type, pool_data in report['agent_health'].items():
                    pool_icon = '🟢' if pool_data['health_status'] == 'healthy' else '🟡' if pool_data['health_status'] == 'warning' else '🔴'
                    formatted += f"├── {pool_icon} {pool_type.title()}: {pool_data['active_agents']}/{pool_data['total_agents']} active ({pool_data['utilization']:.1f}% util)\n"
                formatted += "\n"
            
            # Database health
            if 'database_health' in report and report['database_health']:
                db_data = report['database_health']
                db_icon = '🟢' if db_data['status'] == 'healthy' else '🟡' if db_data['status'] == 'slow' else '🔴'
                formatted += f"🗄️ **Database**: {db_icon} {db_data['status'].upper()}\n"
                formatted += f"├── Connection Time: {db_data.get('connection_time', 'N/A')}ms\n"
                formatted += f"├── Pending Tasks: {db_data.get('pending_tasks', 0)}\n"
                formatted += f"└── Processing Tasks: {db_data.get('processing_tasks', 0)}\n\n"
            
            # Active alerts
            if 'active_alerts' in report and report['active_alerts']:
                formatted += "🚨 **Active Alerts**:\n"
                for alert in report['active_alerts'][-5:]:  # Show last 5 alerts
                    alert_icon = '🔴' if alert['severity'] == 'critical' else '🟡'
                    formatted += f"├── {alert_icon} {alert['message']}\n"
                formatted += "\n"
            else:
                formatted += "✅ **No Active Alerts**\n\n"
            
            # Monitoring status
            monitoring_icon = '🟢' if report['monitoring_active'] else '🔴'
            formatted += f"{monitoring_icon} **Monitoring**: {'ACTIVE' if report['monitoring_active'] else 'INACTIVE'}\n"
            
            formatted += f"\n⏰ **Report Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            
            return formatted
            
        except Exception as e:
            logging.error(f"Error formatting health report: {e}")
            return f"❌ Error formatting health report: {str(e)}"

    def get_quick_status(self) -> str:
        """Get quick status summary for conversational display"""
        try:
            report = self.get_health_report()
            overall = report['overall_health']
            
            status_emojis = {
                'excellent': '🟢 Excellent',
                'healthy': '🟢 Healthy',
                'warning': '🟡 Warning',
                'degraded': '🟠 Degraded',
                'critical': '🔴 Critical'
            }
            
            status_text = status_emojis.get(overall['status'], '❓ Unknown')
            
            alert_count = len(report.get('active_alerts', []))
            alert_text = f" • {alert_count} alert{'s' if alert_count != 1 else ''}" if alert_count > 0 else ""
            
            return f"System Health: {status_text} ({overall['score']:.0f}/100){alert_text}"
            
        except Exception as e:
            return f"Health Status: ❌ Error ({str(e)})"

    def run_health_check(self) -> Dict[str, Any]:
        """Run immediate comprehensive health check"""
        try:
            logging.info("🔍 Running comprehensive health check...")
            
            # Force fresh data collection
            self._collect_system_metrics()
            self._check_agent_health()
            self._check_database_health()
            self._evaluate_alerts()
            
            report = self.get_health_report()
            
            logging.info(f"✅ Health check complete - Status: {report['overall_health']['status']}")
            
            return report
            
        except Exception as e:
            logging.error(f"Error running health check: {e}")
            return {'error': str(e)}

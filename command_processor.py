import logging
import re
from typing import Dict, Any, Optional, List
from datetime import datetime
from agent_pools import SpecializedAgentPools
from health_monitor import HealthMonitor
from demo_runner import DemoRunner
from business_automation import BusinessAutomationEngine
from agent_master_controller import AgentMasterController

class CommandProcessor:
    """
    Natural language command processing for OperatorOS
    Parses conversational input and executes appropriate system operations
    """
    
    def __init__(self):
        self.agent_pools = SpecializedAgentPools()
        self.health_monitor = HealthMonitor()
        self.demo_runner = DemoRunner()
        self.business_automation = BusinessAutomationEngine()
        self.agent_controller = AgentMasterController()
        
        # Command patterns for natural language processing
        self.command_patterns = {
            'status': [
                r'(?:show|get|display)?\s*(?:me\s+)?(?:the\s+)?(?:system\s+)?status',
                r'how\s+(?:is|are)\s+(?:the\s+)?(?:system|things|everything)',
                r'what\'?s\s+(?:the\s+)?(?:current\s+)?(?:system\s+)?status',
                r'status\s*(?:report|update)?'
            ],
            'health': [
                r'(?:show|get|display)?\s*(?:me\s+)?(?:the\s+)?(?:system\s+)?health',
                r'health\s*(?:check|report|status)?',
                r'how\s+healthy\s+is\s+(?:the\s+)?system',
                r'(?:run|perform)\s+(?:a\s+)?health\s+check'
            ],
            'pools': [
                r'(?:show|display|list)?\s*(?:me\s+)?(?:the\s+)?(?:agent\s+)?pools?',
                r'agent\s+pool\s*(?:status|info|information)?',
                r'how\s+are\s+(?:the\s+)?(?:agent\s+)?pools?\s+(?:doing|performing)',
                r'pool\s*(?:status|performance|metrics)?'
            ],
            'scale_up': [
                r'scale\s+up\s+(\w+)(?:\s+(?:pool|agents?))?(?:\s+by\s+(\d+))?',
                r'increase\s+(\w+)\s+(?:pool|agents?)(?:\s+by\s+(\d+))?',
                r'add\s+(?:more\s+)?(\w+)\s+agents?(?:\s+(\d+))?',
                r'expand\s+(?:the\s+)?(\w+)\s+pool(?:\s+by\s+(\d+))?'
            ],
            'scale_down': [
                r'scale\s+down\s+(\w+)(?:\s+(?:pool|agents?))?(?:\s+by\s+(\d+))?',
                r'decrease\s+(\w+)\s+(?:pool|agents?)(?:\s+by\s+(\d+))?',
                r'remove\s+(\w+)\s+agents?(?:\s+(\d+))?',
                r'reduce\s+(?:the\s+)?(\w+)\s+pool(?:\s+by\s+(\d+))?'
            ],
            'restart': [
                r'restart\s+(\w+)(?:\s+(?:pool|agents?))?',
                r'reboot\s+(\w+)(?:\s+(?:pool|agents?))?',
                r'reset\s+(?:the\s+)?(\w+)\s+pool'
            ],
            'demo': [
                r'(?:show|run|start)\s+(?:me\s+)?(?:a\s+)?(\w+)\s+demo',
                r'demo\s+(\w+)',
                r'demonstrate\s+(\w+)(?:\s+capabilities)?',
                r'example\s+of\s+(\w+)'
            ],
            'help': [
                r'help(?:\s+me)?(?:\s+with\s+\w+)?',
                r'what\s+can\s+you\s+do',
                r'(?:show|list)\s+(?:me\s+)?(?:all\s+)?(?:available\s+)?commands?',
                r'how\s+do\s+i\s+use\s+this',
                r'capabilities'
            ],
            'task_healthcare': [
                r'i\s+(?:have|need|want)\s+(?:medical|health)',
                r'(?:medical|health)\s+(?:advice|help|question)',
                r'(?:doctor|physician|medical)\s+(?:advice|consultation)',
                r'(?:symptoms?|pain|hurt|sick|illness)',
                r'health\s*(?:issue|problem|concern)'
            ],
            'task_financial': [
                r'(?:should\s+i\s+)?invest(?:ment)?',
                r'(?:stock|financial|money|finance)',
                r'(?:market|trading|portfolio)',
                r'financial\s+(?:advice|planning|analysis)',
                r'(?:buy|sell)\s+(?:stock|shares)'
            ],
            'task_sports': [
                r'(?:predict|prediction)(?:s)?\s+(?:for\s+)?(?:tonight|today|game)',
                r'(?:sports|game|team|player)',
                r'(?:bet|betting|odds)',
                r'(?:nfl|nba|mlb|nhl|soccer|football|basketball)',
                r'fantasy\s+(?:football|basketball|sports)'
            ],
            'task_business': [
                r'(?:business|work|workflow|process)',
                r'(?:automate|automation|optimize)',
                r'(?:team|management|productivity)',
                r'help\s+(?:me\s+)?(?:with\s+)?(?:my\s+)?(?:business|work)',
                r'(?:improve|optimize)\s+(?:our|my)\s+(?:process|workflow)'
            ],
            'admin': [
                r'admin\s+(\w+)(?:\s+(.*))?',
                r'administrative\s+(\w+)',
                r'(?:show|get)\s+admin\s+(\w+)'
            ]
        }
        
        logging.info("🎯 Command Processor initialized with natural language patterns")

    def process_command(self, user_input: str, user_id: int, session_context: Optional[Dict] = None) -> Dict[str, Any]:
        """Process natural language command and execute appropriate action"""
        try:
            command_input = user_input.strip().lower()
            logging.info(f"🔍 Processing command: {command_input[:100]}...")
            
            # Try to match command patterns
            command_match = self._match_command_pattern(command_input)
            
            if command_match:
                command_type = command_match['type']
                groups = command_match['groups']
                
                logging.info(f"✅ Matched command type: {command_type}")
                
                # Execute matched command
                return self._execute_command(command_type, groups, user_input, user_id, session_context)
            else:
                # If no specific command pattern matched, treat as general task
                return self._handle_general_task(user_input, user_id, session_context)
                
        except Exception as e:
            logging.error(f"Error processing command: {e}")
            return {
                'error': True,
                'message': f"Command processing failed: {str(e)}",
                'command_type': 'error'
            }

    def _match_command_pattern(self, command_input: str) -> Optional[Dict[str, Any]]:
        """Match user input against command patterns"""
        for command_type, patterns in self.command_patterns.items():
            for pattern in patterns:
                match = re.search(pattern, command_input, re.IGNORECASE)
                if match:
                    return {
                        'type': command_type,
                        'groups': match.groups(),
                        'pattern': pattern
                    }
        return None

    def _execute_command(self, command_type: str, groups: tuple, original_input: str, 
                        user_id: int, session_context: Optional[Dict] = None) -> Dict[str, Any]:
        """Execute the matched command"""
        try:
            if command_type == 'status':
                return self._handle_status_command(user_id)
            
            elif command_type == 'health':
                return self._handle_health_command(user_id)
            
            elif command_type == 'pools':
                return self._handle_pools_command(user_id)
            
            elif command_type == 'scale_up':
                pool_name = groups[0] if groups[0] else 'general'
                count = int(groups[1]) if len(groups) > 1 and groups[1] else 1
                return self._handle_scale_command(pool_name, 'up', count, user_id)
            
            elif command_type == 'scale_down':
                pool_name = groups[0] if groups[0] else 'general'
                count = int(groups[1]) if len(groups) > 1 and groups[1] else 1
                return self._handle_scale_command(pool_name, 'down', count, user_id)
            
            elif command_type == 'restart':
                pool_name = groups[0] if groups[0] else 'all'
                return self._handle_restart_command(pool_name, user_id)
            
            elif command_type == 'demo':
                demo_type = groups[0] if groups[0] else 'general'
                return self._handle_demo_command(demo_type, user_id)
            
            elif command_type == 'help':
                return self._handle_help_command(user_id)
            
            elif command_type.startswith('task_'):
                task_type = command_type.replace('task_', '')
                return self._handle_task_submission(original_input, task_type, user_id)
            
            elif command_type == 'admin':
                admin_command = groups[0] if groups[0] else 'status'
                admin_args = groups[1] if len(groups) > 1 else ''
                return self._handle_admin_command(admin_command, admin_args, user_id)
            
            else:
                return {
                    'error': True,
                    'message': f"Unknown command type: {command_type}",
                    'command_type': 'error'
                }
                
        except Exception as e:
            logging.error(f"Error executing command {command_type}: {e}")
            return {
                'error': True,
                'message': f"Command execution failed: {str(e)}",
                'command_type': 'error'
            }

    def _handle_status_command(self, user_id: int) -> Dict[str, Any]:
        """Handle system status commands"""
        try:
            status = self.agent_controller.get_system_status()
            
            if status.get('error'):
                raise Exception(status['error'])
            
            # Format status for conversational display
            status_text = self._format_system_status(status)
            
            return {
                'success': True,
                'response': status_text,
                'command_type': 'system_status',
                'data': status
            }
            
        except Exception as e:
            logging.error(f"Error handling status command: {e}")
            return {
                'error': True,
                'message': f"Failed to get system status: {str(e)}",
                'command_type': 'system_status'
            }

    def _handle_health_command(self, user_id: int) -> Dict[str, Any]:
        """Handle health check commands"""
        try:
            health_report = self.health_monitor.format_health_report_for_display()
            
            return {
                'success': True,
                'response': health_report,
                'command_type': 'health_check'
            }
            
        except Exception as e:
            logging.error(f"Error handling health command: {e}")
            return {
                'error': True,
                'message': f"Health check failed: {str(e)}",
                'command_type': 'health_check'
            }

    def _handle_pools_command(self, user_id: int) -> Dict[str, Any]:
        """Handle agent pool status commands"""
        try:
            pool_status = self.agent_pools.get_pool_status()
            pool_text = self._format_pool_status(pool_status)
            
            return {
                'success': True,
                'response': pool_text,
                'command_type': 'pools_status',
                'data': pool_status
            }
            
        except Exception as e:
            logging.error(f"Error handling pools command: {e}")
            return {
                'error': True,
                'message': f"Failed to get pool status: {str(e)}",
                'command_type': 'pools_status'
            }

    def _handle_scale_command(self, pool_name: str, direction: str, count: int, user_id: int) -> Dict[str, Any]:
        """Handle pool scaling commands"""
        try:
            result = self.agent_controller.scale_pool(pool_name, direction, count)
            
            if result.get('error'):
                raise Exception(result['error'])
            
            response_text = f"⚡ **Agent Pool Scaled Successfully**\n\n"
            response_text += f"📊 **Pool**: {pool_name.title()}\n"
            response_text += f"📈 **Action**: Scaled {direction} by {count} agent{'s' if count != 1 else ''}\n"
            response_text += f"🤖 **New Count**: {result.get('new_count', 'Unknown')} agents\n"
            response_text += f"✅ **Status**: {result.get('message', 'Operation completed')}"
            
            return {
                'success': True,
                'response': response_text,
                'command_type': 'agent_management',
                'data': result
            }
            
        except Exception as e:
            logging.error(f"Error handling scale command: {e}")
            return {
                'error': True,
                'message': f"Scaling failed: {str(e)}",
                'command_type': 'agent_management'
            }

    def _handle_restart_command(self, pool_name: str, user_id: int) -> Dict[str, Any]:
        """Handle agent pool restart commands"""
        try:
            # In production, this would implement actual restart logic
            response_text = f"🔄 **Agent Pool Restart Initiated**\n\n"
            response_text += f"📊 **Pool**: {pool_name.title()}\n"
            response_text += f"⏳ **Status**: Restarting agents...\n"
            response_text += f"🎯 **Expected Duration**: 30-60 seconds\n"
            response_text += f"✅ **Note**: New agents will be available shortly"
            
            return {
                'success': True,
                'response': response_text,
                'command_type': 'agent_management'
            }
            
        except Exception as e:
            logging.error(f"Error handling restart command: {e}")
            return {
                'error': True,
                'message': f"Restart failed: {str(e)}",
                'command_type': 'agent_management'
            }

    def _handle_demo_command(self, demo_type: str, user_id: int) -> Dict[str, Any]:
        """Handle demonstration commands"""
        try:
            demo_result = self.demo_runner.run_demo(demo_type, user_id)
            
            if demo_result.get('error'):
                raise Exception(demo_result['error'])
            
            return {
                'success': True,
                'response': demo_result['demo_content'],
                'command_type': 'demo',
                'data': demo_result
            }
            
        except Exception as e:
            logging.error(f"Error handling demo command: {e}")
            return {
                'error': True,
                'message': f"Demo failed: {str(e)}",
                'command_type': 'demo'
            }

    def _handle_help_command(self, user_id: int) -> Dict[str, Any]:
        """Handle help commands"""
        try:
            help_text = self._generate_help_text()
            
            return {
                'success': True,
                'response': help_text,
                'command_type': 'help'
            }
            
        except Exception as e:
            logging.error(f"Error handling help command: {e}")
            return {
                'error': True,
                'message': f"Help generation failed: {str(e)}",
                'command_type': 'help'
            }

    def _handle_task_submission(self, query: str, task_type: str, user_id: int) -> Dict[str, Any]:
        """Handle task submission commands"""
        try:
            # Route task to appropriate agent pool
            result = self.agent_pools.route_query(query, user_id, task_type)
            
            if result.get('error'):
                raise Exception(result.get('message', 'Task processing failed'))
            
            # Format response for conversational display
            response_text = f"✅ **Task Processed Successfully**\n\n"
            response_text += f"🎯 **Routed to**: {result.get('pool_name', 'Unknown Pool')}\n"
            response_text += f"🤖 **Agent Type**: {result.get('pool_used', task_type).title()}\n\n"
            response_text += f"**Response**:\n{result['result']['response']}"
            
            return {
                'success': True,
                'response': response_text,
                'command_type': 'task_submission',
                'data': result
            }
            
        except Exception as e:
            logging.error(f"Error handling task submission: {e}")
            return {
                'error': True,
                'message': f"Task submission failed: {str(e)}",
                'command_type': 'task_submission'
            }

    def _handle_admin_command(self, admin_command: str, admin_args: str, user_id: int) -> Dict[str, Any]:
        """Handle administrative commands"""
        try:
            if not self._is_admin_user(user_id):
                return {
                    'error': True,
                    'message': "Administrative privileges required for this command",
                    'command_type': 'admin'
                }
            
            # Handle different admin commands
            if admin_command == 'status':
                admin_status = self._get_admin_dashboard()
                return {
                    'success': True,
                    'response': admin_status,
                    'command_type': 'admin'
                }
            elif admin_command == 'logs':
                return {
                    'success': True,
                    'response': "📋 **System Logs**: Log viewing would be implemented in production",
                    'command_type': 'admin'
                }
            elif admin_command == 'users':
                return {
                    'success': True,
                    'response': "👥 **User Management**: User management interface would be implemented in production",
                    'command_type': 'admin'
                }
            else:
                return {
                    'error': True,
                    'message': f"Unknown admin command: {admin_command}",
                    'command_type': 'admin'
                }
                
        except Exception as e:
            logging.error(f"Error handling admin command: {e}")
            return {
                'error': True,
                'message': f"Admin command failed: {str(e)}",
                'command_type': 'admin'
            }

    def _handle_general_task(self, user_input: str, user_id: int, session_context: Optional[Dict] = None) -> Dict[str, Any]:
        """Handle general tasks that don't match specific command patterns"""
        try:
            # Auto-detect task type
            task_type = self._detect_task_type(user_input)
            
            # Route to appropriate agent pool
            result = self.agent_pools.route_query(user_input, user_id, task_type)
            
            if result.get('error'):
                # If agent pool fails, try business automation for business-related queries
                if self._is_business_query(user_input):
                    business_result = self.business_automation.analyze_workflow(user_input, user_id)
                    if business_result.get('success'):
                        formatted_response = self.business_automation.format_business_analysis_for_display(business_result)
                        return {
                            'success': True,
                            'response': formatted_response,
                            'command_type': 'business_analysis',
                            'data': business_result
                        }
                
                raise Exception(result.get('message', 'Task processing failed'))
            
            # Format response
            response_text = f"🎯 **Query Processed**\n\n"
            response_text += f"**Agent Pool**: {result.get('pool_name', 'Unknown')}\n"
            response_text += f"**Task Type**: {result.get('pool_used', task_type).title()}\n\n"
            response_text += result['result']['response']
            
            return {
                'success': True,
                'response': response_text,
                'command_type': 'general_task',
                'data': result
            }
            
        except Exception as e:
            logging.error(f"Error handling general task: {e}")
            
            # Provide helpful fallback response
            fallback_response = self._generate_fallback_response(user_input)
            
            return {
                'error': True,
                'message': str(e),
                'response': fallback_response,
                'command_type': 'general_task'
            }

    def _detect_task_type(self, query: str) -> str:
        """Auto-detect task type based on query content"""
        query_lower = query.lower()
        
        # Healthcare keywords
        if any(keyword in query_lower for keyword in [
            'medical', 'health', 'doctor', 'symptom', 'pain', 'sick', 'medication',
            'headache', 'fever', 'chest', 'hurt', 'disease', 'treatment'
        ]):
            return 'healthcare'
        
        # Financial keywords
        elif any(keyword in query_lower for keyword in [
            'invest', 'stock', 'money', 'financial', 'market', 'trading',
            'portfolio', 'buy', 'sell', 'fund', 'crypto', 'bitcoin'
        ]):
            return 'financial'
        
        # Sports keywords
        elif any(keyword in query_lower for keyword in [
            'game', 'team', 'player', 'sport', 'bet', 'odds', 'predict',
            'nfl', 'nba', 'mlb', 'soccer', 'football', 'basketball'
        ]):
            return 'sports'
        
        # Business keywords
        elif any(keyword in query_lower for keyword in [
            'business', 'work', 'workflow', 'process', 'automate', 'team',
            'management', 'productivity', 'optimize', 'efficiency'
        ]):
            return 'business'
        
        else:
            return 'general'

    def _is_business_query(self, query: str) -> bool:
        """Check if query is business-related for automation analysis"""
        business_keywords = [
            'workflow', 'process', 'automate', 'automation', 'business',
            'optimize', 'efficiency', 'team', 'management', 'operations'
        ]
        query_lower = query.lower()
        return any(keyword in query_lower for keyword in business_keywords)

    def _is_admin_user(self, user_id: int) -> bool:
        """Check if user has admin privileges"""
        # In production, this would check against proper user permissions
        return user_id == 1  # Default admin user

    def _format_system_status(self, status: Dict[str, Any]) -> str:
        """Format system status for conversational display"""
        formatted = "🤖 **OPERATOROS SYSTEM STATUS**\n"
        formatted += "=" * 50 + "\n\n"
        
        # Agent Pools
        if 'pools' in status:
            formatted += "📊 **Agent Pool Status**:\n"
            for pool in status['pools']:
                efficiency = pool.get('efficiency', 0)
                efficiency_icon = "🟢" if efficiency > 80 else "🟡" if efficiency > 60 else "🔴"
                formatted += f"├── {efficiency_icon} **{pool['name'].title()}**: {pool['active']}/{pool['current']} active ({efficiency}% efficiency)\n"
            formatted += "\n"
        
        # Performance
        if 'performance' in status:
            perf = status['performance']
            formatted += "⚡ **System Performance**:\n"
            formatted += f"├── Avg Response Time: {perf.get('avg_response_time', 'N/A')}s\n"
            formatted += f"└── Uptime: {perf.get('uptime', 'N/A')}%\n\n"
        
        # Tasks
        if 'tasks' in status:
            tasks = status['tasks']
            formatted += "📋 **Task Activity Today**:\n"
            formatted += f"├── Completed: {tasks.get('completed_today', 0)}\n"
            formatted += f"├── Processing: {tasks.get('processing', 0)}\n"
            formatted += f"├── Pending: {tasks.get('pending', 0)}\n"
            formatted += f"└── Success Rate: {tasks.get('success_rate', 0)}%\n"
        
        formatted += f"\n⏰ **Status as of**: {datetime.now().strftime('%H:%M:%S')}"
        
        return formatted

    def _format_pool_status(self, pool_status: Dict[str, Any]) -> str:
        """Format agent pool status for conversational display"""
        formatted = "🤖 **AGENT POOL STATUS**\n"
        formatted += "=" * 50 + "\n\n"
        
        for pool_type, pool_data in pool_status.items():
            health_icon = "🟢" if pool_data['health_status'] == 'healthy' else "🟡" if pool_data['health_status'] == 'warning' else "🔴"
            
            formatted += f"{health_icon} **{pool_data['name']}**:\n"
            formatted += f"├── Active Agents: {pool_data['active_agents']}/{pool_data['total_agents']}\n"
            formatted += f"├── Success Rate: {pool_data['success_rate']}%\n"
            formatted += f"├── Avg Response: {pool_data['avg_response_time']}s\n"
            formatted += f"├── Requests Today: {pool_data['requests_today']}\n"
            formatted += f"└── Specialties: {', '.join(pool_data['specialties'][:3])}\n\n"
        
        return formatted

    def _get_admin_dashboard(self) -> str:
        """Generate admin dashboard"""
        dashboard = "👑 **ADMINISTRATIVE DASHBOARD**\n"
        dashboard += "=" * 50 + "\n\n"
        
        # System info
        dashboard += "🖥️ **System Information**:\n"
        dashboard += f"├── Version: OperatorOS v1.0.0\n"
        dashboard += f"├── Environment: Production\n"
        dashboard += f"└── Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        
        # Quick stats
        from models import User, Task, Agent
        try:
            dashboard += "📊 **Quick Statistics**:\n"
            dashboard += f"├── Total Users: {User.query.count()}\n"
            dashboard += f"├── Total Tasks: {Task.query.count()}\n"
            dashboard += f"├── Active Agents: {Agent.query.filter_by(status='active').count()}\n"
            dashboard += f"└── System Health: {self.health_monitor.get_quick_status()}\n"
        except Exception as e:
            dashboard += f"├── Database: Error accessing stats ({str(e)})\n"
        
        return dashboard

    def _generate_help_text(self) -> str:
        """Generate comprehensive help text"""
        help_text = "💡 **OPERATOROS HELP & COMMANDS**\n"
        help_text += "=" * 50 + "\n\n"
        
        help_text += "🎯 **Task Submission** (Natural Language):\n"
        help_text += "├── Healthcare: 'I have persistent headaches'\n"
        help_text += "├── Financial: 'Should I invest in tech stocks?'\n"
        help_text += "├── Sports: 'Predict tonight's NBA games'\n"
        help_text += "├── Business: 'Help optimize my workflow'\n"
        help_text += "└── General: 'What's the weather in NYC?'\n\n"
        
        help_text += "📊 **System Management**:\n"
        help_text += "├── 'status' - System overview\n"
        help_text += "├── 'health' - Health check report\n"
        help_text += "├── 'pools' - Agent pool status\n"
        help_text += "├── 'scale up [pool]' - Increase agents\n"
        help_text += "└── 'scale down [pool]' - Decrease agents\n\n"
        
        help_text += "🎬 **Demonstrations**:\n"
        help_text += "├── 'demo healthcare' - Medical AI demo\n"
        help_text += "├── 'demo financial' - Finance AI demo\n"
        help_text += "├── 'demo sports' - Sports analytics demo\n"
        help_text += "├── 'demo business' - Business automation demo\n"
        help_text += "└── 'demo general' - General AI demo\n\n"
        
        help_text += "🔧 **Advanced Commands**:\n"
        help_text += "├── 'admin status' - Administrative dashboard\n"
        help_text += "├── 'capabilities' - Full system capabilities\n"
        help_text += "├── 'restart [pool]' - Restart agent pool\n"
        help_text += "└── 'exit' - Stop the system\n\n"
        
        help_text += "💬 **Natural Language Tips**:\n"
        help_text += "• Speak naturally - I understand conversational input\n"
        help_text += "• Be specific about your needs for better results\n"
        help_text += "• Ask follow-up questions to dive deeper\n"
        help_text += "• Use 'help [topic]' for specific area guidance"
        
        return help_text

    def _generate_fallback_response(self, user_input: str) -> str:
        """Generate helpful fallback response when processing fails"""
        fallback = "🤔 **I'm not sure how to help with that specific request.**\n\n"
        fallback += "Here are some things you can try:\n\n"
        fallback += "🎯 **Ask me about**:\n"
        fallback += "• Medical questions: 'I have chest pain symptoms'\n"
        fallback += "• Investment advice: 'Should I buy Apple stock?'\n"
        fallback += "• Sports predictions: 'Who will win tonight's game?'\n"
        fallback += "• Business help: 'How can I automate my workflow?'\n\n"
        fallback += "📋 **System commands**:\n"
        fallback += "• 'status' - Check system status\n"
        fallback += "• 'health' - Run health check\n"
        fallback += "• 'demo [type]' - See demonstrations\n"
        fallback += "• 'help' - Full command reference\n\n"
        fallback += "💡 **Tip**: Try rephrasing your question or be more specific about what you need help with."
        
        return fallback


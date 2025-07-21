import logging
import sys
import threading
import time
from typing import Dict, Any, Optional
from datetime import datetime
from conversation_manager import ConversationManager
from command_processor import CommandProcessor
from demo_runner import DemoRunner
from agent_master_controller import AgentMasterController
from health_monitor import HealthMonitor

class ReplitInterface:
    """
    Core interface between Replit Agent and OperatorOS
    Handles natural language interactions and system orchestration
    """
    
    def __init__(self):
        # Initialize core components
        self.conversation_manager = ConversationManager()
        self.command_processor = CommandProcessor()
        self.demo_runner = DemoRunner()
        self.agent_controller = AgentMasterController()
        self.health_monitor = HealthMonitor()
        
        # System state
        self.is_running = False
        self.current_user_session = None
        
        # Initialize and start background services
        self._initialize_system()
        
        logging.info("🚀 Replit Interface initialized and ready")

    def _initialize_system(self):
        """Initialize and start all system components"""
        try:
            # Start agent master controller
            self.agent_controller.start()
            
            # Start health monitoring
            self.health_monitor.start_monitoring()
            
            logging.info("✅ All system components initialized successfully")
            
        except Exception as e:
            logging.error(f"❌ System initialization failed: {e}")
            raise e

    def start_interactive_mode(self):
        """Start interactive mode for Replit Agent conversations"""
        self.is_running = True
        logging.info("💬 Starting Replit Agent interactive mode...")
        
        print("\n" + "="*60)
        print("🤖 OPERATOROS - AI AGENT ORCHESTRATION PLATFORM")
        print("💬 Replit Agent Conversational Interface Active")
        print("="*60)
        print("\n✨ Ready for natural language commands!")
        print("💡 Try commands like:")
        print("   • 'status' - System overview")
        print("   • 'health' - Health check")
        print("   • 'demo healthcare' - Healthcare demo")
        print("   • 'I need help with chest pain symptoms' - Task submission")
        print("   • 'help' - Show all commands")
        print("   • 'exit' - Stop the system")
        print("-" * 60)
        
        # Main interaction loop
        while self.is_running:
            try:
                # Get user input
                user_input = input("\n🎯 OperatorOS > ").strip()
                
                if not user_input:
                    continue
                
                # Handle exit commands
                if user_input.lower() in ['exit', 'quit', 'stop']:
                    print("👋 Shutting down OperatorOS...")
                    self.stop_system()
                    break
                
                # Process the command through conversational interface
                response = self.process_conversation_input(user_input)
                
                # Display response
                print(f"\n{response}\n")
                
            except KeyboardInterrupt:
                print("\n👋 Shutting down OperatorOS...")
                self.stop_system()
                break
            except Exception as e:
                logging.error(f"Error in interactive mode: {e}")
                print(f"\n❌ Error processing command: {str(e)}\n")

    def process_conversation_input(self, user_input: str, user_id: Optional[int] = None) -> str:
        """Process user input through conversational interface"""
        try:
            # Use default user ID if not provided (for interactive mode)
            if user_id is None:
                user_id = 1  # Default user for interactive sessions
            
            # Get or create conversation session
            session = self.conversation_manager.get_or_create_session(user_id, 'replit_agent')
            
            logging.info(f"🎯 Processing input from user {user_id}: {user_input[:100]}...")
            
            # Process through command processor
            command_result = self.command_processor.process_command(user_input, user_id, session)
            
            # Update conversation context
            self.conversation_manager.add_interaction(
                user_id,
                user_input,
                command_result.get('response', 'No response generated'),
                command_result.get('command_type', 'unknown')
            )
            
            # Format response for conversational display
            response = self._format_conversational_response(command_result, user_input)
            
            return response
            
        except Exception as e:
            logging.error(f"Error processing conversation input: {e}")
            return f"❌ **System Error**\n\nI encountered an error processing your request: {str(e)}\n\nPlease try again or use 'help' for available commands."

    def _format_conversational_response(self, command_result: Dict[str, Any], original_input: str) -> str:
        """Format command results for natural conversational display"""
        try:
            if command_result.get('error'):
                return f"❌ **Error**: {command_result['error']}"
            
            response = command_result.get('response', 'No response generated')
            command_type = command_result.get('command_type', 'unknown')
            
            # Add conversational context
            if command_type == 'system_status':
                return f"📊 Here's your system overview:\n\n{response}"
            elif command_type == 'health_check':
                return f"🏥 System health report:\n\n{response}"
            elif command_type == 'task_submission':
                return f"✅ Task submitted successfully!\n\n{response}"
            elif command_type == 'demo':
                return f"🎬 Here's your demo:\n\n{response}"
            elif command_type == 'help':
                return f"💡 Here's how I can help you:\n\n{response}"
            elif command_type == 'agent_management':
                return f"🤖 Agent pool update:\n\n{response}"
            else:
                return response
                
        except Exception as e:
            logging.error(f"Error formatting conversational response: {e}")
            return f"Response formatting error: {str(e)}"

    def handle_task_submission(self, query: str, user_id: int, task_type: Optional[str] = None) -> Dict[str, Any]:
        """Handle task submission through conversational interface"""
        try:
            from models import Task, User
            from app import db
            
            # Ensure user exists
            user = User.query.get(user_id)
            if not user:
                user = User(
                    id=user_id,
                    replit_session_id=f"replit_session_{user_id}_{int(time.time())}",
                    username=f"user_{user_id}"
                )
                db.session.add(user)
                db.session.commit()
            
            # Auto-detect task type if not provided
            if not task_type:
                task_type = self.command_processor._detect_task_type(query)
            
            # Create task
            task = Task(
                user_id=user_id,
                query=query,
                task_type=task_type,
                priority=5,
                metadata={'submitted_via': 'replit_agent'}
            )
            
            db.session.add(task)
            db.session.commit()
            
            # Process task through agent controller
            result = self.agent_controller.process_task(task.id)
            
            return {
                'success': True,
                'task_id': task.id,
                'task_type': task_type,
                'result': result
            }
            
        except Exception as e:
            logging.error(f"Error handling task submission: {e}")
            return {
                'success': False,
                'error': str(e)
            }

    def get_system_overview(self) -> str:
        """Get comprehensive system overview for conversational display"""
        try:
            # Get system status from agent controller
            status = self.agent_controller.get_system_status()
            
            overview = "🤖 **OPERATOROS SYSTEM OVERVIEW**\n"
            overview += "=" * 50 + "\n\n"
            
            # Agent Pools Status
            if 'pools' in status:
                overview += "📊 **Agent Pool Status**:\n"
                for pool in status['pools']:
                    efficiency = pool.get('efficiency', 0)
                    efficiency_icon = "🟢" if efficiency > 80 else "🟡" if efficiency > 60 else "🔴"
                    
                    overview += f"├── {efficiency_icon} **{pool['name'].title()}**: "
                    overview += f"{pool['active']}/{pool['current']} active ({efficiency}% efficiency)\n"
                overview += "\n"
            
            # System Performance
            if 'performance' in status:
                perf = status['performance']
                overview += "⚡ **System Performance**:\n"
                overview += f"├── Avg Response Time: {perf.get('avg_response_time', 'N/A')}s\n"
                overview += f"└── Uptime: {perf.get('uptime', 'N/A')}%\n\n"
            
            # Task Activity
            if 'tasks' in status:
                tasks = status['tasks']
                overview += "📋 **Task Activity Today**:\n"
                overview += f"├── Completed: {tasks.get('completed_today', 0)}\n"
                overview += f"├── Processing: {tasks.get('processing', 0)}\n"
                overview += f"├── Pending: {tasks.get('pending', 0)}\n"
                overview += f"└── Success Rate: {tasks.get('success_rate', 0)}%\n\n"
            
            # Quick Health Status
            health_status = self.health_monitor.get_quick_status()
            overview += f"🏥 **{health_status}**\n\n"
            
            overview += "💡 **Available Commands**:\n"
            overview += "├── 'health' - Detailed health report\n"
            overview += "├── 'pools' - Agent pool management\n"
            overview += "├── 'demo [type]' - Run interactive demos\n"
            overview += "└── 'help' - Complete command reference\n"
            
            overview += f"\n⏰ **Status as of**: {datetime.now().strftime('%H:%M:%S')}"
            
            return overview
            
        except Exception as e:
            logging.error(f"Error getting system overview: {e}")
            return f"❌ Error generating system overview: {str(e)}"

    def handle_scaling_request(self, pool_name: str, direction: str, count: int = 1) -> str:
        """Handle agent pool scaling through conversational interface"""
        try:
            result = self.agent_controller.scale_pool(pool_name, direction, count)
            
            if result.get('error'):
                return f"❌ **Scaling Failed**\n\n{result['error']}"
            
            response = f"⚡ **Agent Pool Scaled Successfully**\n\n"
            response += f"📊 **Pool**: {pool_name.title()}\n"
            response += f"📈 **Action**: Scaled {direction} by {count} agent{'s' if count != 1 else ''}\n"
            response += f"🤖 **New Count**: {result.get('new_count', 'Unknown')} agents\n"
            response += f"✅ **Status**: {result.get('message', 'Operation completed')}"
            
            return response
            
        except Exception as e:
            logging.error(f"Error handling scaling request: {e}")
            return f"❌ Error scaling pool: {str(e)}"

    def get_conversation_context(self, user_id: int) -> Dict[str, Any]:
        """Get current conversation context for a user"""
        try:
            return self.conversation_manager.get_session_context(user_id)
        except Exception as e:
            logging.error(f"Error getting conversation context: {e}")
            return {}

    def handle_admin_command(self, command: str, user_id: int) -> str:
        """Handle administrative commands through conversational interface"""
        try:
            if not self._is_admin_user(user_id):
                return "❌ **Access Denied**: Administrative privileges required for this command."
            
            if command.startswith('admin status'):
                return self._get_admin_status()
            elif command.startswith('admin logs'):
                return self._get_system_logs()
            elif command.startswith('admin users'):
                return self._get_user_sessions()
            elif command.startswith('admin backup'):
                return self._initiate_backup()
            else:
                return "❌ **Unknown Admin Command**: Use 'help admin' for administrative commands."
                
        except Exception as e:
            logging.error(f"Error handling admin command: {e}")
            return f"❌ Admin command error: {str(e)}"

    def _is_admin_user(self, user_id: int) -> bool:
        """Check if user has administrative privileges"""
        # In production, this would check against a proper user permissions system
        return user_id == 1  # Default admin user for demo

    def _get_admin_status(self) -> str:
        """Get administrative status dashboard"""
        try:
            status = "👑 **OPERATOROS ADMINISTRATIVE DASHBOARD**\n"
            status += "=" * 50 + "\n\n"
            
            # System uptime and version info
            status += "🖥️ **System Information**:\n"
            status += f"├── Version: OperatorOS v1.0.0\n"
            status += f"├── Environment: Production\n"
            status += f"└── Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
            
            # Database statistics
            from models import User, Task, Agent, AgentPool
            status += "🗄️ **Database Statistics**:\n"
            status += f"├── Total Users: {User.query.count()}\n"
            status += f"├── Total Tasks: {Task.query.count()}\n"
            status += f"├── Active Agents: {Agent.query.filter_by(status='active').count()}\n"
            status += f"└── Agent Pools: {AgentPool.query.count()}\n\n"
            
            # Performance metrics
            status += "📊 **Performance Metrics**:\n"
            status += f"├── Memory Usage: {self.health_monitor.health_data.get('system', {}).get('memory_usage', 'N/A')}%\n"
            status += f"├── CPU Usage: {self.health_monitor.health_data.get('system', {}).get('cpu_usage', 'N/A')}%\n"
            status += f"└── Active Connections: {len(self.conversation_manager.active_sessions)}\n"
            
            return status
            
        except Exception as e:
            logging.error(f"Error getting admin status: {e}")
            return f"❌ Error retrieving admin status: {str(e)}"

    def _get_system_logs(self) -> str:
        """Get recent system logs"""
        return "📋 **Recent System Logs** (Last 10 entries):\n\nLog viewing feature would be implemented here in production.\nFor now, check the console output for real-time logs."

    def _get_user_sessions(self) -> str:
        """Get active user sessions"""
        try:
            sessions = self.conversation_manager.get_all_sessions()
            
            if not sessions:
                return "👥 **No Active User Sessions**"
            
            status = "👥 **Active User Sessions**:\n\n"
            for session_id, session_data in sessions.items():
                status += f"├── **User {session_data.get('user_id')}**: {session_data.get('message_count', 0)} messages\n"
                status += f"│   └── Last Active: {session_data.get('last_active', 'Unknown')}\n"
            
            return status
            
        except Exception as e:
            logging.error(f"Error getting user sessions: {e}")
            return f"❌ Error retrieving user sessions: {str(e)}"

    def _initiate_backup(self) -> str:
        """Initiate system backup"""
        return "💾 **System Backup**: Backup functionality would be implemented here in production.\nThis would include database backup, configuration backup, and log archival."

    def stop_system(self):
        """Gracefully stop all system components"""
        try:
            logging.info("🛑 Stopping OperatorOS system...")
            
            self.is_running = False
            
            # Stop health monitoring
            self.health_monitor.stop_monitoring()
            
            # Stop agent controller
            self.agent_controller.stop()
            
            # Clean up conversation manager
            self.conversation_manager.cleanup()
            
            logging.info("✅ OperatorOS system stopped successfully")
            
        except Exception as e:
            logging.error(f"Error stopping system: {e}")

    def get_system_capabilities(self) -> str:
        """Get comprehensive list of system capabilities"""
        try:
            capabilities = "🚀 **OPERATOROS CAPABILITIES**\n"
            capabilities += "=" * 50 + "\n\n"
            
            capabilities += "🤖 **AI Agent Pools**:\n"
            capabilities += "├── Healthcare: Medical advice and symptom analysis\n"
            capabilities += "├── Financial: Investment advice and market analysis\n" 
            capabilities += "├── Sports: Game predictions and analytics\n"
            capabilities += "├── Business: Process automation and optimization\n"
            capabilities += "└── General: Wide-ranging knowledge assistance\n\n"
            
            capabilities += "⚙️ **System Management**:\n"
            capabilities += "├── Real-time health monitoring\n"
            capabilities += "├── Auto-scaling agent pools\n"
            capabilities += "├── Task queue processing\n"
            capabilities += "├── Performance analytics\n"
            capabilities += "└── Administrative controls\n\n"
            
            capabilities += "💬 **Conversational Interface**:\n"
            capabilities += "├── Natural language command processing\n"
            capabilities += "├── Multi-user session management\n"
            capabilities += "├── Context-aware interactions\n"
            capabilities += "├── Interactive demonstrations\n"
            capabilities += "└── Real-time status updates\n\n"
            
            capabilities += "🔧 **Enterprise Features**:\n"
            capabilities += "├── OpenAI Assistants integration\n"
            capabilities += "├── Multi-provider AI routing\n"
            capabilities += "├── Persistent conversation context\n"
            capabilities += "├── Automated error recovery\n"
            capabilities += "└── Comprehensive logging and monitoring"
            
            return capabilities
            
        except Exception as e:
            logging.error(f"Error getting system capabilities: {e}")
            return f"❌ Error retrieving capabilities: {str(e)}"

    def format_welcome_message(self) -> str:
        """Format welcome message for new users"""
        welcome = "🎉 **Welcome to OperatorOS!**\n\n"
        welcome += "I'm your AI orchestration platform, accessible entirely through this conversational interface. "
        welcome += "I manage multiple specialized AI agents that can help you with:\n\n"
        welcome += "🏥 **Healthcare**: Medical advice and symptom analysis\n"
        welcome += "💰 **Finance**: Investment advice and market analysis\n"  
        welcome += "🏈 **Sports**: Game predictions and analytics\n"
        welcome += "💼 **Business**: Process automation and optimization\n"
        welcome += "📚 **General**: Knowledge and research assistance\n\n"
        welcome += "💡 **Quick Start**:\n"
        welcome += "• Try: 'I need medical advice about headaches'\n"
        welcome += "• Or: 'Should I invest in tech stocks?'\n"
        welcome += "• Or: 'demo healthcare' for a demonstration\n"
        welcome += "• Or: 'help' for complete command reference\n\n"
        welcome += "Let's get started! What can I help you with today? 🚀"
        
        return welcome


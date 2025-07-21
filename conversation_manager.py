import logging
import json
import threading
from typing import Dict, Any, Optional, List
from datetime import datetime, timedelta
from dataclasses import dataclass, asdict
from models import User, Conversation
from app import db

@dataclass
class ConversationSession:
    """Represents an active conversation session"""
    user_id: int
    session_id: str
    session_type: str
    created_at: datetime
    last_active: datetime
    message_count: int
    context_data: Dict[str, Any]
    conversation_history: List[Dict[str, Any]]

class ConversationManager:
    """
    Multi-user conversation state and session management
    Handles conversation context, history, and persistence for Replit Agent interactions
    """
    
    def __init__(self):
        self.active_sessions = {}
        self.session_lock = threading.Lock()
        self.max_session_history = 50  # Maximum messages to keep in memory
        self.session_timeout = timedelta(hours=1)  # Session expires after 1 hour of inactivity
        
        # Context tracking
        self.context_weights = {
            'recent_queries': 0.4,
            'user_preferences': 0.3,
            'session_context': 0.2,
            'conversation_flow': 0.1
        }
        
        logging.info("💬 Conversation Manager initialized")

    def get_or_create_session(self, user_id: int, session_type: str = 'replit_agent') -> ConversationSession:
        """Get existing conversation session or create new one"""
        try:
            with self.session_lock:
                session_key = f"{user_id}_{session_type}"
                
                # Check if session exists and is still valid
                if session_key in self.active_sessions:
                    session = self.active_sessions[session_key]
                    
                    # Check if session has expired
                    if datetime.utcnow() - session.last_active > self.session_timeout:
                        logging.info(f"Session {session_key} expired, creating new session")
                        del self.active_sessions[session_key]
                    else:
                        # Update last active time
                        session.last_active = datetime.utcnow()
                        return session
                
                # Create new session
                session = self._create_new_session(user_id, session_type)
                self.active_sessions[session_key] = session
                
                logging.info(f"📱 Created new conversation session for user {user_id}")
                return session
                
        except Exception as e:
            logging.error(f"Error getting/creating session: {e}")
            # Return a minimal fallback session
            return ConversationSession(
                user_id=user_id,
                session_id=f"fallback_{user_id}_{int(datetime.utcnow().timestamp())}",
                session_type=session_type,
                created_at=datetime.utcnow(),
                last_active=datetime.utcnow(),
                message_count=0,
                context_data={},
                conversation_history=[]
            )

    def _create_new_session(self, user_id: int, session_type: str) -> ConversationSession:
        """Create a new conversation session"""
        try:
            # Ensure user exists in database
            user = User.query.get(user_id)
            if not user:
                user = User(
                    id=user_id,
                    replit_session_id=f"replit_{user_id}_{int(datetime.utcnow().timestamp())}",
                    username=f"user_{user_id}",
                    created_at=datetime.utcnow(),
                    last_active=datetime.utcnow()
                )
                db.session.add(user)
                db.session.commit()
            
            # Load conversation history from database
            conversation_history = self._load_conversation_history(user_id, session_type)
            
            # Create session object
            session_id = f"session_{user_id}_{session_type}_{int(datetime.utcnow().timestamp())}"
            
            session = ConversationSession(
                user_id=user_id,
                session_id=session_id,
                session_type=session_type,
                created_at=datetime.utcnow(),
                last_active=datetime.utcnow(),
                message_count=len(conversation_history),
                context_data=self._initialize_context_data(user_id),
                conversation_history=conversation_history
            )
            
            return session
            
        except Exception as e:
            logging.error(f"Error creating new session: {e}")
            raise e

    def _load_conversation_history(self, user_id: int, session_type: str) -> List[Dict[str, Any]]:
        """Load recent conversation history from database"""
        try:
            # Get recent conversations of this type
            conversations = Conversation.query.filter_by(
                user_id=user_id,
                conversation_type=session_type
            ).order_by(Conversation.last_message_at.desc()).limit(5).all()
            
            history = []
            for conv in conversations:
                if conv.conversation_data:
                    # Extract last few messages from each conversation
                    messages = conv.conversation_data.get('recent_messages', [])
                    history.extend(messages[-5:])  # Last 5 messages from each conversation
            
            # Return most recent messages first
            return history[-self.max_session_history:]
            
        except Exception as e:
            logging.error(f"Error loading conversation history: {e}")
            return []

    def _initialize_context_data(self, user_id: int) -> Dict[str, Any]:
        """Initialize context data for new session"""
        try:
            # Load user preferences and context from database
            user = User.query.get(user_id)
            
            context_data = {
                'user_preferences': user.session_data if user and user.session_data else {},
                'conversation_topics': [],
                'recent_task_types': [],
                'interaction_patterns': {
                    'preferred_response_style': 'detailed',
                    'technical_level': 'intermediate',
                    'common_domains': []
                },
                'session_metadata': {
                    'start_time': datetime.utcnow().isoformat(),
                    'platform': 'replit_agent',
                    'session_version': '1.0'
                }
            }
            
            return context_data
            
        except Exception as e:
            logging.error(f"Error initializing context data: {e}")
            return {}

    def add_interaction(self, user_id: int, user_message: str, ai_response: str, 
                       interaction_type: str = 'general') -> None:
        """Add interaction to conversation history and update context"""
        try:
            with self.session_lock:
                session_key = f"{user_id}_replit_agent"
                
                if session_key not in self.active_sessions:
                    # Create session if it doesn't exist
                    self.get_or_create_session(user_id)
                
                session = self.active_sessions[session_key]
                
                # Create interaction record
                interaction = {
                    'timestamp': datetime.utcnow().isoformat(),
                    'user_message': user_message,
                    'ai_response': ai_response,
                    'interaction_type': interaction_type,
                    'message_id': f"msg_{session.message_count + 1}"
                }
                
                # Add to conversation history
                session.conversation_history.append(interaction)
                session.message_count += 1
                session.last_active = datetime.utcnow()
                
                # Trim history if too long
                if len(session.conversation_history) > self.max_session_history:
                    session.conversation_history = session.conversation_history[-self.max_session_history:]
                
                # Update context based on interaction
                self._update_context_from_interaction(session, interaction)
                
                # Persist to database periodically
                if session.message_count % 5 == 0:  # Every 5 messages
                    self._persist_session_to_database(session)
                
                logging.debug(f"Added interaction to session {session_key}")
                
        except Exception as e:
            logging.error(f"Error adding interaction: {e}")

    def _update_context_from_interaction(self, session: ConversationSession, interaction: Dict[str, Any]) -> None:
        """Update session context based on interaction"""
        try:
            # Extract topics and keywords
            user_message = interaction['user_message'].lower()
            interaction_type = interaction['interaction_type']
            
            # Update conversation topics
            topics = session.context_data.get('conversation_topics', [])
            if interaction_type not in topics:
                topics.append(interaction_type)
                session.context_data['conversation_topics'] = topics[-10:]  # Keep last 10 topics
            
            # Track recent task types
            if interaction_type in ['healthcare', 'financial', 'sports', 'business', 'general']:
                recent_tasks = session.context_data.get('recent_task_types', [])
                recent_tasks.append({
                    'task_type': interaction_type,
                    'timestamp': datetime.utcnow().isoformat()
                })
                session.context_data['recent_task_types'] = recent_tasks[-20:]  # Keep last 20
            
            # Update interaction patterns
            patterns = session.context_data.get('interaction_patterns', {})
            
            # Detect technical level from user messages
            technical_keywords = ['api', 'algorithm', 'database', 'server', 'configuration']
            if any(keyword in user_message for keyword in technical_keywords):
                patterns['technical_level'] = 'advanced'
            
            # Detect response style preference
            if any(phrase in user_message for phrase in ['brief', 'short', 'quick', 'summary']):
                patterns['preferred_response_style'] = 'concise'
            elif any(phrase in user_message for phrase in ['detail', 'explain', 'comprehensive']):
                patterns['preferred_response_style'] = 'detailed'
            
            session.context_data['interaction_patterns'] = patterns
            
        except Exception as e:
            logging.error(f"Error updating context: {e}")

    def get_session_context(self, user_id: int) -> Dict[str, Any]:
        """Get current session context for user"""
        try:
            with self.session_lock:
                session_key = f"{user_id}_replit_agent"
                
                if session_key not in self.active_sessions:
                    return {}
                
                session = self.active_sessions[session_key]
                
                # Build comprehensive context
                context = {
                    'session_info': {
                        'user_id': session.user_id,
                        'session_id': session.session_id,
                        'message_count': session.message_count,
                        'created_at': session.created_at.isoformat(),
                        'last_active': session.last_active.isoformat()
                    },
                    'conversation_context': {
                        'recent_topics': session.context_data.get('conversation_topics', [])[-5:],
                        'recent_interactions': len(session.conversation_history),
                        'dominant_task_type': self._get_dominant_task_type(session),
                        'conversation_flow': self._analyze_conversation_flow(session)
                    },
                    'user_preferences': session.context_data.get('user_preferences', {}),
                    'interaction_patterns': session.context_data.get('interaction_patterns', {}),
                    'contextual_hints': self._generate_contextual_hints(session)
                }
                
                return context
                
        except Exception as e:
            logging.error(f"Error getting session context: {e}")
            return {}

    def _get_dominant_task_type(self, session: ConversationSession) -> str:
        """Analyze and return the dominant task type in recent interactions"""
        try:
            recent_tasks = session.context_data.get('recent_task_types', [])
            
            if not recent_tasks:
                return 'general'
            
            # Count task types in recent interactions
            task_counts = {}
            recent_cutoff = datetime.utcnow() - timedelta(minutes=30)
            
            for task in recent_tasks:
                task_time = datetime.fromisoformat(task['timestamp'])
                if task_time > recent_cutoff:
                    task_type = task['task_type']
                    task_counts[task_type] = task_counts.get(task_type, 0) + 1
            
            if task_counts:
                return max(task_counts, key=task_counts.get)
            else:
                return 'general'
                
        except Exception as e:
            logging.error(f"Error getting dominant task type: {e}")
            return 'general'

    def _analyze_conversation_flow(self, session: ConversationSession) -> Dict[str, Any]:
        """Analyze conversation flow patterns"""
        try:
            history = session.conversation_history
            
            if len(history) < 2:
                return {'pattern': 'new_conversation'}
            
            # Analyze recent interactions
            recent_interactions = history[-5:]  # Last 5 interactions
            
            # Check for patterns
            interaction_types = [interaction['interaction_type'] for interaction in recent_interactions]
            
            # Detect pattern
            if len(set(interaction_types)) == 1:
                pattern = f'focused_{interaction_types[0]}'
            elif len(set(interaction_types)) >= 3:
                pattern = 'multi_domain'
            else:
                pattern = 'mixed'
            
            # Calculate engagement level
            avg_message_length = sum(len(interaction['user_message']) for interaction in recent_interactions) / len(recent_interactions)
            engagement_level = 'high' if avg_message_length > 100 else 'medium' if avg_message_length > 50 else 'low'
            
            return {
                'pattern': pattern,
                'engagement_level': engagement_level,
                'recent_types': interaction_types,
                'conversation_depth': len(history)
            }
            
        except Exception as e:
            logging.error(f"Error analyzing conversation flow: {e}")
            return {'pattern': 'unknown'}

    def _generate_contextual_hints(self, session: ConversationSession) -> List[str]:
        """Generate contextual hints based on session data"""
        hints = []
        
        try:
            # Based on dominant task type
            dominant_type = self._get_dominant_task_type(session)
            if dominant_type == 'healthcare':
                hints.append("Consider asking for follow-up medical advice or health-related questions")
            elif dominant_type == 'financial':
                hints.append("You might want to explore portfolio analysis or investment strategies")
            elif dominant_type == 'sports':
                hints.append("Try asking for more game predictions or player analysis")
            elif dominant_type == 'business':
                hints.append("Consider exploring workflow automation or business optimization")
            
            # Based on interaction patterns
            patterns = session.context_data.get('interaction_patterns', {})
            if patterns.get('technical_level') == 'advanced':
                hints.append("User prefers technical details and advanced explanations")
            
            # Based on conversation flow
            if session.message_count > 10:
                hints.append("Extended conversation - user is highly engaged")
            
            # Based on recent topics
            recent_topics = session.context_data.get('conversation_topics', [])
            if len(set(recent_topics)) > 3:
                hints.append("User explores multiple domains - provide comprehensive responses")
            
            return hints[:3]  # Return top 3 hints
            
        except Exception as e:
            logging.error(f"Error generating contextual hints: {e}")
            return []

    def _persist_session_to_database(self, session: ConversationSession) -> None:
        """Persist session data to database"""
        try:
            # Update user's session data
            user = User.query.get(session.user_id)
            if user:
                user.last_active = session.last_active
                user.session_data = session.context_data
                
                # Create or update conversation record
                conversation = Conversation.query.filter_by(
                    user_id=session.user_id,
                    conversation_type=session.session_type
                ).first()
                
                if not conversation:
                    conversation = Conversation(
                        user_id=session.user_id,
                        conversation_type=session.session_type,
                        created_at=session.created_at
                    )
                    db.session.add(conversation)
                
                conversation.last_message_at = session.last_active
                conversation.message_count = session.message_count
                conversation.conversation_data = {
                    'recent_messages': session.conversation_history[-10:],  # Last 10 messages
                    'context_summary': session.context_data,
                    'session_id': session.session_id
                }
                
                db.session.commit()
                logging.debug(f"Persisted session data for user {session.user_id}")
                
        except Exception as e:
            logging.error(f"Error persisting session: {e}")
            db.session.rollback()

    def get_conversation_summary(self, user_id: int) -> str:
        """Get conversation summary for display"""
        try:
            context = self.get_session_context(user_id)
            
            if not context:
                return "No active conversation session"
            
            session_info = context['session_info']
            conv_context = context['conversation_context']
            
            summary = f"💬 **Conversation Summary**\n\n"
            summary += f"📊 **Session Info**:\n"
            summary += f"├── Messages: {session_info['message_count']}\n"
            summary += f"├── Duration: {self._format_duration(session_info['created_at'])}\n"
            summary += f"└── Last Active: {self._format_time(session_info['last_active'])}\n\n"
            
            summary += f"🎯 **Conversation Context**:\n"
            summary += f"├── Primary Focus: {conv_context['dominant_task_type'].title()}\n"
            summary += f"├── Recent Topics: {', '.join(conv_context['recent_topics'])}\n"
            summary += f"└── Engagement: {conv_context['conversation_flow']['engagement_level'].title()}\n\n"
            
            # Add contextual hints
            hints = context.get('contextual_hints', [])
            if hints:
                summary += f"💡 **Contextual Insights**:\n"
                for i, hint in enumerate(hints, 1):
                    summary += f"{i}. {hint}\n"
            
            return summary
            
        except Exception as e:
            logging.error(f"Error getting conversation summary: {e}")
            return f"Error generating summary: {str(e)}"

    def _format_duration(self, start_time_str: str) -> str:
        """Format duration since start time"""
        try:
            start_time = datetime.fromisoformat(start_time_str)
            duration = datetime.utcnow() - start_time
            
            if duration.total_seconds() < 60:
                return "< 1 minute"
            elif duration.total_seconds() < 3600:
                return f"{int(duration.total_seconds() // 60)} minutes"
            else:
                hours = int(duration.total_seconds() // 3600)
                minutes = int((duration.total_seconds() % 3600) // 60)
                return f"{hours}h {minutes}m"
                
        except Exception:
            return "Unknown"

    def _format_time(self, time_str: str) -> str:
        """Format timestamp for display"""
        try:
            time_obj = datetime.fromisoformat(time_str)
            return time_obj.strftime('%H:%M:%S')
        except Exception:
            return "Unknown"

    def clear_session(self, user_id: int) -> bool:
        """Clear/reset a user's conversation session"""
        try:
            with self.session_lock:
                session_key = f"{user_id}_replit_agent"
                
                if session_key in self.active_sessions:
                    del self.active_sessions[session_key]
                    logging.info(f"Cleared session for user {user_id}")
                    return True
                
                return False
                
        except Exception as e:
            logging.error(f"Error clearing session: {e}")
            return False

    def get_all_sessions(self) -> Dict[str, Dict[str, Any]]:
        """Get information about all active sessions"""
        try:
            with self.session_lock:
                sessions_info = {}
                
                for session_key, session in self.active_sessions.items():
                    sessions_info[session_key] = {
                        'user_id': session.user_id,
                        'message_count': session.message_count,
                        'created_at': session.created_at.isoformat(),
                        'last_active': session.last_active.isoformat(),
                        'session_type': session.session_type
                    }
                
                return sessions_info
                
        except Exception as e:
            logging.error(f"Error getting all sessions: {e}")
            return {}

    def cleanup_expired_sessions(self) -> int:
        """Clean up expired sessions"""
        cleaned_count = 0
        
        try:
            with self.session_lock:
                expired_sessions = []
                cutoff_time = datetime.utcnow() - self.session_timeout
                
                for session_key, session in self.active_sessions.items():
                    if session.last_active < cutoff_time:
                        expired_sessions.append(session_key)
                
                for session_key in expired_sessions:
                    # Persist final state before cleanup
                    session = self.active_sessions[session_key]
                    self._persist_session_to_database(session)
                    del self.active_sessions[session_key]
                    cleaned_count += 1
                
                if cleaned_count > 0:
                    logging.info(f"Cleaned up {cleaned_count} expired sessions")
                
                return cleaned_count
                
        except Exception as e:
            logging.error(f"Error cleaning up sessions: {e}")
            return 0

    def cleanup(self) -> None:
        """Final cleanup when shutting down"""
        try:
            with self.session_lock:
                # Persist all active sessions
                for session in self.active_sessions.values():
                    self._persist_session_to_database(session)
                
                self.active_sessions.clear()
                logging.info("✅ Conversation Manager cleanup completed")
                
        except Exception as e:
            logging.error(f"Error during cleanup: {e}")


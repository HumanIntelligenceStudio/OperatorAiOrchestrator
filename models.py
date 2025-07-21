from datetime import datetime
from app import db
from sqlalchemy import Text, JSON
from flask_login import UserMixin

class User(UserMixin, db.Model):
    """User model for tracking Replit Agent conversations and sessions"""
    id = db.Column(db.Integer, primary_key=True)
    replit_session_id = db.Column(db.String(255), unique=True, nullable=False)
    username = db.Column(db.String(64), nullable=True)
    email = db.Column(db.String(120), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_active = db.Column(db.DateTime, default=datetime.utcnow)
    session_data = db.Column(JSON, default=dict)
    
    # Relationships
    tasks = db.relationship('Task', backref='user', lazy=True)
    conversations = db.relationship('Conversation', backref='user', lazy=True)

class Agent(db.Model):
    """Agent model for tracking AI agent instances and their status"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    agent_type = db.Column(db.String(50), nullable=False)  # healthcare, financial, sports, business, general
    status = db.Column(db.String(20), default='idle')  # idle, active, failed, maintenance
    provider = db.Column(db.String(50), default='openai')  # openai, anthropic
    model = db.Column(db.String(100), default='gpt-4o')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_used = db.Column(db.DateTime, default=datetime.utcnow)
    performance_metrics = db.Column(JSON, default=dict)
    
    # Relationships
    tasks = db.relationship('Task', backref='agent', lazy=True)

class Task(db.Model):
    """Task model for tracking user requests and AI agent processing"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    agent_id = db.Column(db.Integer, db.ForeignKey('agent.id'), nullable=True)
    query = db.Column(Text, nullable=False)
    task_type = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, processing, completed, failed
    priority = db.Column(db.Integer, default=5)  # 1-10 scale
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    started_at = db.Column(db.DateTime, nullable=True)
    completed_at = db.Column(db.DateTime, nullable=True)
    response = db.Column(Text, nullable=True)
    error_message = db.Column(Text, nullable=True)
    task_metadata = db.Column(JSON, default=dict)

class Conversation(db.Model):
    """Conversation model for OpenAI Assistants integration"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    openai_thread_id = db.Column(db.String(255), unique=True, nullable=True)
    assistant_id = db.Column(db.String(255), nullable=True)
    conversation_type = db.Column(db.String(50), nullable=False)  # healthcare, financial, etc.
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_message_at = db.Column(db.DateTime, default=datetime.utcnow)
    message_count = db.Column(db.Integer, default=0)
    conversation_data = db.Column(JSON, default=dict)

class SystemMetrics(db.Model):
    """System metrics for monitoring and health checks"""
    id = db.Column(db.Integer, primary_key=True)
    metric_name = db.Column(db.String(100), nullable=False)
    metric_value = db.Column(db.Float, nullable=False)
    metric_unit = db.Column(db.String(20), nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    metric_metadata = db.Column(JSON, default=dict)

class AgentPool(db.Model):
    """Agent pool configuration and status"""
    id = db.Column(db.Integer, primary_key=True)
    pool_name = db.Column(db.String(100), unique=True, nullable=False)
    pool_type = db.Column(db.String(50), nullable=False)
    min_agents = db.Column(db.Integer, default=1)
    max_agents = db.Column(db.Integer, default=10)
    current_agents = db.Column(db.Integer, default=0)
    active_agents = db.Column(db.Integer, default=0)
    target_agents = db.Column(db.Integer, default=3)
    auto_scale = db.Column(db.Boolean, default=True)
    health_status = db.Column(db.String(20), default='healthy')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    configuration = db.Column(JSON, default=dict)

from flask import Blueprint, jsonify, request
from datetime import datetime
import logging
from models import Agent, Task, SystemMetrics, AgentPool, User, Conversation
from app import db
from agent_master_controller import AgentMasterController
from health_monitor import HealthMonitor
from sports_data_provider import SportsDataProvider

# Create API blueprint for headless backend
api_bp = Blueprint('api', __name__)

# Controllers will be initialized when needed within routes
agent_controller = None
health_monitor = None

def get_agent_controller():
    global agent_controller
    if agent_controller is None:
        agent_controller = AgentMasterController()
    return agent_controller

def get_health_monitor():
    global health_monitor
    if health_monitor is None:
        health_monitor = HealthMonitor()
    return health_monitor

def get_sports_data_provider():
    return SportsDataProvider()

@api_bp.route('/status', methods=['GET'])
def system_status():
    """Get comprehensive system status"""
    try:
        controller = get_agent_controller()
        controller._initialize_pools()  # Ensure pools are initialized
        status = controller.get_system_status()
        return jsonify({
            'status': 'success',
            'data': status
        }), 200
    except Exception as e:
        logging.error(f"Error getting system status: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@api_bp.route('/agents', methods=['GET'])
def list_agents():
    """List all agents and their status"""
    try:
        agents = Agent.query.all()
        agents_data = []
        for agent in agents:
            agents_data.append({
                'id': agent.id,
                'name': agent.name,
                'type': agent.agent_type,
                'status': agent.status,
                'provider': agent.provider,
                'model': agent.model,
                'last_used': agent.last_used.isoformat() if agent.last_used else None,
                'performance_metrics': agent.performance_metrics
            })
        
        return jsonify({
            'status': 'success',
            'data': {'agents': agents_data}
        }), 200
    except Exception as e:
        logging.error(f"Error listing agents: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@api_bp.route('/tasks', methods=['POST'])
def submit_task():
    """Submit a new task for processing"""
    try:
        data = request.get_json()
        
        # Create new task
        task = Task(
            user_id=data.get('user_id'),
            query=data.get('query'),
            task_type=data.get('task_type'),
            priority=data.get('priority', 5),
            metadata=data.get('metadata', {})
        )
        
        db.session.add(task)
        db.session.commit()
        
        # Process task through agent controller
        result = agent_controller.process_task(task.id)
        
        return jsonify({
            'status': 'success',
            'data': {
                'task_id': task.id,
                'result': result
            }
        }), 200
    except Exception as e:
        logging.error(f"Error submitting task: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@api_bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_task_status(task_id):
    """Get task status and results"""
    try:
        task = Task.query.get_or_404(task_id)
        
        return jsonify({
            'status': 'success',
            'data': {
                'id': task.id,
                'query': task.query,
                'task_type': task.task_type,
                'status': task.status,
                'created_at': task.created_at.isoformat(),
                'completed_at': task.completed_at.isoformat() if task.completed_at else None,
                'response': task.response,
                'error_message': task.error_message,
                'metadata': task.metadata
            }
        }), 200
    except Exception as e:
        logging.error(f"Error getting task status: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@api_bp.route('/pools', methods=['GET'])
def list_pools():
    """List all agent pools and their status"""
    try:
        pools = AgentPool.query.all()
        pools_data = []
        for pool in pools:
            pools_data.append({
                'id': pool.id,
                'name': pool.pool_name,
                'type': pool.pool_type,
                'current_agents': pool.current_agents,
                'active_agents': pool.active_agents,
                'target_agents': pool.target_agents,
                'health_status': pool.health_status,
                'auto_scale': pool.auto_scale
            })
        
        return jsonify({
            'status': 'success',
            'data': {'pools': pools_data}
        }), 200
    except Exception as e:
        logging.error(f"Error listing pools: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@api_bp.route('/pools/<pool_name>/scale', methods=['POST'])
def scale_pool(pool_name):
    """Scale agent pool up or down"""
    try:
        data = request.get_json()
        direction = data.get('direction', 'up')  # up or down
        count = data.get('count', 1)
        
        result = agent_controller.scale_pool(pool_name, direction, count)
        
        return jsonify({
            'status': 'success',
            'data': result
        }), 200
    except Exception as e:
        logging.error(f"Error scaling pool: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@api_bp.route('/health', methods=['GET'])
def health_check():
    """Comprehensive health check endpoint"""
    try:
        health_data = health_monitor.get_health_report()
        
        return jsonify({
            'status': 'success',
            'data': health_data
        }), 200
    except Exception as e:
        logging.error(f"Error during health check: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@api_bp.route('/metrics', methods=['GET'])
def get_metrics():
    """Get system performance metrics"""
    try:
        metrics = SystemMetrics.query.order_by(SystemMetrics.timestamp.desc()).limit(100).all()
        metrics_data = []
        
        for metric in metrics:
            metrics_data.append({
                'name': metric.metric_name,
                'value': metric.metric_value,
                'unit': metric.metric_unit,
                'timestamp': metric.timestamp.isoformat(),
                'metadata': metric.metadata
            })
        
        return jsonify({
            'status': 'success',
            'data': {'metrics': metrics_data}
        }), 200
    except Exception as e:
        logging.error(f"Error getting metrics: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@api_bp.route("/sports/odds/<sport>", methods=["GET"])
def get_sports_odds(sport):
    """Get live sports betting odds"""
    try:
        sports_provider = get_sports_data_provider()
        odds_data = sports_provider.get_sports_betting_odds(sport.upper())
        
        return jsonify({
            "status": "success",
            "data": odds_data,
            "sport": sport,
            "timestamp": datetime.utcnow().isoformat()
        }), 200
        
    except Exception as e:
        logging.error(f"Error fetching sports odds: {e}")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@api_bp.route("/sports/features", methods=["GET"])
def get_sports_features():
    """Get available sports data features"""
    try:
        sports_provider = get_sports_data_provider()
        features = sports_provider.get_available_features()
        
        return jsonify({
            "status": "success",
            "data": features
        }), 200
        
    except Exception as e:
        logging.error(f"Error fetching sports features: {e}")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


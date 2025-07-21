import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from werkzeug.middleware.proxy_fix import ProxyFix

# Configure logging
logging.basicConfig(level=logging.DEBUG)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

# Create the Flask app (headless API backend - no web templates)
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "operatoros_default_secret")
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# Configure the database
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///operatoros.db")
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}

# Initialize the app with the extension
db.init_app(app)

with app.app_context():
    # Import models to ensure tables are created
    import models
    db.create_all()
    logging.info("✅ Database initialized successfully")

# Import and register API routes after app context
from api_routes import api_bp
app.register_blueprint(api_bp, url_prefix='/api')

# Add main web interface routes
@app.route('/')
def index():
    """Main OperatorOS interface"""
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>OperatorOS - Enterprise AI Agent Orchestration</title>
        <link href="https://cdn.replit.com/agent/bootstrap-agent-dark-theme.min.css" rel="stylesheet">
        <style>
            .hero-section {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 4rem 0;
            }
            .feature-card {
                transition: transform 0.3s ease;
                height: 100%;
            }
            .feature-card:hover {
                transform: translateY(-5px);
            }
            .pool-status {
                display: inline-block;
                padding: 0.25rem 0.5rem;
                border-radius: 0.375rem;
                font-size: 0.75rem;
                font-weight: 600;
            }
            .status-ready {
                background-color: #d1fae5;
                color: #065f46;
            }
            .agent-icon {
                font-size: 2rem;
                margin-bottom: 1rem;
            }
        </style>
    </head>
    <body data-bs-theme="dark">
        <!-- Hero Section -->
        <div class="hero-section text-center">
            <div class="container">
                <h1 class="display-4 fw-bold mb-4">🚀 OperatorOS</h1>
                <p class="lead mb-4">Enterprise AI Agent Orchestration Platform</p>
                <p class="mb-4">Powered by Replit Agent Conversational Interface</p>
                <div class="row g-3 justify-content-center">
                    <div class="col-auto">
                        <span class="badge bg-success fs-6">✅ System Operational</span>
                    </div>
                    <div class="col-auto">
                        <span class="badge bg-info fs-6">🤖 5 Agent Pools Active</span>
                    </div>
                    <div class="col-auto">
                        <span class="badge bg-warning fs-6">🧠 OpenAI + Anthropic</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- Main Content -->
        <div class="container my-5">
            
            <!-- Conversational Interface Section -->
            <div class="row mb-5">
                <div class="col-12">
                    <div class="card border-primary">
                        <div class="card-body text-center p-5">
                            <h2 class="card-title mb-4">💬 Conversational Interface</h2>
                            <p class="lead mb-4">
                                OperatorOS uses <strong>Replit Agent</strong> as your complete user interface.
                                Simply talk to Replit Agent using natural language commands!
                            </p>
                            <div class="alert alert-info">
                                <h5>🎯 How to Interact:</h5>
                                <p class="mb-2">Talk to Replit Agent with commands like:</p>
                                <div class="row g-2 text-start">
                                    <div class="col-md-6">
                                        <code>"What's the system status?"</code><br>
                                        <code>"I need medical advice"</code><br>
                                        <code>"Analyze the stock market"</code>
                                    </div>
                                    <div class="col-md-6">
                                        <code>"Scale up healthcare agents"</code><br>
                                        <code>"Help with business automation"</code><br>
                                        <code>"Run a sports analysis"</code>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Agent Pools Section -->
            <div class="row mb-5">
                <div class="col-12">
                    <h2 class="text-center mb-4">🤖 Specialized Agent Pools</h2>
                </div>
                
                <div class="col-md-6 col-lg-4 mb-4">
                    <div class="card feature-card h-100">
                        <div class="card-body text-center">
                            <div class="agent-icon">🏥</div>
                            <h5 class="card-title">Healthcare Pool</h5>
                            <p class="card-text">Medical advice, symptom analysis, health consultations</p>
                            <div class="mb-2">
                                <strong>AI Model:</strong> GPT-4o<br>
                                <strong>Status:</strong> <span class="pool-status status-ready">Ready</span>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="col-md-6 col-lg-4 mb-4">
                    <div class="card feature-card h-100">
                        <div class="card-body text-center">
                            <div class="agent-icon">💰</div>
                            <h5 class="card-title">Financial Pool</h5>
                            <p class="card-text">Investment advice, market analysis, financial planning</p>
                            <div class="mb-2">
                                <strong>AI Model:</strong> Claude Sonnet<br>
                                <strong>Status:</strong> <span class="pool-status status-ready">Ready</span>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="col-md-6 col-lg-4 mb-4">
                    <div class="card feature-card h-100">
                        <div class="card-body text-center">
                            <div class="agent-icon">🏈</div>
                            <h5 class="card-title">Sports Pool</h5>
                            <p class="card-text">Game predictions, player statistics, sports analysis</p>
                            <div class="mb-2">
                                <strong>AI Model:</strong> GPT-4o<br>
                                <strong>Status:</strong> <span class="pool-status status-ready">Ready</span>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="col-md-6 col-lg-4 mb-4">
                    <div class="card feature-card h-100">
                        <div class="card-body text-center">
                            <div class="agent-icon">💼</div>
                            <h5 class="card-title">Business Pool</h5>
                            <p class="card-text">Process automation, strategy consulting, workflow optimization</p>
                            <div class="mb-2">
                                <strong>AI Model:</strong> Claude Sonnet<br>
                                <strong>Status:</strong> <span class="pool-status status-ready">Ready</span>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="col-md-6 col-lg-4 mb-4">
                    <div class="card feature-card h-100">
                        <div class="card-body text-center">
                            <div class="agent-icon">📚</div>
                            <h5 class="card-title">General Pool</h5>
                            <p class="card-text">Comprehensive assistance across all topics and domains</p>
                            <div class="mb-2">
                                <strong>AI Model:</strong> GPT-4o<br>
                                <strong>Status:</strong> <span class="pool-status status-ready">Ready</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Features Section -->
            <div class="row mb-5">
                <div class="col-12">
                    <h2 class="text-center mb-4">⭐ Key Features</h2>
                    <div class="row">
                        <div class="col-md-6 mb-3">
                            <div class="card">
                                <div class="card-body">
                                    <h5 class="card-title">🗣️ Natural Language Interface</h5>
                                    <p class="card-text">Talk to the system in plain English through Replit Agent</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-6 mb-3">
                            <div class="card">
                                <div class="card-body">
                                    <h5 class="card-title">🎯 Smart Agent Routing</h5>
                                    <p class="card-text">Automatic selection of specialized AI pools based on task type</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-6 mb-3">
                            <div class="card">
                                <div class="card-body">
                                    <h5 class="card-title">🔄 Auto-scaling</h5>
                                    <p class="card-text">Dynamic pool management based on demand and workload</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-6 mb-3">
                            <div class="card">
                                <div class="card-body">
                                    <h5 class="card-title">📊 Real-time Monitoring</h5>
                                    <p class="card-text">System health and performance tracking with alerts</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Architecture Section -->
            <div class="row">
                <div class="col-12">
                    <div class="card">
                        <div class="card-body">
                            <h2 class="card-title text-center mb-4">🎯 System Architecture</h2>
                            <div class="row text-center">
                                <div class="col-md-3 mb-3">
                                    <h5>📱 Frontend</h5>
                                    <p>Replit Agent<br>Conversational UI</p>
                                </div>
                                <div class="col-md-3 mb-3">
                                    <h5>⚙️ Backend</h5>
                                    <p>Flask REST API<br>Headless Service</p>
                                </div>
                                <div class="col-md-3 mb-3">
                                    <h5>🗄️ Database</h5>
                                    <p>PostgreSQL<br>Production Ready</p>
                                </div>
                                <div class="col-md-3 mb-3">
                                    <h5>🤖 AI Providers</h5>
                                    <p>OpenAI GPT-4o<br>Anthropic Claude</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Footer -->
        <footer class="bg-dark py-4 mt-5">
            <div class="container text-center">
                <p class="mb-0">🚀 OperatorOS - Enterprise AI Agent Orchestration Platform</p>
                <small class="text-muted">Powered by Replit Agent Interface</small>
            </div>
        </footer>

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    '''

@app.route('/health')
def health():
    """Health check endpoint"""
    return {"status": "healthy", "message": "OperatorOS is operational"}

if __name__ == "__main__":
    # Run the headless Flask API backend
    app.run(host="0.0.0.0", port=8000, debug=True)

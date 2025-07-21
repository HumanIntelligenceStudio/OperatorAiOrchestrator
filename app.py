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

# Import and register API routes
from api_routes import api_bp
app.register_blueprint(api_bp, url_prefix='/api')

with app.app_context():
    # Import models to ensure tables are created
    import models
    db.create_all()
    logging.info("✅ Database initialized successfully")

if __name__ == "__main__":
    # Run the headless Flask API backend
    app.run(host="0.0.0.0", port=8000, debug=True)

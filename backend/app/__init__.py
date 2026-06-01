"""Flask Application Factory"""

import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import config

db = SQLAlchemy()
jwt = JWTManager()

def create_app(config_class):
    """Create and configure Flask application"""
    
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    CORS(app, resources={r"/api/*": {"origins": app.config['CORS_ORIGINS']}})
    
    # Create uploads directory
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs('logs', exist_ok=True)
    
    # Setup logging
    setup_logging(app)
    
    # Register blueprints
    register_blueprints(app)
    
    # Register error handlers
    register_error_handlers(app)
    
    # Database context
    with app.app_context():
        db.create_all()
    
    return app


def register_blueprints(app):
    """Register Flask blueprints"""
    from app.routes import auth_routes, patient_routes, doctor_routes, appointment_routes, ai_routes, admin_routes
    
    app.register_blueprint(auth_routes.bp)
    app.register_blueprint(patient_routes.bp)
    app.register_blueprint(doctor_routes.bp)
    app.register_blueprint(appointment_routes.bp)
    app.register_blueprint(ai_routes.bp)
    app.register_blueprint(admin_routes.bp)


def register_error_handlers(app):
    """Register error handlers"""
    
    @app.errorhandler(400)
    def bad_request(error):
        return {'error': 'Bad request', 'message': str(error)}, 400
    
    @app.errorhandler(401)
    def unauthorized(error):
        return {'error': 'Unauthorized', 'message': 'Invalid credentials'}, 401
    
    @app.errorhandler(403)
    def forbidden(error):
        return {'error': 'Forbidden', 'message': 'Access denied'}, 403
    
    @app.errorhandler(404)
    def not_found(error):
        return {'error': 'Not found', 'message': 'Resource not found'}, 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return {'error': 'Internal server error', 'message': 'An unexpected error occurred'}, 500


def setup_logging(app):
    """Setup application logging"""
    
    log_level = getattr(logging, app.config['LOG_LEVEL'].upper())
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    
    # File handler
    file_handler = logging.FileHandler(app.config['LOG_FILE'])
    file_handler.setLevel(log_level)
    
    # Formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    
    # Add handlers
    app.logger.addHandler(console_handler)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(log_level)

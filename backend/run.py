#!/usr/bin/env python
"""Application entry point"""

import os
import logging
from app import create_app, db
from config import config

# Get configuration
config_name = os.getenv('FLASK_ENV', 'development')
app = create_app(config[config_name])

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    with app.app_context():
        # Create tables if they don't exist
        db.create_all()
        logger.info('Database tables created')
    
    # Run application
    host = os.getenv('API_HOST', '0.0.0.0')
    port = int(os.getenv('API_PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', True)
    
    logger.info(f'Starting CuraAI API on {host}:{port}')
    app.run(host=host, port=port, debug=debug)

from flask import Flask
from config import Config
from app.utils.logger import setup_logger

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Set up logging
    setup_logger(app)
    
    # Register blueprints
    from app.routes import main
    app.register_blueprint(main.bp)
    
    # Initialize extensions
    with app.app_context():
        app.logger.info('Initializing application...')
        
    return app 
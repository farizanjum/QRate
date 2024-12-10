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
    
    @app.route('/health')
    def health_check():
        return {'status': 'healthy'}, 200
    
    return app

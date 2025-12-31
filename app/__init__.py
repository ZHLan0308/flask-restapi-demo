from flask import Flask
from .routes import api_bp
from .errors import register_error_handlers

def create_app() -> Flask:
    app = Flask(__name__)

    # Register API blueprint
    app.register_blueprint(api_bp, url_prefix="/api")

    # Register centralized error handlers
    register_error_handlers(app)

    return app
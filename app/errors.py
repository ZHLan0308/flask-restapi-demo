from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException
from .utils import fail

def register_error_handlers(app: Flask) -> None:
    """
    Centralized error handling to keep response formats consistent.
    """

    @app.errorhandler(HTTPException)
    def handle_http_exception(e: HTTPException):
        payload, code = fail(
            message=e.description or "HTTP error",
            status_code=e.code or 400,
            errors={"name": e.name},
        )
        return jsonify(payload), code

    @app.errorhandler(Exception)
    def handle_unexpected_exception(e: Exception):
        # In production, you'd log the traceback.
        payload, code = fail(
            message="Internal Server Error",
            status_code=500,
            errors={"type": type(e).__name__},
        )
        return jsonify(payload), code
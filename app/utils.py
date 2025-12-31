from typing import Any

def ok(data: Any = None, message: str = "OK", status_code: int = 200):
    """
    Consistent success response wrapper.
    """
    return {
        "success": True,
        "message": message,
        "data": data,
    }, status_code

def fail(message: str, status_code: int = 400, errors: Any = None):
    """
    Consistent error response wrapper.
    """
    return {
        "success": False,
        "message": message,
        "errors": errors,
    }, status_code
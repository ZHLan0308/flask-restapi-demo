from flask import Blueprint, request, jsonify
from werkzeug.exceptions import BadRequest, NotFound
from .utils import ok, fail

api_bp = Blueprint("api", __name__)

# Simple in-memory store for demo purposes
_USERS: dict[int, dict] = {}
_NEXT_ID = 1

@api_bp.get("/health")
def health():
    payload, code = ok({"status": "up"}, "Service is healthy")
    return jsonify(payload), code

@api_bp.post("/users")
def create_user():
    global _NEXT_ID

    if not request.is_json:
        raise BadRequest("Request body must be JSON.")

    body = request.get_json(silent=True)
    if body is None:
        raise BadRequest("Invalid JSON body.")

    username = body.get("username")

    if not username or not isinstance(username, str):
        resp, code = fail(
            message="Validation error",
            status_code=422,
            errors={"username": "username is required and must be a string"},
        )
        return jsonify(resp), code

    user_id = _NEXT_ID
    _NEXT_ID += 1

    user = {"id": user_id, "username": username}
    _USERS[user_id] = user

    resp, code = ok(user, "User created", 201)
    return jsonify(resp), code

@api_bp.get("/users/<int:user_id>")
def get_user(user_id: int):
    user = _USERS.get(user_id)
    if user is None:
        raise NotFound("User not found.")
    resp, code = ok(user, "User fetched")
    return jsonify(resp), code

@api_bp.get("/users")
def list_users():
    resp, code = ok({"items": list(_USERS.values())}, "Users listed")
    return jsonify(resp), code
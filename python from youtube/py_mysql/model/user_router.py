from flask import Blueprint
from .user_controller import user_bp

user_router = Blueprint('user_router', __name__)
user_router.register_blueprint(user_bp)

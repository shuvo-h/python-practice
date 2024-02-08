from flask import Blueprint, request, jsonify
from app_name_one.user_module.user_controller import create_user

user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/user', methods=['POST'])
def create_user_route():
    data = request.get_json()
    result, status_code = create_user(data)
    return jsonify(result), status_code

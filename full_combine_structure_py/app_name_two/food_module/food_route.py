from flask import Blueprint, request, jsonify
# from app_name_one.user_module.user_controller import create_user
from app_name_two.food_module.food_controller import create_food

food_bp = Blueprint('food_bp', __name__)


@food_bp.route('/food', methods=['POST'])
def create_food_route():
    data = request.get_json()
    result, status_code = create_food(data)
    return jsonify(result), status_code

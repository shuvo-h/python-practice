# from app_name_one.user_module.user_service import create_new_user
from app_name_two.food_module.food_service import create_new_food
from app_name_two.food_module.food_validation import validate_food_data

def create_food(data):
    errors = validate_food_data(data)
    if errors:
        return {'error': errors}, 400

    food = create_new_food(data)
    return {'food': food}, 201

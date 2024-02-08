from app_name_one.user_module.user_service import create_new_user
from app_name_one.user_module.user_validation import validate_user_data

def create_user(data):
    errors = validate_user_data(data)
    if errors:
        return {'error': errors}, 400

    user = create_new_user(data)
    return {'user': user}, 201

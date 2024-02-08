def validate_food_data(data):
    errors = []
    if 'food_type' not in data:
        errors.append('food_type is required')
    if 'food_name' not in data:
        errors.append('food_name is required')
    return errors


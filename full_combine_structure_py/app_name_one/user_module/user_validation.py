def validate_user_data(data):
    errors = []
    if 'email' not in data:
        errors.append('Email is required')
    if 'name' not in data:
        errors.append('Name is required')
    return errors


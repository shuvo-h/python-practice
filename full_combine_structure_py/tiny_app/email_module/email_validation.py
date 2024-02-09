def validate_email_body(data):
    errors = []
    if 'email' not in data:
        errors.append('Email is required')
    if 'name' not in data:
        errors.append('Name is required')
    return errors


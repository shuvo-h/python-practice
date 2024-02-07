from flask import request, jsonify
from .user_utils import send_response

def validate_user_creation_request():
    data = request.get_json()

    # username and email is required
    if not data or not 'username' in data or 'email' not in data:
        return send_response(False, 400, None,'email and username is required!!')
    
    # check if valid email
    email = data['email']
    if not validateEmail(email):
        return send_response(False, 400, None,'email must be valid!!')
     # If all checks pass, allow the request to continue
    return None


def validateEmail(email):
    return '@' in email


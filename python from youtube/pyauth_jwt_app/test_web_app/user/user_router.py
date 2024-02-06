from flask import Blueprint, request, jsonify
from .user_controller import create_user_controller
# from .middleware import authentication_check, validation
from .user_utils import send_response, handle_exception_wrapper
from .user_validation import validate_user_creation_request


user_bp = Blueprint('user', __name__)

@user_bp.route('/user/create', methods=['POST'])
# @authentication_check
# @validation
@handle_exception_wrapper
def create_user_route():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')

    # validate data first
    validate_res = validate_user_creation_request()
    if validate_res:
        return validate_res

    # return json response
    userResult = create_user_controller(username, email)
    return send_response(userResult['isSuccess'], userResult['http_status'], userResult.get('data'),userResult['message'])

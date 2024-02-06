from flask import jsonify
# try-except-finally wrapper
def handle_exception_wrapper(func):
    # @wraps(func)
    def decorated_function(*args,**kwargs):
        try:
            # Call the wrapped function and return its result
            return func(*args,**kwargs)
        except Exception as e:
            # Handle exceptions and return an error response
            error_message = str(e) if str(e) else 'Internal Server Error'
            return send_response(False,500,None,error_message)
        finally:
            # Optionally perform any cleanup actions
            pass
    return decorated_function


# send structured response always
def send_response(isSuccess,http_status,data,message):
    """
    Construct a dictionary to send json response
    :message = string
    :http_status = number
    :data = any
    """
    response = {
        'isSuccess': isSuccess,
        'message': message,
        'data': data
    }
    return jsonify(response), http_status
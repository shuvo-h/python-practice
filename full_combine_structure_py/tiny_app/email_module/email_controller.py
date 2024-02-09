# from .email_validation import validate_email_body
from tiny_app.email_module.email_validation import validate_email_body
from tiny_app.email_module.email_service import sendSMTPemail

def send_email(data):
    errors = validate_email_body(data)
    if errors:
        return {'error': errors}, 400
    result = sendSMTPemail(data)
    return {'result':result}, 201
from flask import Blueprint

send_email_bp = Blueprint('blueprint1', __name__, template_folder='templates', static_folder='static')
# send_email_bp = Blueprint('send_email',__name__)

# import all the routes here will be starts with prefix "/emails"
from .email_module import send_email_route
from .sqlite_learn_module import sqlite_route

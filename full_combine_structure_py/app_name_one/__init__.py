from flask import Flask
from app_name_one.user_module.user_route import user_bp

# create the app for this application "app_name_one"
# @optional if use combined app, use blueprint_registerer.py to register
def create_app_name_one_app():
    app = Flask(__name__)

    # register blueprints here
    app.register_blueprint(user_bp,url_prefix='/api/v1/users')


    return app
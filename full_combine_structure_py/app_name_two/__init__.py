from flask import Flask
from app_name_two.food_module.food_route import food_bp

# create the app for this application "app_name_two"
# @optional if use combined app, use blueprint_registerer.py to register
def create_app_name_two_app():
    app = Flask(__name__)

    # register blueprints here
    app.register_blueprint(food_bp,url_prefix='/api/v1/foods')


    return app


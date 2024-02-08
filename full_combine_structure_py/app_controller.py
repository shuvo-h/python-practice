from flask import Flask
from app_name_two.blueprint_registerer import register_all_food_bluprint

# create a combined single app and call all blueprints here to register
def create_combined_app():
    app = Flask(__name__)

    # register all blueprints here
    # app.register_blueprint(food_bp,url_prefix='/api/v1/foods')
    register_all_food_bluprint(app)


    return app


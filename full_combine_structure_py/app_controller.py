from flask import Flask,jsonify
from config.database import db_connect
from app_name_one.blueprint_registerer import register_all_users_bluprint
from app_name_two.blueprint_registerer import register_all_food_bluprint
from tiny_app.blueprint_registerer import register_tinyapp_blueprints

# create a combined single app and call all blueprints here to register
def create_combined_app():
    app = Flask(__name__)

    # configure app to add all secret from env
    # call config method and pass the app there
    db_connect(app)
    
    # register all blueprints here
    # app.register_blueprint(food_bp,url_prefix='/api/v1/foods')
    register_all_users_bluprint(app)
    register_all_food_bluprint(app)
    register_tinyapp_blueprints(app)

    # handle custom error page
    # handle invalid url
    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify({'success':False,"message":"URL not found:("}),404
    # Internal server error handler 
    @app.errorhandler(500)
    def internal_server_error(e):
        return jsonify({'success':False,"message":"Internal server error"}),500


    return app


# create a method to run the app
from flask import Flask

# method to run the app 
def create_test_web_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']='your_secret_key'

    # import all the blueprint modules
    from .auth import authBP
    from .user import user_bp


    # register all the blueprints
    # app.register_blueprint(authBP,url_prefix='/')
    app.register_blueprint(user_bp,url_prefix='/users')


    # import database models so that it can be accessed from whole app


    return app

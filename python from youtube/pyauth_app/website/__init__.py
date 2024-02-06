from flask import Flask,current_app
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# database configure 
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']='your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    
    # import all the blueprint here to connect with app
    from .views import views_bp
    from .auth import auth_bp

    # register all the blueprint here
    app.register_blueprint(views_bp,url_prefix='/')
    app.register_blueprint(auth_bp,url_prefix='/auth')

    # import database models so that it can be accessed from whole app 
    from .models import User, Note
    create_database(app)

    # combine with flask login manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    return app

def create_database(app):
    if not path.exists('/website' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')
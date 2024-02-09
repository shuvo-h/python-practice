from os import path
import os
from flask_sqlalchemy import SQLAlchemy
from .env import envList

db = SQLAlchemy()


def db_connect(app):
    DB_NAME = envList['DB_NAME']
    # config database options
    app.config['SECRET_KEY']= envList['APP_SECRET_KEY']
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # connect the database with app
    db.init_app(app)

    # import or initialize all database models ot tables
    # from .models import User, Note

    create_database(app,DB_NAME)

def create_database(app,DB_NAME):
    INSTANCE_DIR = "instance"
    db_path = os.path.join(os.path.dirname(__file__), '..', INSTANCE_DIR, DB_NAME)  # ".." means move up 2 level to find the DB_NAME file
    if not os.path.exists(db_path):
        with app.app_context():
            db.create_all()
            print('Created Database!')
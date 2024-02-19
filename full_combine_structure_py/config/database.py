from os import path
import os
from flask_sqlalchemy import SQLAlchemy
from .env import envList

db = SQLAlchemy()


def db_connect(app):
    # db name and absolute path of database 
    DB_NAME = envList['DB_NAME']
    base_dir = os.getcwd()
    INSTANCE_DIR = "db_instance"
    db_path = os.path.join(base_dir,INSTANCE_DIR,f"{DB_NAME}.db")

    # config database options
    app.config['SECRET_KEY']= envList['APP_SECRET_KEY']
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # connect the database with app
    db.init_app(app)

    # import or initialize all database models ot tables
    # from .models import User, Note

    create_database(app,db_path)

def create_database(app,db_path):
    # Ensure the directory for the database file exists
    db_dir = os.path.dirname(db_path)
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)

    # Create the database if it doesn't exist
    if not os.path.exists(db_path):
        with app.app_context():
            db.create_all()
            print('Created Database!')
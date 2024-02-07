from flask import Flask
from extensions import db
from auth import auth_bp

def create_app():
    # create app, configure from .env file
    app = Flask(__name__)
    app.config.from_prefixed_env() # define in .env FLASK_APP,FLASK_RUN_PORT,FLASK_SECRET_KEY,FLASK_DEBUG

    # connect with DB
    db.init_app(app)

    # register bluprints
    app.register_blueprint(auth_bp,url_prefix="/auth")

     # Create tables if they don't exist
    with app.app_context():
        db.create_all()

    return app


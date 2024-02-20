import os
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
from dotenv import load_dotenv
load_dotenv()
from flask import Flask
from dbConfig import mysql
# from .user_router import user_router
from model.user_router import user_router





def create_app():
    app = Flask(__name__)

    # MySQL configurations
    app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
    app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
    app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
    app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
    
    mysql.init_app(app)

    # blueprints register 
    app.register_blueprint(user_router, url_prefix='/api/v1')
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
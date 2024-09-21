# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config_Env:
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = os.getenv('DEBUG', 'False') == 'True'  # Convert to boolean
    DATABASE_URL = os.getenv('DATABASE_URL')
    # Collect allowed hosts into a list
    ALLOWED_HOSTS = [
        os.getenv('ALLOWED_HOST_1', 'localhost'),
        os.getenv('ALLOWED_HOST_2', '127.0.0.1'),
        # Add more hosts as needed...........
    ]
    DB_INFO = {
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT', '5432'),  # Default to 5432 if not set
    }

    # Add any other variables you need

# Example usage:
# print("SECRET_KEY = ",Config_Env.DB_INFO)

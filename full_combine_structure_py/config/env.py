from os import getenv
envList = {
    'APP_SECRET_KEY': getenv('APP_SECRET_KEY','default_secret_key'),
    'DB_NAME': getenv('DB_NAME','default_db_name'),
    
}
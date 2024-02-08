import threading
import os
from dotenv import load_dotenv
from app_name_one import create_app_name_one_app
from app_name_two import create_app_name_two_app
from app_controller import create_combined_app

# Load environment variables from .env file
load_dotenv()

combined_app = create_combined_app()
# app_one = create_app_name_one_app()
# app_two = create_app_name_two_app()

if __name__ == '__main__':
    # Get port numbers from environment variables or use defaults
    # this port only works for command "python main.py", for command use "FLASK_RUN_PORT" in .env
    port_one = int(os.getenv('PORT_ONE', 4000))
    # port_two = int(os.getenv('PORT_TWO', 4001))
    print(port_one)

    # run only one app at a time, not two
    combined_app.run()
    # app_one.run(port=port_one)
    # app_two.run(port=port_two)

    
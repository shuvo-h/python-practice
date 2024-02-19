import os
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
from dotenv import load_dotenv
load_dotenv()
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/v1/home",)
def home():
    return jsonify({'message':"Ok Py"})

from controller import *
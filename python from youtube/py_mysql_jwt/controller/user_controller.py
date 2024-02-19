from flask import jsonify
from main import app
from model.user_model import user_model

@app.route("/user/signup",)
def user_signup_controller():
    result = user_model.user_signup_model({})
    return jsonify({'message':"Ok Py s","result":result})
from flask import Blueprint

authBP = Blueprint('auth',__name__)

@authBP.route('/ab',methods=['GET'])
def login():
    return '<h1>Login Route hit</h1>'
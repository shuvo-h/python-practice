from flask import Blueprint, request,jsonify
from models import User
from flask_jwt_extended import jwt_required,get_jwt
from schemas import UserSchema
from math import ceil

user_bp = Blueprint('users',__name__)

@user_bp.get('/all')
@jwt_required()         # middleware to check authentication jwt token is in header
def get_all_users():
    claims = get_jwt()
    # only staff can acces this route
    if claims.get('is_staff') == True:  # attached this property with jwt in main.py file
        page = request.args.get('page',default=1, type=int)
        per_page = request.args.get('per_page',default=10, type=int)

        users = User.query.paginate(page=page,per_page=per_page)

        result = UserSchema().dump(users,many=True)

        return jsonify({
            'users': result,
            'meta':{
                'page': page,
                'per_page': per_page
            }
        }), 200
    return jsonify({
        'message': 'you are not permitted'
    }), 401
    

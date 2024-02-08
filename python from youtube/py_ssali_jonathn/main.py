from flask import Flask,jsonify
from extensions import db, jwt
from auth import auth_bp
from users import user_bp
from models import User, TokenBlocklist

def create_app():
    # create app, configure from .env file
    app = Flask(__name__)
    app.config.from_prefixed_env() # define in .env FLASK_APP,FLASK_RUN_PORT,FLASK_SECRET_KEY,FLASK_DEBUG

    # connect with DB
    db.init_app(app)

    # external configure
    jwt.init_app(app)

    # move this part to a separate file to register with app. pass the app as argument
    # register bluprints
    app.register_blueprint(auth_bp,url_prefix="/auth")
    app.register_blueprint(user_bp,url_prefix="/users")

    # load jwt user
    @jwt.user_lookup_loader
    def user_lookup_callback(__jwt_headers,jwt_data):
        identity = jwt_data['sub']
        return User.query.filter_by(username=identity).one_or_none()

    # jwt additional claims: attach information with jwt token
    @jwt.additional_claims_loader
    def make_additional_claims(identity):
        if identity == 'arzel':
            return {'is_staff':True}
        else:
            return {'is_staff':True}

    # jwt error handler
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header,jwt_data):
        return jsonify({
            'message':'Token has expired', 
            "error":"token_expired"
        }), 401
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return jsonify({
            'message':'Signature verification failed', 
            "error":"invalid_token"
        }), 401
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return jsonify({
            'message':'Missing valid token', 
            "error":"authorization_header"
        }), 401
    
    # check if token is blocked
    @jwt.token_in_blocklist_loader
    def token_in_blocklist_callback(jwt_header,jwt_data):
        jti = jwt_data['jti']
        token = db.session.query(TokenBlocklist).filter(TokenBlocklist.jti == jti).scalar()

        return token is not None

    # Create tables if they don't exist
    with app.app_context():
        db.create_all()

    return app


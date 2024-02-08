from app_name_one.user_module.user_route import user_bp

def register_all_users_bluprint(app):
    app.register_blueprint(user_bp,url_prefix='/api/v1/users')
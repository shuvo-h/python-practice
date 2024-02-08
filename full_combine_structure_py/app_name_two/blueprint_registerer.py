from app_name_one.user_module.user_route import user_bp
from app_name_two.food_module.food_route import food_bp

def register_all_food_bluprint(app):
    app.register_blueprint(food_bp,url_prefix='/api/v1/foods')
    app.register_blueprint(user_bp,url_prefix='/api/v1/users')
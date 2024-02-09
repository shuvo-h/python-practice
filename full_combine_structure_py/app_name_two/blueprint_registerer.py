from app_name_two.food_module.food_route import food_bp


def register_all_food_bluprint(app):
    app.register_blueprint(food_bp,url_prefix='/api/v1/foods')


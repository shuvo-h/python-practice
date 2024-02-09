# from tiny_app.v1.email_module import send_email_bp as send_email_bp_v1
# from tiny_app.email_module.send_email_route import send_email_bp
from tiny_app import send_email_bp


blueprintList = [
    {
        "path":"/api/v1/emails",
        "bluePrint": send_email_bp
    },
]

    # loop blueprintList and register with app
def register_tinyapp_blueprints(app):
    for blueprint_info in blueprintList:
        bluePrintInstance = blueprint_info['bluePrint']
        path = blueprint_info['path']
        app.register_blueprint(bluePrintInstance,url_prefix=path)

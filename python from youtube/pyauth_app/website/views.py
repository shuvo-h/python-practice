from flask import Blueprint,render_template
from flask_login import  login_required,current_user

views_bp = Blueprint('views',__name__)

@views_bp.route("/")
@login_required
def home():
    return render_template("home.html",user=current_user)
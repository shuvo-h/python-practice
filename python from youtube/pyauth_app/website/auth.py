from flask import Blueprint,render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from flask_login import login_user, login_required,logout_user,current_user

auth_bp = Blueprint('auth',__name__)

@auth_bp.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        print(user)
        if user:
            if check_password_hash(user.password,password):
                flash('Loggedin successfully!',category='success')
                login_user(user,remember=True) # keep track the loogin user
                return redirect(url_for('views.home'))
            else:
                flash('Failed to Loggedin!',category='error')
        else:
            flash('Email Not exist!',category='error')

    return render_template('login.html',user=current_user)




@auth_bp.route('/logout')
@login_required #must need login
def logout():
    logout_user()
    return redirect(url_for('auth.login'))




@auth_bp.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # validate data 
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exist', category='error')
        elif len(email) < 4:
            flash('Email bust be more than 4 characters', category='error')
        elif len(firstName) < 2:
            flash('First name bust be more than 2 characters', category='error')
           
        elif password1 != password2:
            flash('password must be match with confirm password', category='error')
            
        elif len(password1) < 1:
            flash('Password must be more than 7 characters', category='error')
            
        else:
            # add data to database
            hashed_password = generate_password_hash(password1, method='pbkdf2:sha256')
            newUser = User(email=email,first_name=firstName,password=hashed_password)
            db.session.add(newUser)
            db.session.commit()
            login_user(newUser,remember=True) # keep track the loogin user
            flash('Account created successfully', category='success')
            return redirect(url_for('views.home'))
    return render_template('signup.html',user=current_user)
from app.models.User import User
from app import db, bycrypt, app
from flask_login import LoginManager, login_manager, login_user, logout_user, current_user
from flask import render_template, request, flash, redirect, url_for, session

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth_router.login'
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class AuthController():
    def __init__(self):
        pass

    def signup(self):
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            username = request.form['username']
            password = bycrypt.generate_password_hash(request.form['password'])
            picture_profile = 'user.png'

            user = User(name=name, email=email, username=username, password=password, picture_profile=picture_profile)
            db.session.add(user)
            db.session.commit()
            flash('Usuario registrado exitosamente')
            return render_template('auth/login.html')
        return render_template('auth/signup.html')

    def login(self):
        if request.method == 'POST':
            user = User.query.filter_by(username=request.form['username']).first()
            if user:
                if bycrypt.check_password_hash(user.password, request.form['password']):
                    login_user(user)
                    return redirect(url_for('main_router.main'))
            
            flash('Usuario no existe, o los creadenciales no son válidos')
            return redirect(url_for('auth_router.login'))
        return render_template('auth/login.html')
    def logout(self):
        session.clear()
        logout_user()
        return redirect(url_for('auth_router.login'))

authcontroller = AuthController()
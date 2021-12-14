from os import name
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
            useranme = request.form['useranme']
            direccion = request.form['direccion']
            email = request.form['email']           
            password = bycrypt.generate_password_hash(request.form['password'])
            phone = request.form['phone']
            #picture_profile = 'user.png'
            #user = User(name=name,username=username,direccion=direccion, email=email, password=password, picture_profile=picture_profile)
            user = User(name=name,useranme=useranme,direccion=direccion, email=email, password=password, phone=phone,rol_user='cliente')
            db.session.add(user)
            db.session.commit()
            flash('Usuario registrado exitosamente')
            return render_template('auth/login.html')
        return render_template('auth/signup.html')

    def login(self):
        if request.method == 'POST':
            #user = User.query.filter_by(name=request.form['name']).first()
            user = User.query.filter_by(name=request.form['name']).first()
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
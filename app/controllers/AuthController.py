from os import name
from app.models.Usuario import Usuario
from app import db, bycrypt, app
from flask_login import LoginManager, login_manager, login_user, logout_user, current_user
from flask import render_template, request, flash, redirect, url_for, session

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth_router.login'
@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

class AuthController():
    def __init__(self):
        pass

    def signup(self):
        if request.method == 'POST':
            nombre = request.form['nombre']
            usuario = request.form['usuario']
            direccion = 'Sin direccion'
            email = request.form['email']           
            clave = bycrypt.generate_password_hash(request.form['password'])
            telefono = 'sin telefono'
            rol_usuario = 'cliente'
            foto_perfil = 'user.png'
        
            user = Usuario(nombre=nombre,usuario=usuario,direccion=direccion, email=email, clave=clave, telefono=telefono,rol_usuario=rol_usuario, foto_perfil=foto_perfil)
            db.session.add(user)
            db.session.commit()
            flash('Usuario registrado exitosamente')
            return render_template('auth/login.html')
        return render_template('auth/signup.html')

    def login(self):
        if request.method == 'POST':
            #user = User.query.filter_by(nombre=request.form['nombre']).first()
            user = Usuario.query.filter_by(usuario=request.form['usuario']).first()
            if user: 
                if bycrypt.check_password_hash(user.clave, request.form['password']):
                    login_user(user)
                    if user.rol_usuario == 'cliente':
                        return redirect(url_for('client_router.index'))
                    else:
                        return redirect(url_for('main_router.main'))
                    
            flash('Usuario no existe, o los creadenciales no son válidos')
            return redirect(url_for('auth_router.login'))
        return render_template('auth/login.html')
    def logout(self):
        session.clear()
        logout_user()
        return redirect(url_for('auth_router.login'))

authcontroller = AuthController()
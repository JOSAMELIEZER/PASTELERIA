from app.models.Usuario import Usuario
from app import db
from flask import render_template
class UserController():
    def __init__(self):
        pass

    def index(self):
        # user = {'name': 'Josam Pinaya'}
        usuarios= Usuario.query.all()
        return render_template('usuario/index.html', usuarios=usuarios)
        """ from app.models.User import User
        users = User.query.all()
        return render_template('materias/index.html', users=users) """

usercontroller = UserController()
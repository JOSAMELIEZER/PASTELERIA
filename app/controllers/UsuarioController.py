from app.models.Usuario import Usuario
from app import db
from flask import render_template
class UsuarioController():
    def __init__(self):
        pass

    def index(self):
        # usuario = {'name': 'Josam Pinaya'}
        usuarios= Usuario.query.all()
        return render_template('usuario/index.html', usuarios=usuarios)
        """ from app.models.Usuario import Usuario
        usuarios = Usuario.query.all()
        return render_template('materias/index.html', usuarios=usuarios) """

usuariocontroller = UsuarioController()
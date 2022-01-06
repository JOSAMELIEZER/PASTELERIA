from flask import Blueprint
from app.controllers.UsuarioController import usuariocontroller

usuario_route = Blueprint('usuario_route', __name__)

@usuario_route.route('/usuario',methods=['GET'])
def index():
    return usuariocontroller.index()

@usuario_route.route('/usuario/<int:id>/eliminar',methods=['GET'])
def eliminar(id):
    return usuariocontroller.eliminar(id)

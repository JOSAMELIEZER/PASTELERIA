from flask import Blueprint
from flask_login import login_required
#llamar clase controlador del main
from app.controllers.MensajeController import mensajecontroller

#definir el nombre de ruta
mensaje_router = Blueprint('mensaje_router', __name__)

#devuelve un main controller con get
@mensaje_router.route('/mensaje',methods=['GET'])
@login_required
def index():
    return mensajecontroller.index()

@mensaje_router.route('/index2',methods=['GET'])
def index2():
    return mensajecontroller.index2()

@mensaje_router.route('/mensaje/store',methods=['POST'])
def store():
    return mensajecontroller.store()

@mensaje_router.route('/mensaje/<int:id>/delete',methods=['GET'])
@login_required
def delete(id):
    return mensajecontroller.delete(id)   
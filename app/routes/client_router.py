from flask import Blueprint
from app.controllers.ClientController import clientcontroller
from flask_login import login_required

client_router = Blueprint('client_router', __name__)

@client_router.route('/client',methods=['GET'])
@login_required
def index():
    return clientcontroller.index()

@client_router.route('/client/micarrito',methods=['GET','POST'])
@login_required
def carrito():
    return clientcontroller.carrito()

@client_router.route('/client/micarrito/quitar/<int:id>',methods=['GET'])
@login_required
def quitar(id):
    return clientcontroller.quitar(id)

@client_router.route('/client/micarrito/getcarrito/<int:id>',methods=['GET'])
@login_required
def obtenerCarrito(id):
    return clientcontroller.obtenerCarrito(id)

@client_router.route('/client/micarrito/agregarcantidad',methods=['POST'])
@login_required
def agregarCantidad():
    return clientcontroller.agregarCantidad()

@client_router.route('/client/micarrito/procesarpedido',methods=['GET'])
@login_required
def pocesarPedido():
    return clientcontroller.pocesarPedido()
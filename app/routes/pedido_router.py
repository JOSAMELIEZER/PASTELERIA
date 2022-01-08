from flask import Blueprint
from app.controllers.PedidoController import pedidocontroller
from flask_login import login_required

pedido_router = Blueprint('pedido_router', __name__)

@pedido_router.route('/pedido',methods=['GET'])
@login_required
def index():
    return pedidocontroller.index()

@pedido_router.route('/pedido/aceptar/<int:id>',methods=['GET'])
@login_required
def aceptar(id):
    return pedidocontroller.aceptar(id)

@pedido_router.route('/pedido/rechazar/<int:id>',methods=['GET'])
@login_required
def rechazar(id):
    return pedidocontroller.rechazar(id)

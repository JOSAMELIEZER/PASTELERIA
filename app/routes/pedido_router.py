from flask import Blueprint
from app.controllers.PedidoController import pedidocontroller

pedido_router = Blueprint('pedido_router', __name__)

@pedido_router.route('/pedido',methods=['GET'])
def index():
    return pedidocontroller.index1()


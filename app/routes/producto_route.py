from flask import Blueprint
from app.controllers.ProductoController import productocontroller

producto_route = Blueprint('producto_route', __name__)

@producto_route.route('/producto',methods=['GET'])
def index():
    return productocontroller.index1()

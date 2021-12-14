from flask import Blueprint
from app.controllers.ProductoController import productocontroller

producto_route = Blueprint('producto_route', __name__)

@producto_route.route('/producto',methods=['GET'])
def index():
    return productocontroller.index1()

@producto_route.route('/producto/create',methods=['GET'])
def create():
    return productocontroller.create()

@producto_route.route('/producto/store',methods=['POST'])
def store():
    return productocontroller.store()

@producto_route.route('/producto/<int:id>/delete',methods=['GET'])
def delete(id):
    return productocontroller.delete(id)

@producto_route.route('/producto/<int:id>/edit',methods=['GET'])
def edit(id):
    return productocontroller.edit(id)

@producto_route.route('/producto/<int:id>/update',methods=['POST'])
def update(id):
    return productocontroller.update(id)
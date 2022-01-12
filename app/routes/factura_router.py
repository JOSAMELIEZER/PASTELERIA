from flask import Blueprint
from app.controllers.FacturaController import facturacontroller
from flask_login import login_required

factura_router = Blueprint('factura_router', __name__)

@factura_router.route('/factura',methods=['GET'])
@login_required
def index():
    return facturacontroller.index()
@factura_router.route('/factura/crear/<int:id>',methods=['GET'])
@login_required
def nuevaFactura(id):
    return facturacontroller.nuevaFactura(id)

@factura_router.route('/factura/detalle/<int:id>',methods=['GET'])
@login_required
def detalleFactura(id):
    return facturacontroller.detalleFactura(id)
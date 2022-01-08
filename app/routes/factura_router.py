from flask import Blueprint
from app.controllers.FacturaController import facturacontroller
from flask_login import login_required

factura_router = Blueprint('factura_router', __name__)

@factura_router.route('/factura',methods=['GET'])
@login_required
def index():
    return facturacontroller.index()
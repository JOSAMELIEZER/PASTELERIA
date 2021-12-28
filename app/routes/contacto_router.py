from flask import Blueprint
from app.controllers.ContactoController import contactocontroller

contacto_router = Blueprint('contacto_router', __name__)

@contacto_router.route('/contacto',methods=['GET'])
def index():
    return contactocontroller.index()
@contacto_router.route('/contacto/store',methods=['POST'])
def store():
    return contactocontroller.store()
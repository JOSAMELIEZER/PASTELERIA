from flask import Blueprint
from app.controllers.ClientController import clientcontroller
from flask_login import login_required

client_router = Blueprint('client_router', __name__)

@client_router.route('/client',methods=['GET'])
@login_required
def index():
    return clientcontroller.index()

@client_router.route('/client/carrito',methods=['POST'])
@login_required
def carrito():
    return clientcontroller.carrito()
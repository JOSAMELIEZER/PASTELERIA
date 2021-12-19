from flask import Blueprint
from app.controllers.ClientController import clientcontroller

client_router = Blueprint('client_router', __name__)

@client_router.route('/client',methods=['GET'])
def index():
    return clientcontroller.index()
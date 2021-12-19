from flask import Blueprint
from app.controllers.UserController import usercontroller

usuario_route = Blueprint('usuario_route', __name__)

@usuario_route.route('/usuario',methods=['GET'])
def index():
    return usercontroller.index()
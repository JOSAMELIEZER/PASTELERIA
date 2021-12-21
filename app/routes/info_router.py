from flask import Blueprint
from app.controllers.InfoController import infocontroller

info_router = Blueprint('info_router', __name__)

@info_router.route('/info',methods=['GET'])
def index():
    return infocontroller.index()
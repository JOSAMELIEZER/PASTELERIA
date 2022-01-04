from flask import Blueprint

from flask_login import login_required
from app.controllers.EstadisticaController import estadisticacontroller

estadistica_router = Blueprint('contacto_router', __name__)

@estadistica_router.route('/index',methods=['GET'])
@login_required
def index():
    return estadisticacontroller.index()



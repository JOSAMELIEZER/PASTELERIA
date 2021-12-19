from flask import Blueprint
from app.controllers.PerfilController import perfilcontroller
from flask_login import login_required

perfil_router = Blueprint('perfil_router', __name__)

@login_required
@perfil_router.route('/perfil',methods=['GET'])
def index():
    return perfilcontroller.index()

@perfil_router.route('/perfil/<int:id>/edit',methods=['GET'])
def edit(id):
    return perfilcontroller.edit(id)

@login_required
@perfil_router.route('/perfil/<int:id>/updateprofile',methods=['POST'])
def updateprofile(id):
    return perfilcontroller.updateprofile(id)


from flask import Blueprint
from app.controllers.PerfilController import perfilcontroller
from flask_login import login_required

perfil_router = Blueprint('perfil_router', __name__)

@perfil_router.route('/perfil',methods=['GET'])
@login_required
def index():
    return perfilcontroller.index()

@perfil_router.route('/perfil/<int:id>/edit',methods=['GET'])
@login_required
def edit(id):
    return perfilcontroller.edit(id)

@perfil_router.route('/perfil/<int:id>/updateprofile',methods=['POST'])
@login_required
def updateprofile(id):
    return perfilcontroller.updateprofile(id)


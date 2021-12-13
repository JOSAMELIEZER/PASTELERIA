from flask import Blueprint
from app.controllers.AuthController import authcontroller

auth_router = Blueprint('auth_router', __name__)

@auth_router.route('/signup',methods=['GET','POST'])
def signup():
    return authcontroller.signup()

@auth_router.route('/login',methods=['GET','POST'])
def login():
    return authcontroller.login()

@auth_router.route('/logout',methods=['GET','POST'])
def logout():
    return authcontroller.logout()
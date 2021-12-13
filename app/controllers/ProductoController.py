#from app.models.User import User
from app import db
from flask import render_template
class ProductoController():
    def __init__(self):
        pass

    def index1(self):
        # user = {'name': 'Josam Pinaya'}
        #user= User.query.get(1)
        return render_template('producto/index.html')

productocontroller = ProductoController()
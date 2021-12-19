from app.models.Producto import Producto
from app import db
from flask import render_template
class ClientController():
    def __init__(self):
        pass

    def index(self):
        # user = {'name': 'Josam Pinaya'}
        prod= Producto.query.all()
        return render_template('clients/index.html', prod=prod)
        
clientcontroller = ClientController()

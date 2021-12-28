from app.models.Pedido import Pedido
from app.models.Producto import Producto
from flask_login import login_user, logout_user, current_user
from app import db
from flask import render_template, redirect, request, flash, url_for, jsonify

from app.models.Usuario import Usuario
class ClientController():
    def __init__(self):
        pass

    def index(self):
        # user = {'name': 'Josam Pinaya'}
        prod= Producto.query.all()
        return render_template('clients/index.html', prod=prod)
    def carrito(self):
        if request.method == 'POST':
            #si existe producto y usuario entonces: actualiar 
            # sino crear 
            id = request.form['id']
            pedido = Producto.query\
            .join(Pedido, Producto.id==Pedido.prod_id)\
            .join(Usuario, Pedido.user_id==Usuario.id)\
            .add_columns(Pedido.prod_id)\
            .filter(Pedido.prod_id == id)\
            .first()
            
            if pedido == "NULL":
                return jsonify(results=pedido)

            #Agregar pedido
            cantidad = 0
            estado = 2
            prod_id = id
            user_id = current_user.id
            est_pedido = Pedido(cantidad=cantidad, estado=estado, prod_id=prod_id, user_id=user_id)
            db.session.add(est_pedido)
            db.session.commit()
            return jsonify(results=user_id)
            
        
clientcontroller = ClientController()

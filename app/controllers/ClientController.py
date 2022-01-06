from app.models.Pedido import Pedido
from app.models.Producto import Producto
from flask_login import login_user, logout_user, current_user
from app import db
from flask import render_template, redirect, request, flash, url_for, jsonify
from sqlalchemy import or_

from app.models.Usuario import Usuario
class ClientController():
    def __init__(self):
        pass

    def index(self):
        # user = {'name': 'Josam Pinaya'}
        prod= Producto.query.all()
        return render_template('clients/index.html', prod=prod)
    def carrito(self):
        user_id = current_user.id
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
            cantidad = 1
            estado = 2
            prod_id = id
            
            est_pedido = Pedido(cantidad=cantidad, estado=estado, prod_id=prod_id, user_id=user_id)
            db.session.add(est_pedido)
            db.session.commit()
            return jsonify(results=user_id)

        carrito = Pedido.query\
            .join(Producto, Producto.id==Pedido.prod_id)\
            .join(Usuario, Pedido.user_id==Usuario.id)\
            .filter(or_(Pedido.estado == 2, Pedido.estado == 3))\
            .filter(Usuario.id == user_id)\
            .all()
            #.add_columns(Pedido.prod_id)\
        return render_template('clients/micarrito.html', carrito=carrito)
    def quitar(self, _id):
        pedido =  Pedido.query.get(_id)   
        db.session.delete(pedido)
        db.session.commit()
        flash('El producto quitado de carrito.')
        return redirect(url_for('client_router.index'))
    def obtenerCarrito(self, _id):
        pedido =  Pedido.query.get(_id)
        return str(pedido.cantidad)
    def agregarCantidad(self):
        if request.method == 'POST':
            id = request.form['id']
            cantidad = request.form['cantidad']

            pedido =  Pedido.query.get(id) 
            pedido.cantidad = cantidad
            db.session.commit()
            #flash('Cantidad agre.')
            return redirect(url_for('client_router.carrito'))
    def pocesarPedido(self):
        user_id = current_user.id
        pedido = Pedido.query\
            .join(Producto, Producto.id==Pedido.prod_id)\
            .join(Usuario, Pedido.user_id==Usuario.id)\
            .filter(Pedido.estado == 2)\
            .filter(Usuario.id == user_id)\
            .all()
        for row in pedido:
            row.estado = 3
            db.session.commit()
        flash('Su pedido se procesó con éxito.')
        return redirect(url_for('client_router.carrito'))
            
        
clientcontroller = ClientController()

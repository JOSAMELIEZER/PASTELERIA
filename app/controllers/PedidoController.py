from flask import render_template, url_for, request, redirect, flash
from app.models.Pedido import Pedido
from app.models.Producto import Producto
from app.models.Usuario import Usuario
from sqlalchemy import or_
from app import db


class PedidoController():
    def __init__(self):
        pass

    def index(self):
        #pedidos = Pedido.query.join(Usuario).filter_by(rol_usuario='cliente').all()
        pedidos = Pedido.query\
            .join(Producto, Producto.id==Pedido.prod_id)\
            .join(Usuario, Pedido.user_id==Usuario.id)\
            .filter(or_(Pedido.estado == 3, Pedido.estado == 4, Pedido.estado == 5))\
            .all()
        return render_template('pedido/index.html', pedidos=pedidos)
    def aceptar(self, _id):
        pedido =  Pedido.query.get(_id)
        pedido.estado = 4
        db.session.commit()
        return redirect(url_for('pedido_router.index'))
    def rechazar(self, _id):
        pedido =  Pedido.query.get(_id)
        pedido.estado = 5
        db.session.commit()
        return redirect(url_for('pedido_router.index'))
    
            
pedidocontroller = PedidoController()
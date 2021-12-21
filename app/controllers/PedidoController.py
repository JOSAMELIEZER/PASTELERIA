from flask import render_template, url_for, request, redirect, flash
from app.models.Pedido import Pedido
from app.models.Usuario import Usuario
from app import db


class PedidoController():
    def __init__(self):
        pass

    def index(self):
        pedidos = Pedido.query.join(Usuario).filter_by(rol_usuario='cliente').all()
        return render_template('pedido/index.html', pedidos=pedidos)
    
            
pedidocontroller = PedidoController()
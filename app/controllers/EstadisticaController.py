from flask import render_template, url_for, request, redirect, flash
from app.models.Usuario import Usuario
from app.models.Mensaje import Mensaje
from app.models.Producto import Producto
from app.models.Pedido import Pedido
from app import db

class EstadisticaController():
    def __init__(self):
        pass

    def index(self):
        cusuario = Usuario.query.count()
        cpedido = Pedido.query.count()
        cproducto = Producto.query.count()
        cmensaje = Mensaje.query.count()
        
        return render_template('index.html', cusuario=cusuario, cmensaje=cmensaje, cpedido=cpedido, cproducto=cproducto)


        
estadisticacontroller = EstadisticaController()
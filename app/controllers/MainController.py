from app.models.Usuario import Usuario
from app.models.Mensaje import Mensaje
from app.models.Producto import Producto
from app.models.Pedido import Pedido
from app import db
from flask import render_template
class MainController():
    def __init__(self):
        pass

    def index(self):
        cusuario = Usuario.query.count()
        cpedido = Pedido.query.count()
        cproducto = Producto.query.count()
        cmensaje = Mensaje.query.count()
        ctorta = Producto.query.filter(Producto.tipo=='torta').count()
        return render_template('index.html', cusuario=cusuario, cmensaje=cmensaje, cpedido=cpedido, cproducto=cproducto, ctorta=ctorta)
        
        #users = User.query.all()
        #return render_template('index.html', users=users)
        #return render_template('index.html')
maincontroller = MainController()

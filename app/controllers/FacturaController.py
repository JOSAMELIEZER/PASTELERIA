from flask import render_template, url_for, request, redirect, flash
from app.models.Factura import Factura
from app.models.Pedido import Pedido
from app.models.Producto import Producto
from app.models.Usuario import Usuario
from sqlalchemy import or_
from app import db


class FacturaController():
    def __init__(self):
        pass

    def index(self):
        #pedidos = Pedido.query.join(Usuario).filter_by(rol_usuario='cliente').all()
        facturas = Factura.query.all()
        return render_template('factura/index.html', facturas=facturas)

facturacontroller = FacturaController()
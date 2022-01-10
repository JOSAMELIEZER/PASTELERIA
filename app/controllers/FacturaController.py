from flask import render_template, url_for, request, redirect, flash
from app.models.Factura import Factura
from app.models.Pedido import Pedido
from app.models.Producto import Producto
from app.models.Usuario import Usuario
from app.models.DetalleFactura import DetalleFactura
from sqlalchemy import or_
from app import db
from datetime import datetime


class FacturaController():
    def __init__(self):
        pass

    def index(self):
        #pedidos = Pedido.query.join(Usuario).filter_by(rol_usuario='cliente').all()
        facturas = Factura.query.all()
        return render_template('factura/index.html', facturas=facturas)
    def nuevaFactura(self, _id):
        pedido = Pedido.query.get(_id)
        fecha = datetime.today().strftime('%Y-%m-%d')
        total = pedido.subtotal
        #registro en Factura
        factura = Factura(fecha=fecha, total=total)
        db.session.add(factura)
        db.session.commit()
        #Registro en detalle
        factura_id = db.session.query(db.func.max(Pedido.id)).scalar()
        pedido_id = pedido.id
        cantidad = 23
        det_factura = DetalleFactura(factura_id=factura_id,pedido_id=pedido_id, cantidad=cantidad)
        db.session.add(det_factura)
        db.session.commit()

        flash('Factura creada satisfactoriamente.')
        return redirect(url_for('factura_router.index'))

facturacontroller = FacturaController()
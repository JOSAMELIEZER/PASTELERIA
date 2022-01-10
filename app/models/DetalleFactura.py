from app import db
class DetalleFactura(db.Model):
    __tablename__ = 'detalle_factura'
    factura_id = db.Column(db.Integer, db.ForeignKey('facturas.id'), primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.id'), primary_key=True)
    cantidad = db.Column(db.Integer())
    #relationship
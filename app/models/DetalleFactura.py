""" from app import db
class DetalleFactura(db.Model):
    __tablename__ = 'detalle_factura'
    factura_id = db.Column(db.Integer, db.ForeignKey('facturas.id'), primary_key=True)
    prod_id = db.Column(db.Integer, db.ForeignKey('peoductos.id'), primary_key=True)
    Cantidad = db.Column(db.Integer()) """
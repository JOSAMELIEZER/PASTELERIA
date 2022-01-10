from app import db
#from app.models.DetalleFactura import DetalleFactura
#from app.models.pedido import Pedido

#DetallFact = db.Table('detalle_factura', db.metadata,
#    db.Column('pedido_id', db.Integer, db.ForeignKey('pedidos.id')),
#    db.Column('factura_id', db.Integer, db.ForeignKey('facturas.id'))
#  )

#detfac = db.Table('detfac', db.metadata,
 #   db.Column('fact_id',db.Integer, db.ForeignKey('factura.id')),
  #  db.Column('ped_id',db.Integer, db.ForeignKey('pedido.id')),
   # db.Column('user_id',db.Integer, db.ForeignKey('user.id')),
   # db.Column('prod_id',db.Integer, db.ForeignKey('producto.id')))

class Factura(db.Model):
    __tablename__="facturas"
    id=db.Column(db.Integer, primary_key= True, autoincrement=True)
    fecha = db.Column(db.Date)
    total = db.Column(db.Float)
    
    detalle = db.relationship(
        'DetalleFactura', backref='factura', lazy='dynamic')
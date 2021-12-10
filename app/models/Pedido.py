from app import db
#from app.models.DetalleFactura import DetalleFactura
from app.models.User import User
from app.models.Producto import Producto
from app.models.Factura import Factura

class Pedido(db.Model):
    __tablename__="pedido"
    id=db.Column(db.Integer, primary_key= True, autoincrement=True)
    cantidad = db.Column(db.Integer)
    #relationship
    user_id = db.Column(db.Integer, db.ForeignKey('users.id')) 
    user = db.relationship("users", back_populates="pedido")
    
    prod_id = db.Column(db.Integer, db.ForeignKey('producto.id'))
    producto = db.relationship("producto", back_populates="pedido")
    

    #relationship
    factura = db.relationship(
        "factura",
        back_populates="factura")

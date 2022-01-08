from app import db
#from app.models.DetalleFactura import DetalleFactura
from app.models.Usuario import Usuario
from app.models.Producto import Producto
from app.models.Factura import Factura

class Pedido(db.Model):
    __tablename__="pedidos"
    id=db.Column(db.Integer, primary_key= True, autoincrement=True)
    cantidad = db.Column(db.Float())
    #ESTADOS
    #Nada -> 0
    #Favoritos -> 1
    #Carrito -> 2
    #Pendiente -> 3
    #Aceptado -> 4
    #Rechazado -> 5
    estado = db.Column(db.Integer, default=0)
    subtotal = db.Column(db.Float())
    #relationship
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id')) 
    #user = db.relationship("Usuario", back_populates="pedidos")
    
    prod_id = db.Column(db.Integer, db.ForeignKey('productos.id'))
    #producto = db.relationship("productos", back_populates="pedidos")
    

    #relationship
    #factura = db.relationship("facturas",back_populates="facturas")

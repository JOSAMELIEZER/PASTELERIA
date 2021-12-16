from app import db

class Producto(db.Model):
    __tablename__="producto"
    id=db.Column(db.Integer, primary_key= True, autoincrement=True)
    nom_prod = db.Column(db.String(50))
    costo = db.Column(db.Float(50))
    det_prod = db.Column(db.String(150))
    picture_prod=db.Column(db.String(150),nullable=True)
    #relationship
    #pedido = db.relationship("pedido", back_populates="producto")
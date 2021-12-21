from app import db

class Producto(db.Model):
    __tablename__="productos"
    id=db.Column(db.Integer, primary_key= True, autoincrement=True)
    nom_prod = db.Column(db.String(50))
    precio = db.Column(db.Float(50))
    desc_prod = db.Column(db.String(150))
    picture_prod=db.Column(db.String(150),nullable=True)
    #relationship
    pedido = db.relationship(
        'Pedido', backref='producto', lazy='dynamic')
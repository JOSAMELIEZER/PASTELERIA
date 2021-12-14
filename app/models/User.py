#from os import name
from flask_login import UserMixin
from app import db
#from app.models.Pedido import Pedido

class User(db.Model, UserMixin):
    __tablename__="users"
    id=db.Column(db.Integer, primary_key= True, autoincrement=True)
    name = db.Column(db.String(50))
    useranme = db.Column(db.String(50))
    direccion = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(200))
    phone = db.Column(db.String(50))
    rol_user = db.Column(db.String(50))
     #relationship
    #pedido = db.relationship("pedido", back_populates="users")
    
#from os import name
from flask_login import UserMixin
from app import db
#from app.models.Pedido import Pedido

class Usuario(db.Model, UserMixin):
    __tablename__="usuarios"
    id=db.Column(db.Integer, primary_key= True, autoincrement=True)
    nombre = db.Column(db.String(50))
    usuario = db.Column(db.String(50))
    direccion = db.Column(db.String(50))
    email = db.Column(db.String(50))
    clave = db.Column(db.String(200))
    telefono = db.Column(db.String(50))
    rol_usuario = db.Column(db.String(50))
    foto_perfil=db.Column(db.String(150),nullable=True)
     #relationship
    #pedido = db.relationship("Pedido", back_populates="usuarios")
    
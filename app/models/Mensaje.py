#from os import name
from flask_login import UserMixin
from app import db
#from app.models.Pedido import Pedido

class Mensaje(db.Model, UserMixin):
    __tablename__="mensajes"
    id=db.Column(db.Integer, primary_key= True, autoincrement=True)
    nombre = db.Column(db.String(50))
    correo = db.Column(db.String(50))
    asunto = db.Column(db.String(50))
    mensaje = db.Column(db.String(350))
    
    
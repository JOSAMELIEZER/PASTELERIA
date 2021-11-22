from os import name
from app import db

class User(db.Model):
    __tablename__="users"
    id=db.Column(db.Integer, primary_key= True, autoincrement=True)
    name = db.Column(db.String(50))
    useranme = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(200))
    phone = db.Column(db.String(50))
    
#importamos la clase User
from flask_sqlalchemy import model
from app.models.Usuario import Usuario
from app.models.Producto import Producto
from app.models.Pedido import Pedido
from app.models.Factura import Factura
from app.models.DetalleFactura import DetalleFactura
#from app.models.DetalleFactura import DetalleFactura


#importamos la bdd
from app import db, bycrypt, app
#borrar y crear bdd
db.drop_all()
db.create_all()
def addUser():
    nombre = 'admin'
    usuario = 'admin'
    direccion = 'Sin direccion'
    email = 'admin@mail.com'          
    clave = bycrypt.generate_password_hash('admin123')
    telefono = 'sin telefono'
    rol_usuario = 'admin'
    foto_perfil = 'user.png'

    user = Usuario(nombre=nombre,usuario=usuario,direccion=direccion, email=email, clave=clave, telefono=telefono,rol_usuario=rol_usuario, foto_perfil=foto_perfil)
    db.session.add(user)
    db.session.commit()
    return 'ok'
addUser()
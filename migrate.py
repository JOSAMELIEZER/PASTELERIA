#importamos la clase User
from app.models.Factura import Factura
from app.models.Pedido import Pedido
from app.models.Producto import Producto
from app.models.User import User
#importamos la bdd
from app import db
#borrar y crear bdd
db.drop_all()
db.create_all()
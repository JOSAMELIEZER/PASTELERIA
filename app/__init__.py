__version__ = "0.1"
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import secrets

UPLOAD_FOLDER = 'app/static/img/'
#app = Flask('app')

app = Flask(__name__, template_folder="views")

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
#CONEXION CON LA BDD
app.config['SQLALCHEMY_DATABASE_URI']= "mysql+pymysql://root@localhost/dbpython"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

secret = secrets.token_urlsafe(32)
app.config['SECRET_KEY'] = secret
#en una variable guardamos la configuracion de la bdd
db=SQLAlchemy(app)
bycrypt = Bcrypt(app)

app.debug = True

from app.routes.auth_router import auth_router
app.register_blueprint(auth_router)
from app.routes.main_router import main_router
app.register_blueprint(main_router)
from app.routes.producto_route import producto_route
app.register_blueprint(producto_route)
from app.routes.usuario_route import usuario_route
app.register_blueprint(usuario_route)
from app.routes.mensaje_router import mensaje_router
app.register_blueprint(mensaje_router)

from app.routes.perfil_router import perfil_router
app.register_blueprint(perfil_router)

from app.routes.client_router import client_router
app.register_blueprint(client_router)

from app.routes.info_router import info_router
app.register_blueprint(info_router)

from app.routes.contacto_router import contacto_router
app.register_blueprint(contacto_router)
#from app.routes.pedido_router import pedido_router
#app.register_blueprint(pedido_router)
from app.routes.pedido_router import pedido_router
app.register_blueprint(pedido_router)

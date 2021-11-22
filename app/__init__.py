__version__ = "0.1"
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import secrets

UPLOAD_FOLDER = 'app/static/img/uploads/'
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

app.debug = True

from app.routes.main_router import main_router
app.register_blueprint(main_router)

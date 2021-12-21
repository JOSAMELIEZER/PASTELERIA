from app.models.Usuario import Usuario
from app import db
from flask import render_template
class InfoController():
    def __init__(self):
        pass

    def index(self):
        user= Usuario.query.all()
        return render_template('info/index.html', user=user)
        
infocontroller = InfoController()

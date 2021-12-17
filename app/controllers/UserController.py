from app.models.Usuario import Usuario
from app import db
from flask import render_template
class MainController():
    def __init__(self):
        pass

    def index(self):
        # user = {'name': 'Josam Pinaya'}
        user= Usuario.query.get(1)
        return render_template('index.html', user=user)
        """ from app.models.User import User
        users = User.query.all()
        return render_template('materias/index.html', users=users) """

maincontroller = MainController()
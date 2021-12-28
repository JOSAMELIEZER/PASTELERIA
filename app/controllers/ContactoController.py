from flask import render_template, url_for, request, redirect, flash
from app.models.Usuario import Usuario
from app import db
class ContactoController():
    def __init__(self):
        pass

    def index(self):
        user= Usuario.query.all()
        return render_template('contacto/index.html', user=user)
    def store(self):
        flash('Mensaje Enviado.')
        return redirect(url_for('contacto_router.index'))
        
contactocontroller = ContactoController()
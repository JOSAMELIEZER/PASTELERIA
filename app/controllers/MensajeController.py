from flask import render_template, url_for, request, redirect, flash
from app.models.Mensaje import Mensaje
from app import db, bycrypt
#definimos clase controlador
class MensajeController():
    def __init__(self):
        pass
 
    #se retorna el metodo index igual con self
    def index(self):
        mensajes = Mensaje.query.all()
        return render_template('mensaje/index.html',mensajes = mensajes)

    def index2(self):
        return render_template('contacto/index.html')

    def store(self):
        if request.method == 'POST':
            nombre = request.form['nombre']
            correo = request.form['correo']
            asunto = request.form['asunto']
            mensaje = request.form['mensaje']
            mensajeadd = Mensaje(nombre = nombre, correo = correo, asunto = asunto, mensaje = mensaje)
            db.session.add(mensajeadd)
            db.session.commit()
            flash('Mensaje enviado correctamente')
            return redirect(url_for('mensaje_router.index2'))

    def delete(self, _id):
        mensaje = Mensaje.query.get(_id)
        db.session.delete(mensaje)
        db.session.commit()
        flash('El usuario se ha eliminado con exito')
        return redirect(url_for('mensaje_router.index'))
   
mensajecontroller = MensajeController()
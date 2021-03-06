from app.models.Usuario import Usuario
from app import db
from flask import render_template, flash, redirect, url_for, request
class UsuarioController():
    def __init__(self):
        pass

    def index(self):
        # usuario = {'name': 'Josam Pinaya'}
        usuarios= Usuario.query.all()
        return render_template('usuario/index.html', usuarios=usuarios)
        """ from app.models.Usuario import Usuario
        usuarios = Usuario.query.all()
        return render_template('materias/index.html', usuarios=usuarios) """
    def eliminar(self, _id):
        usuario = Usuario.query.get(_id)
        db.session.delete(usuario)
        db.session.commit()
        flash('El usuario '+ usuario.nombre +' se ha eliminado con éxito.')
        return redirect(url_for('usuario_route.index'))
    def obtenerUsuario(self, _id):
        consulta_rol =  Usuario.query.get(_id)
        return str(consulta_rol.rol_usuario)
    def cambiarRol(self):
        if request.method == 'POST':
            rol_usuario = request.form['rol']
            _id = request.form['id']
            usuario = Usuario.query.get(_id)
            usuario.rol_usuario = rol_usuario
            db.session.commit()
            flash('El usuario '+ usuario.nombre +' ahora es '+ rol_usuario)
            return redirect(url_for('usuario_route.index'))
usuariocontroller = UsuarioController()
from flask import render_template, url_for, request, redirect, flash
from app.models.Usuario import Usuario
from app import db, app
from flask_login import current_user

import os
import time
from PIL import Image #pip install pillow
import urllib.request
from werkzeug.utils import secure_filename


class PerfilController():
    def __init__(self):
        pass
 
    def index(self):
        iduser = current_user.id
        user = Usuario.query.get(iduser)
        return render_template('perfil/index.html', Usuario=user)
    def edit(self, _id):
        user = Usuario.query.get(_id)
        return render_template('perfil/edit.html',Usuario=user)
    def updateprofile(self, _id):
        if request.method == 'POST':
            perfilV = request.form['nombre']
            perfilDB = Usuario.query.get(_id)
            perfilDB.nombre = perfilV
            perfilV1 = request.form['direccion']
            perfilDB = Usuario.query.get(_id)
            perfilDB.direccion = perfilV1
            perfilV2 = request.form['telefono']
            perfilDB = Usuario.query.get(_id)
            perfilDB.telefono = perfilV2
            perfilV3 = request.form['email']
            perfilDB = Usuario.query.get(_id)
            perfilDB.email = perfilV3
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            if file.filename == '':
                flash('No image selected for uploading')
                return redirect(request.url)
            if file: #and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                #guardar nombre
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                
                fecha = time.strftime("%Y%m%d%H%M%S")
                imgPath = app.config['UPLOAD_FOLDER'] + filename
                img = Image.open(imgPath)
                img.save('app/static/img/'+fecha+'.png')
                os.remove('app/static/img/'+filename)
                newfilename = fecha+'.png'



                producto =  Usuario.query.get(_id)   
                producto.foto_perfil = newfilename
                db.session.commit()

                flash('Datos de Perfil actualizado exitosamente')
                return redirect(url_for('perfil_router.index'))
            else:
                flash('Allowed image types are -> png, jpg, jpeg, gif')
                return redirect(request.url)
 
perfilcontroller = PerfilController()
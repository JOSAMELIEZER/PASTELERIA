from flask import render_template, url_for, request, redirect, flash
from app.models.Producto import Producto
from app import db, app

import os
import time
from PIL import Image #pip install pillow
import urllib.request
from werkzeug.utils import secure_filename

class ProductoController():
    def __init__(self):
        pass

    def index1(self):
        producto = Producto.query.all()
        return render_template('producto/index.html',producto=producto)
    def create(self):
        return render_template('producto/create.html')
    def store(self):
        if request.method == 'POST':
            nom_prod = request.form['nom_prod']
            precio = request.form['precio']
            desc_prod = request.form['desc_prod']
            tipo = request.form['tipo']
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
                
                
                productoadd = Producto(nom_prod = nom_prod,precio=precio,desc_prod=desc_prod,picture_prod=newfilename,tipo=tipo)
                db.session.add(productoadd)
                db.session.commit()

                
                
                flash('El registro se ha realizado con éxito.')
                return redirect(url_for('producto_route.index'))
            else:
                flash('Allowed image types are -> png, jpg, jpeg, gif')
                return redirect(request.url)
            
    def delete(self, _id):
        producto = Producto.query.get(_id)
        db.session.delete(producto)
        db.session.commit()
        flash('El registro se ha eliminado con éxito.')
        return redirect(url_for('producto_route.index'))
    def edit(self, _id):
        producto = Producto.query.get(_id)
        return render_template('producto/edit.html',producto=producto)
    def update(self, _id):
        if request.method == 'POST':
            productoV = request.form['nom_prod']
            productoDB = Producto.query.get(_id)
            productoDB.nom_prod = productoV
            productoV1 = request.form['precio']
            productoDB = Producto.query.get(_id)
            productoDB.precio = productoV1
            productoV2 = request.form['desc_prod']
            productoDB = Producto.query.get(_id)
            productoDB.desc_prod = productoV2
            productoV3 = request.form['tipo']
            productoDB = Producto.query.get(_id)
            productoDB.tipo = productoV3
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

                producto =  Producto.query.get(_id)   
                producto.picture_prod = newfilename
                db.session.commit()
                flash('El producto se ha actualizado con éxito.')
                return redirect(url_for('producto_route.index'))
            else:
                flash('Allowed image types are -> png, jpg, jpeg, gif')
                return redirect(request.url)
    def show(self, _id):
        producto = Producto.query.get(_id)
        return render_template('producto/show.html',producto=producto)      

productocontroller = ProductoController()
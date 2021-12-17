from flask import render_template, url_for, request, redirect, flash
from app.models.Producto import Producto
from app import db
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
            costo = request.form['costo']
            #from app.models.Alumno import Alumno
            productoadd = Producto(nom_prod = nom_prod, costo = costo)
            db.session.add(productoadd)
            db.session.commit()
            flash('El nuevo productoo se ha registrado correctamente!!!')
            return redirect(url_for('producto_route.index'))
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
            productoV = request.form['producto']
            productoDB = Producto.query.get(_id)
            productoDB.producto = productoV
            db.session.commit()
            flash('El registro se ha actualizado con éxito.')
            return redirect(url_for('producto_route.index'))

productocontroller = ProductoController()

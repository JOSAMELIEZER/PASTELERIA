from flask import render_template, url_for, request, redirect, flash
from app.models.Pedido import Pedido
from app import db
class PedidoController():
    def __init__(self):
        pass

    def index1(self):
        pedido = Pedido.query.all()
        return render_template('pedido/index.html',pedido=pedido)
    def create(self):
        return render_template('pedido/create.html')
    def store(self):
        if request.method == 'POST':
            total = request.form['total']
            pedidoadd = Pedido(total= total)
            db.session.add(pedidoadd) 
            db.session.commit()
            flash('El registro se ha realizado con éxito.')
            return redirect(url_for('pedido_route.index'))
    def delete(self, _id):
        pedido = Pedido.query.get(_id)
        db.session.delete(pedido)
        db.session.commit()
        flash('El registro se ha eliminado con éxito.')
        return redirect(url_for('pedido_route.index'))
    def edit(self, _id):
        pedido = Pedido.query.get(_id)
        return render_template('pedido/edit.html',pedido=pedido)
    def update(self, _id):
        if request.method == 'POST':
            pedidoV = request.form['pedido']
            pedidoDB = Pedido.query.get(_id)
            pedidoDB.pedido = pedidoV
            db.session.commit()
            flash('El registro se ha actualizado con éxito.')
            return redirect(url_for('pedido_route.index'))

pedidocontroller = PedidoController()

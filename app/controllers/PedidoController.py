from flask import render_template, url_for, request, redirect, flash
from app.models.Pedido import Pedido
from app import db


class PedidoController():
    def __init__(self):
        pass

    def index1(self):
        return render_template('pedido/index.html')
    
            
pedidocontroller = PedidoController()
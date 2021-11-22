from flask import Blueprint
from app.controllers.MainController import maincontroller

main_router = Blueprint('main_router', __name__)

@main_router.route('/',methods=['GET'])
def main():
    return maincontroller.index()

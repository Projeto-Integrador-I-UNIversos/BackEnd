from flask import Blueprint, jsonify
from models.escritor import Escritor
from models import mysql

consultar_escritores_bp = Blueprint('consultar_escritores', __name__)
escritor_model = Escritor(mysql)

@consultar_escritores_bp.route('/consultar-escritores', methods=['GET'])
def consultar_escritores():
    escritores = escritor_model.buscar_escritores()
    return jsonify(escritores), 200

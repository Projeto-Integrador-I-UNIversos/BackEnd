from flask import Blueprint, request, jsonify
from models.escritor import Escritor
from models import mysql

escritor_bp = Blueprint('escritor', __name__)
escritor_model = Escritor(mysql)

@escritor_bp.route('/cadastro', methods=['POST'])
def criar_escritor():
    dados = request.json
    idEscritor = escritor_model.criar_escritor(dados)
    return jsonify({"idEscritor": idEscritor}), 201

@escritor_bp.route('/escritores/<int:idUsuario>', methods=['GET'])
def buscar_escritor(idUsuario):
    escritor = escritor_model.buscar_escritor_por_usuario(idUsuario)
    return jsonify(escritor), 200

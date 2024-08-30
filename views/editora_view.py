from flask import Blueprint, request, jsonify
from models.editora import Editora
from models import mysql

editora_bp = Blueprint('editora', __name__)
editora_model = Editora(mysql)

@editora_bp.route('/editoras', methods=['POST'])
def criar_editora():
    dados = request.json
    idEditora = editora_model.criar_editora(dados)
    return jsonify({"idEditora": idEditora}), 201

@editora_bp.route('/editoras/<int:idUsuario>', methods=['GET'])
def buscar_editora(idUsuario):
    editora = editora_model.buscar_editora_por_usuario(idUsuario)
    return jsonify(editora), 200

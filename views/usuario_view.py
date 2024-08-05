from flask import Blueprint, request, jsonify
from models.usuario import UsuarioModel
from models import mysql

usuario_bp = Blueprint('usuario', __name__)
usuario_model = UsuarioModel(mysql)

@usuario_bp.route('/usuarios', methods=['POST'])
def criar_usuario():
    dados = request.json
    idUsuario = usuario_model.criar_usuario(dados['email'], dados['senha'], dados['tipo'])
    return jsonify({"idUsuario": idUsuario}), 201

@usuario_bp.route('/usuarios/<int:idUsuario>', methods=['GET'])
def buscar_usuario(idUsuario):
    usuario = usuario_model.buscar_usuario_por_id(idUsuario)
    return jsonify(usuario), 200

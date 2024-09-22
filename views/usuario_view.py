from flask import Blueprint, request, jsonify
from controllers.usuario_controller import UsuarioController
from models import mysql


usuario_bp = Blueprint('usuario', __name__)
usuario_controller = UsuarioController(mysql)


@usuario_bp.route('/cadastro', methods=['POST'])
def criar_usuario():
    dados = request.json

    if 'email' not in dados or 'senha' not in dados or 'tipo' not in dados:
        return jsonify({"message": "Dados incompletos. Email, senha e tipo são necessários.", "dados": dados}), 400


    if dados['tipo'] == 'escritor':
        if 'escritor_dados' not in dados:
            return jsonify({"message": "Dados do escritor são necessários."}), 400

    elif dados['tipo'] == 'editora':
        if 'editora_dados' not in dados:
            return jsonify({"message": "Dados da editora são necessários."}), 400

    try:
        idUsuario = usuario_controller.criar_usuario(dados)
        return jsonify({"idUsuario": idUsuario, "dados": dados}), 201
    except ValueError as e:
        return jsonify({"message": str(e)}), 400


@usuario_bp.route('/buscar/<int:idUsuario>', methods=['GET'])
def buscar_usuario(idUsuario):
    usuario = usuario_controller.buscar_usuario_por_id(idUsuario)
    return jsonify(usuario), 200


@usuario_bp.route('/usuarios', methods=['GET'])
def listar_usuarios():
    usuarios = usuario_controller.listar_todos_usuarios()
    return jsonify(usuarios), 200


@usuario_bp.route('/deletar/<int:idUsuario>', methods=['DELETE'])
def deletar_usuario(idUsuario):
    success = usuario_controller.deletar_usuario(idUsuario)
    if success:
        return jsonify({"message": "Usuário deletado com sucesso"}), 200
    else:
        return jsonify({"message": "Usuário não encontrado"}), 404


@usuario_bp.route('/atualizar/<int:idUsuario>', methods=['PUT'])
def atualizar_usuario(idUsuario):
    dados = request.json
    success = usuario_controller.atualizar_usuario(idUsuario, dados)
    if success:
        return jsonify({"message": "Usuário atualizado com sucesso"}), 200
    else:
        return jsonify({"message": "Usuário não encontrado"}), 404


@usuario_bp.route('/login', methods=['POST'])
def login():
    dados = request.json
    email = dados.get('email')
    senha = dados.get('senha')

    if not email or not senha:
        return jsonify({"message": "Email e senha são necessários"}), 400

    sucesso, token, tipo = usuario_controller.login(email, senha)  
    if sucesso:
        return jsonify({"token": token, "tipo": tipo}), 200  
    else:
        return jsonify({"message": "Credenciais inválidas"}), 401

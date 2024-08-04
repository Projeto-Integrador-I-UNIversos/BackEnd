from flask import Blueprint, request, jsonify
from controllers.usuario_controller import UsuarioController
from config import mysql

usuario_bp = Blueprint('usuario', __name__)
usuario_controller = UsuarioController(mysql)

@usuario_bp.route('/cadastro', methods=['POST'])
def cadastrar_usuario():
    data = request.json
    email = data.get('email')
    senha = data.get('senha')
    tipo = data.get('tipo')

    if not email or not senha or not tipo:
        return jsonify({'status': 'error', 'message': 'Dados obrigatórios faltando'}), 400

    id_usuario = usuario_controller.cadastrar_usuario(email, senha, tipo)
    return jsonify({'status': 'success', 'message': 'Usuário cadastrado com sucesso', 'idUsuario': id_usuario})

@usuario_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    senha = data.get('senha')

    if not email or not senha:
        return jsonify({'status': 'error', 'message': 'Email e senha são obrigatórios'}), 400

    usuario = usuario_controller.autenticar_usuario(email, senha)
    if usuario:
        return jsonify({'status': 'success', 'message': 'Autenticação bem-sucedida', 'usuario': usuario})
    else:
        return jsonify({'status': 'error', 'message': 'Email ou senha inválidos'}), 401

@usuario_bp.route('/recuperar_senha', methods=['POST'])
def recuperar_senha():
    data = request.json
    email = data.get('email')
    nova_senha = data.get('nova_senha')

    if not email or not nova_senha:
        return jsonify({'status': 'error', 'message': 'Email e nova senha são obrigatórios'}), 400

    sucesso = usuario_controller.recuperar_senha(email, nova_senha)
    if sucesso:
        return jsonify({'status': 'success', 'message': 'Senha atualizada com sucesso'})
    else:
        return jsonify({'status': 'error', 'message': 'Erro ao atualizar senha'}), 500

@usuario_bp.route('/bloquear/<int:idUsuario>', methods=['POST'])
def bloquear_usuario(idUsuario):
    usuario_controller.bloquear_usuario(idUsuario)
    return jsonify({'status': 'success', 'message': 'Usuário bloqueado com sucesso'})

@usuario_bp.route('/editar/<int:idUsuario>', methods=['PUT'])
def editar_usuario(idUsuario):
    data = request.json
    sucesso = usuario_controller.editar_usuario(idUsuario, data)
    if sucesso:
        return jsonify({'status': 'success', 'message': 'Usuário atualizado com sucesso'})
    else:
        return jsonify({'status': 'error', 'message': 'Erro ao atualizar usuário'}), 500

@usuario_bp.route('/deletar/<int:idUsuario>', methods=['DELETE'])
def deletar_usuario(idUsuario):
    sucesso = usuario_controller.deletar_usuario(idUsuario)
    if sucesso:
        return jsonify({'status': 'success', 'message': 'Usuário deletado com sucesso'})
    else:
        return jsonify({'status': 'error', 'message': 'Erro ao deletar usuário'}), 500

from flask import Blueprint, request, jsonify
from controllers.usuario_controller import UsuarioController

usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route('/cadastro', methods=['POST'])
def cadastro_usuario():
    data = request.json
    usuario_id = UsuarioController.cadastrar_usuario(data)
    return jsonify({'status': 'success', 'usuario_id': usuario_id})

@usuario_bp.route('/login', methods=['POST'])
def login_usuario():
    data = request.json
    email = data['email']
    senha = data['senha']
    usuario = UsuarioController.autenticar_usuario(email, senha)
    if usuario:
        return jsonify({'status': 'success', 'usuario_id': usuario['id'], 'tipo': usuario['tipo']})
    else:
        return jsonify({'status': 'error', 'message': 'Credenciais inválidas'})

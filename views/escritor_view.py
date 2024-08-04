from flask import Blueprint, request, jsonify
from controllers.escritor_controller import EscritorController
from config import mysql

escritor_bp = Blueprint('escritor', __name__)
escritor_controller = EscritorController(mysql)

@escritor_bp.route('/cadastro', methods=['POST'])
def cadastrar_escritor():
    data = request.json
    required_fields = ['nome', 'dataNasc', 'telefone', 'cpf', 'nacionalidade', 'idUsuario']
    
    for field in required_fields:
        if not data.get(field):
            return jsonify({'status': 'error', f'message': 'Campo obrigatório {field} está faltando'}), 400

    id_escritor = escritor_controller.cadastrar_escritor(data)
    return jsonify({'status': 'success', 'message': 'Escritor cadastrado com sucesso', 'idEscritor': id_escritor})

@escritor_bp.route('/<int:idUsuario>', methods=['GET'])
def buscar_escritor(idUsuario):
    escritor = escritor_controller.buscar_escritor_por_usuario(idUsuario)
    if escritor:
        return jsonify({'status': 'success', 'escritor': escritor})
    else:
        return jsonify({'status': 'error', 'message': 'Escritor não encontrado'}), 404

@escritor_bp.route('/editar/<int:idEscritor>', methods=['PUT'])
def editar_escritor(idEscritor):
    data = request.json
    sucesso = escritor_controller.editar_escritor(idEscritor, data)
    if sucesso:
        return jsonify({'status': 'success', 'message': 'Escritor atualizado com sucesso'})
    else:
        return jsonify({'status': 'error', 'message': 'Erro ao atualizar escritor'}), 500

@escritor_bp.route('/deletar/<int:idEscritor>', methods=['DELETE'])
def deletar_escritor(idEscritor):
    sucesso = escritor_controller.deletar_escritor(idEscritor)
    if sucesso:
        return jsonify({'status': 'success', 'message': 'Escritor deletado com sucesso'})
    else:
        return jsonify({'status': 'error', 'message': 'Erro ao deletar escritor'}), 500

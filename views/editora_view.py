from flask import Blueprint, request, jsonify
from controllers.editora_controller import EditoraController
from config import mysql

editora_bp = Blueprint('editora', __name__)
editora_controller = EditoraController(mysql)

@editora_bp.route('/cadastro', methods=['POST'])
def cadastrar_editora():
    data = request.json
    required_fields = ['nome', 'cnpj', 'telefone', 'siteInstitucional', 'pais', 'descricao', 'idUsuario']
    
    for field in required_fields:
        if not data.get(field):
            return jsonify({'status': 'error', f'message': 'Campo obrigatório {field} está faltando'}), 400

    id_editora = editora_controller.cadastrar_editora(data)
    return jsonify({'status': 'success', 'message': 'Editora cadastrada com sucesso', 'idEditora': id_editora})

@editora_bp.route('/<int:idUsuario>', methods=['GET'])
def buscar_editora(idUsuario):
    editora = editora_controller.buscar_editora_por_usuario(idUsuario)
    if editora:
        return jsonify({'status': 'success', 'editora': editora})
    else:
        return jsonify({'status': 'error', 'message': 'Editora não encontrada'}), 404

@editora_bp.route('/editar/<int:idEditora>', methods=['PUT'])
def editar_editora(idEditora):
    data = request.json
    sucesso = editora_controller.editar_editora(idEditora, data)
    if sucesso:
        return jsonify({'status': 'success', 'message': 'Editora atualizada com sucesso'})
    else:
        return jsonify({'status': 'error', 'message': 'Erro ao atualizar editora'}), 500

@editora_bp.route('/deletar/<int:idEditora>', methods=['DELETE'])
def deletar_editora(idEditora):
    sucesso = editora_controller.deletar_editora(idEditora)
    if sucesso:
        return jsonify({'status': 'success', 'message': 'Editora deletada com sucesso'})
    else:
        return jsonify({'status': 'error', 'message': 'Erro ao deletar editora'}), 500

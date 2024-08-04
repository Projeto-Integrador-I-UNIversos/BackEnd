from flask import Blueprint, request, jsonify
from controllers.livro_controller import LivroController
from config import mysql

livro_bp = Blueprint('livro', __name__)
livro_controller = LivroController(mysql)

@livro_bp.route('/adicionar', methods=['POST'])
def adicionar_livro():
    data = request.json
    required_fields = ['titulo', 'idioma', 'QuantPaginas', 'pais', 'descricao', 'capaLivro', 'idEscritor', 'status', 'PdfLivro']
    
    for field in required_fields:
        if not data.get(field):
            return jsonify({'status': 'error', f'message': 'Campo obrigatório {field} está faltando'}), 400

    id_livro = livro_controller.adicionar_livro(data)
    return jsonify({'status': 'success', 'message': 'Livro adicionado com sucesso', 'idLivro': id_livro})

@livro_bp.route('/escritor/<int:idEscritor>', methods=['GET'])
def buscar_livros_por_escritor(idEscritor):
    livros = livro_controller.buscar_livros_por_escritor(idEscritor)
    return jsonify({'status': 'success', 'livros': livros})

@livro_bp.route('/editar/<int:idLivro>', methods=['PUT'])
def editar_livro(idLivro):
    data = request.json
    sucesso = livro_controller.editar_livro(idLivro, data)
    if sucesso:
        return jsonify({'status': 'success', 'message': 'Livro atualizado com sucesso'})
    else:
        return jsonify({'status': 'error', 'message': 'Erro ao atualizar livro'}), 500

@livro_bp.route('/deletar/<int:idLivro>', methods=['DELETE'])
def deletar_livro(idLivro):
    sucesso = livro_controller.deletar_livro(idLivro)
    if sucesso:
        return jsonify({'status': 'success', 'message': 'Livro deletado com sucesso'})
    else:
        return jsonify({'status': 'error', 'message': 'Erro ao deletar livro'}), 500

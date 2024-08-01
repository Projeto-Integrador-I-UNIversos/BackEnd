from flask import Blueprint, request, jsonify
from controllers.livro_controller import LivroController
from config import conn

livro_bp = Blueprint('livro', __name__)

@livro_bp.route('/adicionar', methods=['POST'])
def adicionar_livro():
    data = request.json
    livro_id = LivroController.adicionar_livro(data)
    return jsonify({'status': 'success', 'livro_id': livro_id})

@livro_bp.route('/enviar_proposta', methods=['POST'])
def enviar_proposta():
    data = request.json
    proposta_id = LivroController.enviar_proposta(data)
    return jsonify({'status': 'success', 'proposta_id': proposta_id})

@livro_bp.route('/livros', methods=['GET'])
def listar_livros():
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tb_livro")
        livros = cursor.fetchall()
        cursor.close()
        return jsonify({'livros': livros})

    except Exception as e:
        print(f"Erro ao listar livros: {e}")
        return jsonify({'status': 'error', 'message': 'Erro interno do servidor'}), 500
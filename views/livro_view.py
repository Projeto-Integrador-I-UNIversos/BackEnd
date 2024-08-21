from flask import Blueprint, request, jsonify
from models.livro import Livro
from models import mysql

livro_bp = Blueprint('livro', __name__)
livro_model = Livro(mysql)

@livro_bp.route('/cadastroLivro', methods=['POST'])
def criar_livro():
    dados = request.json
    idLivro = livro_model.criar_livro(dados)
    return jsonify({"idLivro": idLivro}), 201

@livro_bp.route('/buscarLivro/<int:idLivro>', methods=['GET'])
def buscar_livro(idLivro):
    livro = livro_model.buscar_livro_por_id(idLivro)
    return jsonify(livro), 200

@livro_bp.route('/livros', methods=['GET'])
def listar_livros():
    livros = livro_model.listar_todos_livros()
    return jsonify(livros), 200
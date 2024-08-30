from flask import Blueprint, request, jsonify
from controllers.favoritos_controller import FavoritosController
from models import mysql

favoritos_bp = Blueprint('favoritos', __name__)
favoritos_controller = FavoritosController(mysql)

@favoritos_bp.route('/favoritar/escritor', methods=['POST'])
def favoritar_escritor():
    dados = request.json
    favoritos_controller.favoritar_escritor(dados['idEditora'], dados['idEscritor'])
    return jsonify({"message": "Escritor favoritado com sucesso!"}), 201

@favoritos_bp.route('/favoritar/livro', methods=['POST'])
def favoritar_livro():
    dados = request.json
    favoritos_controller.favoritar_livro(dados['idEditora'], dados['idLivro'])
    return jsonify({"message": "Livro favoritado com sucesso!"}), 201

@favoritos_bp.route('/favoritar/editora', methods=['POST'])
def favoritar_editora():
    dados = request.json
    favoritos_controller.favoritar_editora(dados['idEscritor'], dados['idEditora'])
    return jsonify({"message": "Editora favoritada com sucesso!"}), 201

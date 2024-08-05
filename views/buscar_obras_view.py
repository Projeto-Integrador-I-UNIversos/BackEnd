from flask import Blueprint, jsonify
from models.livro import Livro
from models import mysql

buscar_obras_bp = Blueprint('buscar_obras', __name__)
livro_model = Livro(mysql)

@buscar_obras_bp.route('/buscar-obras/<int:idEscritor>', methods=['GET'])
def buscar_obras_por_escritor(idEscritor):
    obras = livro_model.buscar_livro_por_escritor(idEscritor)
    return jsonify(obras), 200

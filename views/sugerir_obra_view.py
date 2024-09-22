from flask import Blueprint, request, jsonify
from models.sugerir_obra import SugerirObra
from models import mysql

sugerir_obra_bp = Blueprint('sugerir_obra', __name__)
sugerir_obra_model = SugerirObra(mysql)

@sugerir_obra_bp.route('/sugerir-obras', methods=['POST'])
def sugerir_obra():
    dados = request.json
    idSugerirObra = sugerir_obra_model.sugerir_obra(dados)
    return jsonify({"idSugerirObra": idSugerirObra}), 201

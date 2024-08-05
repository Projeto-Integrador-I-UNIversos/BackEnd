from flask import Blueprint, request, jsonify
from models.proposta import Proposta
from models import mysql

proposta_bp = Blueprint('proposta', __name__)
proposta_model = Proposta(mysql)

@proposta_bp.route('/propostas', methods=['POST'])
def criar_proposta():
    dados = request.json
    idProposta = proposta_model.criar_proposta(dados)
    return jsonify({"idProposta": idProposta}), 201

@proposta_bp.route('/propostas/<int:idProposta>', methods=['GET'])
def buscar_proposta(idProposta):
    proposta = proposta_model.buscar_proposta_por_id(idProposta)
    return jsonify(proposta), 200

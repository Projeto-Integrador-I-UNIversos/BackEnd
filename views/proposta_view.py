from flask import Blueprint, request, jsonify
from controllers.proposta_controller import PropostaController
from config import mysql

proposta_bp = Blueprint('proposta', __name__)
proposta_controller = PropostaController(mysql)

@proposta_bp.route('/enviar', methods=['POST'])
def enviar_proposta():
    data = request.json
    required_fields = ['data', 'idEditora', 'idObra']
    
    for field in required_fields:
        if not data.get(field):
            return jsonify({'status': 'error', f'message': 'Campo obrigatório {field} está faltando'}), 400

    id_proposta = proposta_controller.enviar_proposta(data)
    return jsonify({'status': 'success', 'message': 'Proposta enviada com sucesso', 'idProposta': id_proposta})

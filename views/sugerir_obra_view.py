from flask import Blueprint, request, jsonify
from controllers.sugerir_obra_controller import SugerirObraController
from config import mysql

sugerir_obra_bp = Blueprint('sugerir_obra', __name__)
sugerir_obra_controller = SugerirObraController(mysql)

@sugerir_obra_bp.route('/sugerir', methods=['POST'])
def sugerir_obra():
    data = request.json
    required_fields = ['idEditora', 'idLivro', 'data']
    
    for field in required_fields:
        if not data.get(field):
            return jsonify({'status': 'error', f'message': 'Campo obrigatório {field} está faltando'}), 400

    id_sugestao = sugerir_obra_controller.sugerir_obra(data)
    return jsonify({'status': 'success', 'message': 'Sugestão de obra enviada com sucesso', 'idSugestao': id_sugestao})

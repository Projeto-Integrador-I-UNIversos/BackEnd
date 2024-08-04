from flask import Blueprint, request, jsonify
from controllers.buscar_obras_controller import BuscarObrasController
from config import mysql

buscar_obras_bp = Blueprint('buscar_obras', __name__)
buscar_obras_controller = BuscarObrasController(mysql)

@buscar_obras_bp.route('/buscar', methods=['GET'])
def buscar_obras():
    criterios = request.args.to_dict()
    obras = buscar_obras_controller.buscar_obras(criterios)
    return jsonify({'status': 'success', 'obras': obras})

from flask import Blueprint, request, jsonify
from controllers.consultar_escritores_controller import ConsultarEscritoresController
from config import mysql

consultar_escritores_bp = Blueprint('consultar_escritores', __name__)
consultar_escritores_controller = ConsultarEscritoresController(mysql)

@consultar_escritores_bp.route('/consultar', methods=['GET'])
def consultar_escritores():
    criterios = request.args.to_dict()
    escritores = consultar_escritores_controller.buscar_escritores(criterios)
    return jsonify({'status': 'success', 'escritores': escritores})

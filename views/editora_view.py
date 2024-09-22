from flask import Blueprint, request, jsonify
from models.editora import Editora
from models import mysql
from werkzeug.exceptions import BadRequest


editora_bp = Blueprint('editora', __name__)
editora_model = Editora(mysql)

@editora_bp.route('/editoras', methods=['POST'])
def criar_editora():
    try:
        dados = request.json
        if not dados:
            return jsonify({"erro": "Nenhum dado foi fornecido."}), 400
        
        campos_obrigatorios = ['nome', 'cnpj', 'telefone', 'linkedin', 'siteInstitucional', 'twitter', 'instagram', 'pais', 'descricao', 'idUsuario']
        for campo in campos_obrigatorios:
            if campo not in dados or not dados[campo].strip():
                return jsonify({"erro": f"Campo '{campo}' é obrigatório e não pode estar vazio."}), 400

        idEditora = editora_model.criar_editora(dados)
        return jsonify({"idEditora": idEditora}), 201

    except ValueError as e:
        return jsonify({"erro": str(e), "dados": dados}), 400
    
    except Exception as e:
        return jsonify({"erro": "Erro no servidor", "mensagem": str(e)}), 500



@editora_bp.route('/editoras/<int:idUsuario>', methods=['GET'])
def buscar_editora(idUsuario):
    editora = editora_model.buscar_editora_por_usuario(idUsuario)
    return jsonify(editora), 200

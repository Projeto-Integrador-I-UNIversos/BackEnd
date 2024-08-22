from flask import Blueprint, request, jsonify, current_app
from models.livro import Livro
from models import mysql
import os
from werkzeug.utils import secure_filename

livro_bp = Blueprint('livro', __name__)
livro_model = Livro(mysql)

@livro_bp.route('/cadastroLivro', methods=['POST'])
def criar_livro():
    dados = request.form.to_dict()
    upload_folder = current_app.config['UPLOAD_FOLDER']

    if 'PdfLivro' in request.files:
        pdf_livro = request.files['PdfLivro']
        nome_pdf_livro = secure_filename(pdf_livro.filename)
        pdf_path = os.path.join(upload_folder, nome_pdf_livro)
        pdf_livro.save(pdf_path)
        dados['PdfLivro'] = nome_pdf_livro

    if 'capaLivro' in request.files:
        capa_livro = request.files['capaLivro']
        nome_capa_livro = secure_filename(capa_livro.filename)
        capa_path = os.path.join(upload_folder, nome_capa_livro)
        capa_livro.save(capa_path)
        dados['capaLivro'] = nome_capa_livro
        print("Nome da capa do livro salvo:", nome_capa_livro)


    print("Dados após processamento:", dados)  # Log dos dados finais

    try:
        idLivro = livro_model.criar_livro(dados)
        return jsonify({"idLivro": idLivro}), 201
    except KeyError as e:
        return jsonify({"error": f"Chave ausente: {str(e)}"}), 400

@livro_bp.route('/buscarLivro/<int:idLivro>', methods=['GET'])
def buscar_livro(idLivro):
    livro = livro_model.buscar_livro_por_id(idLivro)
    return jsonify(livro), 200

@livro_bp.route('/livros', methods=['GET'])
def listar_livros():
    livros = livro_model.listar_todos_livros()
    return jsonify(livros), 200

@livro_bp.route('/editarLivro/<int:idLivro>', methods=['POST'])
def atualizar_livro(idLivro):
    dados = request.form.to_dict()
    print("Dados recebidos:", dados)  # Log dos dados recebidos

    upload_folder = current_app.config['UPLOAD_FOLDER']

    if 'PdfLivro' in request.files:
        pdf_livro = request.files['PdfLivro']
        nome_pdf_livro = secure_filename(pdf_livro.filename)
        pdf_path = os.path.join(upload_folder, nome_pdf_livro)
        pdf_livro.save(pdf_path)
        dados['PdfLivro'] = nome_pdf_livro

    if 'capaLivro' in request.files:
        capa_livro = request.files['capaLivro']
        nome_capa_livro = secure_filename(capa_livro.filename)
        capa_path = os.path.join(upload_folder, nome_capa_livro)
        capa_livro.save(capa_path)
        dados['capaLivro'] = nome_capa_livro

    if not dados:
        return jsonify({'error': 'No data provided'}), 400

    try:
        sucesso = livro_model.atualizar_livro(idLivro, dados)
        if sucesso:
            return jsonify({'message': 'Livro atualizado com sucesso!'}), 200
        else:
            return jsonify({'error': 'Erro ao atualizar o livro, nenhum registro afetado'}), 500
    except Exception as e:
        return jsonify({'error': f'Erro ao atualizar o livro: {str(e)}'}), 500

@livro_bp.route('/deletarLivro/<int:idLivro>', methods=['DELETE'])
def deletar_livro(idLivro):
    try:
        sucesso = livro_model.deletar_livro(idLivro)
        if sucesso:
            return jsonify({'message': 'Livro deletado com sucesso!'}), 200
        else:
            return jsonify({'error': f'Erro ao deletar o livro, nenhum registro afetado', 'codigo_erro': e.args[0]}), 404
    except Exception as e:
        #return jsonify({'error': f'Erro ao deletar o livro: {str(e)}'}), 500
        return jsonify({'error': f'Erro ao deletar o livro: {str(e)}', 'codigo_erro': e.args[0]}), 500

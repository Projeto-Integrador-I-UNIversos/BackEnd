from flask import Blueprint, request, jsonify
from controllers.usuario_controller import UsuarioController
from config import conn

usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route('/login', methods=['POST'])
def login_usuario():
    data = request.json
    email = data['email']
    senha = data['senha']
    usuario = UsuarioController.autenticar_usuario(email, senha)
    if usuario:
        return jsonify({'status': 'success', 'usuario_id': usuario['id'], 'tipo': usuario['tipo']})
    else:
        return jsonify({'status': 'error', 'message': 'Credenciais inválidas'})


@usuario_bp.route('/cadastro', methods=['POST'])
def cadastro_usuario():
    data = request.json
    email = data['email']
    senha = data['senha']
    tipo = data['tipo']

    cursor = conn.cursor()
    # Inserir o usuário no banco
    cursor.execute("INSERT INTO tb_usuario (email, senha, tipo) VALUES (%s, %s, %s)", (email, senha, tipo))
    conn.commit()
    cursor.close()
    return jsonify({"status": "success", "message": "Usuário cadastrado com sucesso!"})

@usuario_bp.route('/usuarios', methods=['GET'])
def listar_usuarios():
    """Listar todos os usuários"""
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tb_usuario")
    usuarios = cursor.fetchall()
    cursor.close()
    return jsonify({'usuarios': usuarios})
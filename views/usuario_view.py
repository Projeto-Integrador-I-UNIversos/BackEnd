from flask import Blueprint, request, jsonify
from controllers.usuario_controller import UsuarioController
from werkzeug.security import generate_password_hash
from config import conn

usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route('/login', methods=['POST'])
def login_usuario():
    try:
        data = request.json

        # Verifica se 'email' e 'senha' estão presentes nos dados recebidos
        email = data.get('email')
        senha = data.get('senha')

        if not email or not senha:
            return jsonify({'status': 'error', 'message': 'Email e senha são obrigatórios'}), 400

        usuario = UsuarioController.autenticar_usuario(email, senha)
        if usuario:
            return jsonify({'status': 'success', 'idUsuario': usuario['idUsuario'], 'tipo': usuario['tipo']})
        else:
            return jsonify({'status': 'error', 'message': 'Credenciais inválidas'}), 401

    except Exception as e:
        print(f"Erro no login: {e}")
        return jsonify({'status': 'error', 'message': 'Erro interno do servidor'}), 500

@usuario_bp.route('/cadastro', methods=['POST'])
def cadastro_usuario():
    try:
        data = request.json

        # Verifica se todos os campos necessários estão presentes
        email = data.get('email')
        senha = data.get('senha')
        tipo = data.get('tipo')

        if not email or not senha or not tipo:
            return jsonify({'status': 'error', 'message': 'Email, senha e tipo são obrigatórios'}), 400

        with conn.cursor() as cursor:
            # Verifica se o usuário já existe
            cursor.execute("SELECT * FROM tb_usuario WHERE email = %s", (email,))
            if cursor.fetchone():
                return jsonify({'status': 'error', 'message': 'Usuário já cadastrado'}), 400

            # Gerar hash da senha
            hashed_password = generate_password_hash(senha)

            # Inserir o usuário no banco
            cursor.execute("INSERT INTO tb_usuario (email, senha, tipo) VALUES (%s, %s, %s)", (email, hashed_password, tipo))
            conn.commit()
            
        return jsonify({"status": "success", "message": "Usuário cadastrado com sucesso!"})

    except Exception as e:
        print(f"Erro no cadastro: {e}")
        return jsonify({'status': 'error', 'message': 'Erro interno do servidor'}), 500

@usuario_bp.route('/usuarios', methods=['GET'])
def listar_usuarios():
    try:
        with conn.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM tb_usuario")
            usuarios = cursor.fetchall()
        return jsonify({'usuarios': usuarios})

    except Exception as e:
        print(f"Erro ao listar usuários: {e}")
        return jsonify({'status': 'error', 'message': 'Erro interno do servidor'}), 500
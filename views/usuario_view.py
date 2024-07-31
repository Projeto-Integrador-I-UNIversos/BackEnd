from flask import Blueprint, request, jsonify
from controllers.usuario_controller import UsuarioController
from config import conn
import bcrypt
from mysql.connector import Error


usuario_bp = Blueprint('usuario', __name__)

def autenticar_usuario(email, senha):
        """Verifica as credenciais do usuário e retorna as informações se forem válidas."""
        connection = conn()
        if connection is None:
            return None
        
        try:
            cursor = connection.cursor(dictionary=True)
            query = "SELECT id, senha, tipo FROM tb_Usuario WHERE email = %s"
            cursor.execute(query, (email,))
            resultado = cursor.fetchone()
            
            if resultado and bcrypt.checkpw(senha.encode('utf-8'), resultado['senha'].encode('utf-8')):
                return resultado
            else:
                return None
        except Error as e:
            print(f"Erro ao autenticar usuário: {e}")
            return None
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                
@usuario_bp.route('/login', methods=['POST'])
def login_usuario():
    data = request.json
    email = data.get('email')
    senha = data.get('senha')

    if not email or not senha:
        return jsonify({'status': 'error', 'message': 'Email e senha são obrigatórios!'}), 400

    usuario = UsuarioController.autenticar_usuario(email, senha)
    if usuario:
        return jsonify({'status': 'success', 'usuario_id': usuario['id'], 'tipo': usuario['tipo']})
    else:
        return jsonify({'status': 'error', 'message': 'Credenciais inválidas'}), 401       

"""@usuario_bp.route('/login', methods=['POST'])
def login_usuario():
    data = request.json
    email = data['email']
    senha = data['senha']
    usuario = UsuarioController.autenticar_usuario(email, senha)
    if usuario:
        return jsonify({'status': 'success', 'usuario_id': usuario['id'], 'tipo': usuario['tipo']})
    else:
        return jsonify({'status': 'error', 'message': 'Credenciais inválidas'})
"""


@usuario_bp.route('/cadastro', methods=['POST'])
def cadastro_usuario():
    data = request.json
    email = data['email']
    senha = data['senha']
    tipo = data['tipo']

    cursor = conn.cursor()
    # Inserir o usuário no banco
    cursor.execute("INSERT INTO tb_Usuario (email, senha, tipo) VALUES (%s, %s, %s)", (email, senha, tipo))
    conn.commit()
    cursor.close()
    return jsonify({"status": "success", "message": "Usuário cadastrado com sucesso!"})

@usuario_bp.route('/usuarios', methods=['GET'])
def listar_usuarios():
    """Listar todos os usuários"""
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tb_Usuario")
    usuarios = cursor.fetchall()
    cursor.close()
    return jsonify({'usuarios': usuarios})
import hashlib
from werkzeug.security import generate_password_hash, check_password_hash

class UsuarioModel:
    def __init__(self, mysql):
        self.mysql = mysql

    @staticmethod
    def hash_senha(senha):
        return hashlib.sha256(senha.encode()).hexdigest()

    def criar_usuario(self, email, senha, tipo):
        senha_hash = generate_password_hash(senha)
        try:
            with self.mysql.connection.cursor() as cursor:
                cursor.execute(
                    'INSERT INTO tb_usuario (email, senha, tipo) VALUES (%s, %s, %s)',
                    (email, senha_hash, tipo)
                )
                self.mysql.connection.commit()
            return cursor.lastrowid
        except Exception as e:
            print(f"Erro ao criar usuário: {e}")
            return None

    def buscar_usuario_por_email(self, email):
        query = "SELECT * FROM tb_usuario WHERE email = %s"
        try:
            with self.mysql.connection.cursor(dictionary=True) as cursor:
                cursor.execute(query, (email,))
                usuario = cursor.fetchone()
            return usuario
        except Exception as e:
            print(f"Erro ao buscar usuário por email: {e}")
            return None

    def buscar_usuario_por_id(self, idUsuario):
        query = 'SELECT * FROM tb_usuario WHERE idUsuario = %s'
        try:
            with self.mysql.connection.cursor(dictionary=True) as cursor:
                cursor.execute(query, (idUsuario,))
                return cursor.fetchone()
        except Exception as e:
            print(f"Erro ao buscar usuário por ID: {e}")
            return None
    
    def listar_todos_usuarios(self):
        try:
            with self.mysql.connection.cursor(dictionary=True) as cursor:
                cursor.execute('SELECT * FROM tb_usuario')
                usuarios = cursor.fetchall()
            return usuarios
        except Exception as e:
            print(f"Erro ao listar todos os usuários: {e}")
            return []

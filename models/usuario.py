import hashlib

class UsuarioModel:
    def __init__(self, mysql):
        self.mysql = mysql

    @staticmethod
    def hash_senha(senha):
        return hashlib.sha256(senha.encode()).hexdigest()

    def criar_usuario(self, email, senha, tipo):
        hashed_senha = self.hash_senha(senha)
        with self.mysql.connection.cursor() as cursor:
            cursor.execute(
                'INSERT INTO tb_usuario (email, senha, tipo) VALUES (%s, %s, %s)',
                (email, hashed_senha, tipo)
            )
            self.mysql.connection.commit()
        return cursor.lastrowid

    def buscar_usuario_por_email(self, email):
        with self.mysql.connection.cursor(dictionary=True) as cursor:
            cursor.execute('SELECT * FROM tb_usuario WHERE email = %s', (email,))
            return cursor.fetchone()

    def buscar_usuario_por_id(self, idUsuario):
        with self.mysql.connection.cursor(dictionary=True) as cursor:
            cursor.execute('SELECT * FROM tb_usuario WHERE idUsuario = %s', (idUsuario,))
            return cursor.fetchone()

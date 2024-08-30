from werkzeug.security import generate_password_hash, check_password_hash

class UsuarioModel:

    def __init__(self, mysql):
        self.mysql = mysql

    def criar_usuario(self, email, senha, tipo):
        with self.mysql.connection.cursor() as cursor:
            cursor.execute(
                'INSERT INTO tb_usuario (email, senha, tipo) VALUES (%s, %s, %s)',
                (email, senha, tipo)
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

    def listar_todos_usuarios(self):
        with self.mysql.connection.cursor(dictionary=True) as cursor:
            cursor.execute('SELECT * FROM tb_usuario')
            return cursor.fetchall()

    def deletar_usuario(self, idUsuario):
        with self.mysql.connection.cursor() as cursor:
            cursor.execute('DELETE FROM tb_usuario WHERE idUsuario = %s', (idUsuario,))
            self.mysql.connection.commit()

    def atualizar_usuario(self, idUsuario, dados):
        set_clause = ', '.join([f"{key} = %s" for key in dados.keys()])
        values = list(dados.values())
        values.append(idUsuario)
        query = f'UPDATE tb_usuario SET {set_clause} WHERE idUsuario = %s'

        with self.mysql.connection.cursor() as cursor:
            cursor.execute(query, values)
            self.mysql.connection.commit()
            return cursor.rowcount > 0

    def verificar_senha(self, senha_hash, senha):
        return check_password_hash(senha_hash, senha)

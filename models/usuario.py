from flask_mysql_connector import MySQL
from . import mysql

class UsuarioModel:
    @staticmethod
    def criar_usuario(email, senha, tipo):
        # Use o contexto with para garantir que o cursor seja fechado adequadamente
        with mysql.connection.cursor() as cursor:
            cursor.execute(
                'INSERT INTO tb_usuario (email, senha, tipo) VALUES (%s, %s, %s)',
                (email, senha, tipo)
            )
            mysql.connection.commit()
            usuario_id = cursor.lastrowid
        return usuario_id

    @staticmethod
    def buscar_usuario_por_email(email):
        # Use o contexto with para garantir que o cursor seja fechado adequadamente
        with mysql.connection.cursor(dictionary=True) as cursor:
            cursor.execute(
                'SELECT * FROM tb_usuario WHERE email = %s',
                (email,)
            )
            usuario = cursor.fetchone()
        return usuario

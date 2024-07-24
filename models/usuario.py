from flask_mysql_connector import MySQL
from . import mysql

class UsuarioModel:
    @staticmethod
    def criar_usuario(email, senha, tipo):
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO usuarios (email, senha, tipo) VALUES (%s, %s, %s)', (email, senha, tipo))
        mysql.connection.commit()
        usuario_id = cursor.lastrowid
        cursor.close()
        return usuario_id

    @staticmethod
    def buscar_usuario_por_email(email):
        cursor = mysql.connection.cursor(dictionary=True)
        cursor.execute('SELECT * FROM usuarios WHERE email = %s', (email,))
        usuario = cursor.fetchone()
        cursor.close()
        return usuario

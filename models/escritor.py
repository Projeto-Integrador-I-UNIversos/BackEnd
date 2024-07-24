from flask_mysql_connector import MySQL
from . import mysql

class EscritorModel:
    @staticmethod
    def criar_escritor(usuario_id, nome, idade, telefone, cpf, instagram, linkedin, sexo, twitter, nacionalidade):
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO escritores (id, nome, idade, telefone, cpf, instagram, linkedin, sexo, twitter, nacionalidade) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (
            usuario_id, nome, idade, telefone, cpf, instagram, linkedin, sexo, twitter, nacionalidade
        ))
        mysql.connection.commit()
        cursor.close()

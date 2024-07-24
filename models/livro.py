from flask_mysql_connector import MySQL
from . import mysql

class LivroModel:
    @staticmethod
    def adicionar_livro(titulo, idioma, quantidade_paginas, pais, sinopse, status, genero, escritor_id):
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO livros (titulo, idioma, quantidade_paginas, pais, sinopse, status, genero, escritor_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', (
            titulo, idioma, quantidade_paginas, pais, sinopse, status, genero, escritor_id
        ))
        mysql.connection.commit()
        livro_id = cursor.lastrowid
        cursor.close()
        return livro_id

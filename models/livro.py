from flask_mysql_connector import MySQL
from . import mysql

class LivroModel:
    @staticmethod
    def adicionar_livro(titulo, idioma, QuantPaginas, pais, descricao, capaLivro, idEscritor,status):
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO livros (titulo, idioma, QuantPaginas, pais, descricao, capaLivro, idEscritor,status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', (
            titulo, idioma, QuantPaginas, pais, descricao, capaLivro, idEscritor,status
        ))
        mysql.connection.commit()
        livro_id = cursor.lastrowid
        cursor.close()
        return livro_id

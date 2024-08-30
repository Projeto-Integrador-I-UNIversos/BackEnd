class FavoritosModel:
    def __init__(self, mysql):
        self.mysql = mysql

    def favoritar_escritor(self, idEditora, idEscritor):
        with self.mysql.connection.cursor() as cursor:
            cursor.execute(
                'INSERT INTO tb_favoritos_escritores (idEditora, idEscritor) VALUES (%s, %s)',
                (idEditora, idEscritor)
            )
            self.mysql.connection.commit()

    def favoritar_livro(self, idEditora, idLivro):
        with self.mysql.connection.cursor() as cursor:
            cursor.execute(
                'INSERT INTO tb_favoritos_livros (idEditora, idLivro) VALUES (%s, %s)',
                (idEditora, idLivro)
            )
            self.mysql.connection.commit()

    def favoritar_editora(self, idEscritor, idEditora):
        with self.mysql.connection.cursor() as cursor:
            cursor.execute(
                'INSERT INTO tb_favoritos_editoras (idEscritor, idEditora) VALUES (%s, %s)',
                (idEscritor, idEditora)
            )
            self.mysql.connection.commit()

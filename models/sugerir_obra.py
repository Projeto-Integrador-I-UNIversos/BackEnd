class SugerirObra:
    def __init__(self, mysql):
        self.mysql = mysql

    def sugerir_obra(self, dados):
        with self.mysql.connection.cursor() as cursor:
            cursor.execute(
                'INSERT INTO tb_sugerirobra (idEditora, idLivro) VALUES (%s, %s)',
                (dados['idEditora'], dados['idLivro'])
            )
            self.mysql.connection.commit()
        return cursor.lastrowid

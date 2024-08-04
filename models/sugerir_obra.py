class SugerirObra:
    def __init__(self, mysql):
        self.mysql = mysql

    def criar_sugestao(self, dados):
        with self.mysql.connection.cursor() as cursor:
            cursor.execute(
                'INSERT INTO tb_sugerirobra (idEditora, idLivro, data) VALUES (%s, %s, %s)',
                (dados['idEditora'], dados['idLivro'], dados['data'])
            )
            self.mysql.connection.commit()
        return cursor.lastrowid

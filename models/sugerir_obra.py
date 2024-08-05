class SugerirObra:
    def __init__(self, mysql):
        self.mysql = mysql

    def sugerir_obra(self, dados):
        with self.mysql.connection.cursor() as cursor:
            cursor.execute(
                'INSERT INTO tb_sugerir_obra (idEditora, idObra) VALUES (%s, %s)',
                (dados['idEditora'], dados['idObra'])
            )
            self.mysql.connection.commit()
        return cursor.lastrowid

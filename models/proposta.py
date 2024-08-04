class Proposta:
    def __init__(self, mysql):
        self.mysql = mysql

    def criar_proposta(self, dados):
        with self.mysql.connection.cursor() as cursor:
            cursor.execute(
                'INSERT INTO tb_proposta (data, idEditora, idObra) VALUES (%s, %s, %s)',
                (dados['data'], dados['idEditora'], dados['idObra'])
            )
            self.mysql.connection.commit()
        return cursor.lastrowid

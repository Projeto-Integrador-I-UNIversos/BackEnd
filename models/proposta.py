class Proposta:
    def __init__(self, mysql):
        self.mysql = mysql

    def criar_proposta(self, dados):
        with self.mysql.connection.cursor() as cursor:
            cursor.execute(
                'INSERT INTO tb_proposta (data, idEditora, idLivro, idEscritor) VALUES (%s, %s, %s, %s)',
                (dados['data'], dados['idEditora'], dados['idLivro'], dados['idEscritor'])
            )
            self.mysql.connection.commit()
        return cursor.lastrowid

    def buscar_proposta_por_id(self, idProposta):
        with self.mysql.connection.cursor(dictionary=True) as cursor:
            cursor.execute('SELECT * FROM tb_proposta WHERE idProposta = %s', (idProposta,))
            return cursor.fetchone()

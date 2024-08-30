class Chat:
    def __init__(self, mysql):
        self.mysql = mysql

    def criar_chat(self, dados):
        with self.mysql.connection.cursor() as cursor:
            cursor.execute(
                'INSERT INTO tb_chat (idProposta, mensagem, dataInicio) VALUES (%s, %s, %s)',
                (dados['idProposta'], dados['mensagem'], dados['dataInicio'])
            )
            self.mysql.connection.commit()
        return cursor.lastrowid

    def buscar_chat_por_id(self, idChat):
        with self.mysql.connection.cursor(dictionary=True) as cursor:
            cursor.execute('SELECT * FROM tb_chat WHERE idChat = %s', (idChat,))
            return cursor.fetchone()

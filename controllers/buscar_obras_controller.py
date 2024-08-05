from models.livro import Livro

class BuscarObrasController:
    def __init__(self, mysql):
        self.model = Livro(mysql)

    def buscar_obras(self, criterios):
        with self.model.mysql.connection.cursor(dictionary=True) as cursor:
            query = 'SELECT * FROM tb_livro WHERE TRUE'
            params = []

            if 'tipo' in criterios:
                query += ' AND tipo = %s'
                params.append(criterios['tipo'])

            if 'genero' in criterios:
                query += '''
                AND EXISTS (
                    SELECT 1 FROM tb_generolivro gl 
                    JOIN tb_genero g ON gl.idGenero = g.idGenero 
                    WHERE gl.idLivro = tb_livro.idLivro 
                    AND g.nomeGenero = %s
                )
                '''
                params.append(criterios['genero'])

            if 'palavras_chave' in criterios:
                query += ' AND (titulo LIKE %s OR descricao LIKE %s)'
                keyword = f"%{criterios['palavras_chave']}%"
                params.extend([keyword, keyword])

            cursor.execute(query, params)
            return cursor.fetchall()

from models.escritor import Escritor
from models.livro import Livro

class ConsultarEscritoresController:
    def __init__(self, mysql):
        self.escritor_model = Escritor(mysql)
        self.livro_model = Livro(mysql)

    def buscar_escritores(self, criterios):
        with self.escritor_model.mysql.connection.cursor(dictionary=True) as cursor:
            query = 'SELECT * FROM tb_escritor WHERE TRUE'
            params = []

            if 'nome' in criterios:
                query += ' AND nome LIKE %s'
                params.append(f"%{criterios['nome']}%")

            cursor.execute(query, params)
            escritores = cursor.fetchall()

            for escritor in escritores:
                escritor['obras'] = self.livro_model.buscar_livros_por_escritor(escritor['idEscritor'])

            return escritores

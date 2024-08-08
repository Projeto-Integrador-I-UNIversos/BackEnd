from models.livro import Livro

class LivroController:
    def __init__(self, mysql):
        self.model = Livro(mysql)

    def adicionar_livro(self, dados):
        return self.model.criar_livro(dados)

    def buscar_livros_por_escritor(self, idEscritor):
        return self.model.buscar_livros_por_escritor(idEscritor)

    def editar_livro(self, idLivro, dados):
        return self.model.atualizar_livro(idLivro, dados)

    def deletar_livro(self, idLivro):
        return self.model.deletar_livro(idLivro)

    def listar_todos_livros(self):
        with self.mysql.connection.cursor() as cursor:
            cursor.execute('SELECT * FROM tb_livro')
            livros = cursor.fetchall()
        return livros
class Livro:
    def __init__(self, mysql):
        self.mysql = mysql

    def criar_livro(self, dados):
        with self.mysql.connection.cursor() as cursor:
            cursor.execute(
                'INSERT INTO tb_livro (titulo, idioma, QuantPaginas, pais, descricao, capaLivro, idEscritor, status, PdfLivro) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
                (dados['titulo'], dados['idioma'], dados['QuantPaginas'], dados['pais'], dados['descricao'], dados['capaLivro'], dados['idEscritor'], dados['status'], dados['PdfLivro'])
            )
            self.mysql.connection.commit()
        return cursor.lastrowid

    def buscar_livro_por_escritor(self, idEscritor):
        with self.mysql.connection.cursor(dictionary=True) as cursor:
            cursor.execute('SELECT * FROM tb_livro WHERE idEscritor = %s', (idEscritor,))
            return cursor.fetchall()

    def buscar_livro_por_id(self, idLivro):
        with self.mysql.connection.cursor(dictionary=True) as cursor:
            cursor.execute('SELECT * FROM tb_livro WHERE idLivro = %s', (idLivro,))
            return cursor.fetchone()

    def atualizar_livro(self, idLivro, dados):
        with self.mysql.connection.cursor() as cursor:
            cursor.execute(
                'UPDATE tb_livro SET titulo = %s, idioma = %s, QuantPaginas = %s, pais = %s, descricao = %s, capaLivro = %s, status = %s, PdfLivro = %s WHERE idLivro = %s',
                (dados['titulo'], dados['idioma'], dados['QuantPaginas'], dados['pais'], dados['descricao'], dados['capaLivro'], dados['status'], dados['PdfLivro'], idLivro)
            )
            self.mysql.connection.commit()
        return cursor.rowcount > 0

    def deletar_livro(self, idLivro):
        with self.mysql.connection.cursor() as cursor:
            cursor.execute('DELETE FROM tb_livro WHERE idLivro = %s', (idLivro,))
            self.mysql.connection.commit()
        return cursor.rowcount > 0

    def listar_todos_livros(self):
        with self.mysql.connection.cursor() as cursor:
            cursor.execute('SELECT * FROM tb_livro')
            livros = cursor.fetchall()
        return livros
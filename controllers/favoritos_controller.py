from models.favoritos import FavoritosModel

class FavoritosController:
    def __init__(self, mysql):
        self.model = FavoritosModel(mysql)

    def favoritar_escritor(self, idEditora, idEscritor):
        return self.model.favoritar_escritor(idEditora, idEscritor)

    def favoritar_livro(self, idEditora, idLivro):
        return self.model.favoritar_livro(idEditora, idLivro)

    def favoritar_editora(self, idEscritor, idEditora):
        return self.model.favoritar_editora(idEscritor, idEditora)

class ObraView:
    def mostrar_dados(self, obra):
        print("Título da obra:", obra.titulo)
        print("Autor:", obra.autor.nome)
        print("Tipo:", obra.tipo)
        print("Gênero:", obra.genero)
        print("Sinopse:", obra.sinopse)

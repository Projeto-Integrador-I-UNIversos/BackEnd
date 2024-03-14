from Model.obra import Obra
from View.obra_view import ObraView

class ObraController:
    def cadastrar_obra(self, titulo, autor, tipo, genero, sinopse):
        obra = Obra(titulo, autor, tipo, genero, sinopse)
        view = ObraView()
        view.mostrar_dados(obra)

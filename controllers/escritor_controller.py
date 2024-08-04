from models.escritor import Escritor

class EscritorController:
    def __init__(self, mysql):
        self.model = Escritor(mysql)

    def cadastrar_escritor(self, dados):
        return self.model.criar_escritor(dados)

    def buscar_escritor_por_usuario(self, idUsuario):
        return self.model.buscar_escritor_por_usuario(idUsuario)

    def editar_escritor(self, idEscritor, dados):
        return self.model.atualizar_escritor(idEscritor, dados)

    def deletar_escritor(self, idEscritor):
        return self.model.deletar_escritor(idEscritor)

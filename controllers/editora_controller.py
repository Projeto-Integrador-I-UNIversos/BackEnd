from models.editora import Editora

class EditoraController:
    def __init__(self, mysql):
        self.model = Editora(mysql)

    def cadastrar_editora(self, dados):
        return self.model.criar_editora(dados)

    def buscar_editora_por_usuario(self, idUsuario):
        return self.model.buscar_editora_por_usuario(idUsuario)

    def editar_editora(self, idEditora, dados):
        return self.model.atualizar_editora(idEditora, dados)

    def deletar_editora(self, idEditora):
        return self.model.deletar_editora(idEditora)

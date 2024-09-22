from models.editora import Editora

class EditoraController:
    def __init__(self, mysql):
        self.mysql = mysql
        self.model = Editora(mysql)

    def cadastrar_editora(self, dados):
        return self.model.criar_editora(dados)

    def buscar_editora_por_usuario(self, idUsuario):
        return self.model.buscar_editora_por_usuario(idUsuario)

    def editar_editora(self, idUsuario, dados):
        return self.model.atualizar_editora(idUsuario, dados)

    def deletar_editora(self, idUsuario):
        return self.model.deletar_editora(idUsuario)
    
    def listar_todos_editoras(self):
        return self.model.listar_todos_editoras()

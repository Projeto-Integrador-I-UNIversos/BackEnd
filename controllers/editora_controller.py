from models.editora import Editora

class EditoraController:
    def __init__(self, mysql):
        self.mysql = mysql
        self.model = Editora(mysql)

    def cadastrar_editora(self, dados):
        # Valida e cadastra uma nova editora
        return self.model.criar_editora(dados)

    def buscar_editora_por_usuario(self, idUsuario):
        # Busca uma editora pelo ID do usuário
        return self.model.buscar_editora_por_usuario(idUsuario)

    def editar_editora(self, idUsuario, dados):
        # Atualiza os dados de uma editora
        return self.model.atualizar_editora(idUsuario, dados)

    def deletar_editora(self, idUsuario):
        # Deleta uma editora
        return self.model.deletar_editora(idUsuario)
    
    def listar_todos_editoras(self):
        # Lista todas as editoras
        return self.model.listar_todos_editoras()

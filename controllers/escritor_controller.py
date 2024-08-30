from models.escritor import Escritor

class EscritorController:
    def __init__(self, mysql):
        self.mysql = mysql
        self.model = Escritor(mysql)

    def cadastrar_escritor(self, dados):
        # Valida e cadastra um novo escritor
        return self.model.criar_escritor(dados)

    def buscar_escritor_por_usuario(self, idUsuario):
        # Busca um escritor pelo ID do usuário
        return self.model.buscar_escritor_por_usuario(idUsuario)

    def editar_escritor(self, idUsuario, dados):
        # Atualiza os dados de um escritor
        return self.model.atualizar_escritor(idUsuario, dados)

    def deletar_escritor(self, idUsuario):
        # Deleta um escritor
        return self.model.deletar_escritor(idUsuario)
    
    def listar_todos_escritores(self):
        # Lista todos os escritores
        return self.model.listar_todos_escritores()

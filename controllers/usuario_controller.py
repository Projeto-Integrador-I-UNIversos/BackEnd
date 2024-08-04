from models.usuario import UsuarioModel

class UsuarioController:
    def __init__(self, mysql):
        self.mysql = mysql

    def criar_usuario(self, email, senha, tipo):
        return UsuarioModel.criar_usuario(email, senha, tipo)

    def buscar_usuario_por_email(self, email):
        return UsuarioModel.buscar_usuario_por_email(email)

    def buscar_usuario_por_id(self, idUsuario):
        return UsuarioModel.buscar_usuario_por_id(idUsuario)

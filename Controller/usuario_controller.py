from Model.usuario import Usuario
from View.usuario_view import UsuarioView

class UsuarioController:
    def cadastrar_usuario(self, nome, email, senha):
        usuario = Usuario(nome, email, senha)
        view = UsuarioView()
        view.mostrar_dados(usuario)

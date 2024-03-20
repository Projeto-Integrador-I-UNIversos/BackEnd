from Controller.usuario_controller import UsuarioController
from Controller.obra_controller import ObraController


if __name__ == "__main__":
    # Criar um usuário
    usuario_controller = UsuarioController()
    usuario_controller.cadastrar_usuario("João", "joao@email.com", "senha123")

    # Criar uma obra
    obra_controller = ObraController()
    obra_controller.cadastrar_obra("Meu Livro", "João", "Romance", "Ficção", "Uma história emocionante...")

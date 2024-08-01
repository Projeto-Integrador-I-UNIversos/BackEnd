from werkzeug.security import generate_password_hash, check_password_hash
from models.usuario import UsuarioModel
from models.escritor import EscritorModel
from models.editora import EditoraModel

class UsuarioController:
    @staticmethod
    def cadastrar_usuario(data):
        email = data['email']
        senha = generate_password_hash(data['senha'])
        tipo = data['tipo']

        # Criação de editora ou escritor com base no tipo de usuário
        if tipo == 'editora':
            EditoraModel.criar_editora(
                idUsuario,
                data.get('nome_fantasia'),
                data.get('cnpj'),
                data.get('telefone'),
                data.get('linkedin'),
                data.get('site_institucional'),
                data.get('twitter'),
                data.get('instagram'),
                data.get('pais'),
                data.get('descricao')
            )
        elif tipo == 'escritor':
            EscritorModel.criar_escritor(
                idUsuario,
                data.get('nome'),
                data.get('idade'),
                data.get('telefone'),
                data.get('cpf'),
                data.get('instagram'),
                data.get('linkedin'),
                data.get('sexo'),
                data.get('twitter'),
                data.get('nacionalidade')
            )
            
            idUsuario = UsuarioModel.criar_usuario(email, senha, tipo)
        
        return idUsuario

    @staticmethod
    def autenticar_usuario(email, senha):
        usuario = UsuarioModel.buscar_usuario_por_email(email)
        if usuario and check_password_hash(usuario['senha'], senha):
            return usuario
        return None

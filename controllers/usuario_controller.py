from models.usuario import UsuarioModel
from models.escritor import Escritor
from models.editora import Editora
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
import jwt

class UsuarioController:
    def __init__(self, mysql):
        self.mysql = mysql
        self.usuario_model = UsuarioModel(mysql)
        self.escritor_model = Escritor(mysql)
        self.editora_model = Editora(mysql)
        self.secret_key = 'admin'

    def criar_usuario(self, dados):
        senha_hash = generate_password_hash(dados['senha'])
        idUsuario = self.usuario_model.criar_usuario(dados['email'], senha_hash, dados['tipo'])
        
        if dados['tipo'] == 'escritor':
            dados_escritor = dados.get('escritor_dados', {})
            if not dados_escritor:
                raise ValueError("Dados do escritor não fornecidos")
            
            if 'dataNasc' in dados_escritor:
                dados_escritor['dataNasc'] = self.converter_data_para_iso(dados_escritor['dataNasc'])
                
            dados_escritor['idUsuario'] = idUsuario
            self.escritor_model.criar_escritor(dados_escritor)
        
        elif dados['tipo'] == 'editora':
            dados_editora = dados.get('editora_dados', {})
            if not dados_editora:
                raise ValueError("Dados da editora não fornecidos")
            
            dados_editora['idUsuario'] = idUsuario
            self.editora_model.criar_editora(dados_editora)
        
        return idUsuario

    def converter_data_para_iso(self, data_ddmmaa):
        try:
            data_datetime = datetime.strptime(data_ddmmaa, '%d/%m/%Y')
            return data_datetime.strftime('%Y-%m-%d')
        except ValueError:
            raise ValueError("Data inválida. O formato deve ser dd/mm/aaaa.")

    def buscar_usuario_por_email(self, email):
        return self.usuario_model.buscar_usuario_por_email(email)

    def buscar_usuario_por_id(self, idUsuario):
        return self.usuario_model.buscar_usuario_por_id(idUsuario)
    
    def listar_todos_usuarios(self):
        return self.usuario_model.listar_todos_usuarios()

    def deletar_usuario(self, idUsuario):
        usuario = self.usuario_model.buscar_usuario_por_id(idUsuario)
        if usuario:
            if usuario['tipo'] == 'escritor':
                self.escritor_model.deletar_escritor(idUsuario)
            elif usuario['tipo'] == 'editora':
                self.editora_model.deletar_editora(idUsuario)
            return self.usuario_model.deletar_usuario(idUsuario)
        return False

    def atualizar_usuario(self, idUsuario, dados):
        usuario = self.usuario_model.buscar_usuario_por_id(idUsuario)
        if usuario:
            if self.usuario_model.atualizar_usuario(idUsuario, dados['usuario']):
                if usuario['tipo'] == 'escritor':
                    if 'escritor_dados' in dados:
                        self.escritor_model.atualizar_escritor(idUsuario, dados['escritor_dados'])
                elif usuario['tipo'] == 'editora':
                    if 'editora_dados' in dados:
                        self.editora_model.atualizar_editora(idUsuario, dados['editora_dados'])
                return True
        return False
    
    def login(self, email, senha):
        usuario = self.usuario_model.buscar_usuario_por_email(email)
        if usuario and check_password_hash(usuario['senha'], senha):
            token = self.gerar_token(usuario['idUsuario'])
            return True, token
        return False, None

    def gerar_token(self, user_id):
        payload = {
            'user_id': user_id,
            'exp': datetime.utcnow() + timedelta(hours=1)
        }
        return jwt.encode(payload, self.secret_key, algorithm='HS256')

from models.chat import Chat

class ChatController:
    def __init__(self, mysql):
        self.model = Chat(mysql)

    def enviar_proposta(self, dados):
        return self.model.criar_chat(dados)
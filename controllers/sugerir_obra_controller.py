from models.sugerir_obra import SugerirObra

class SugerirObraController:
    def __init__(self, mysql):
        self.model = SugerirObra(mysql)

    def sugerir_obra(self, dados):
        return self.model.criar_sugestao(dados)

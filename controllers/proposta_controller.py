from models.proposta import Proposta

class PropostaController:
    def __init__(self, mysql):
        self.model = Proposta(mysql)

    def enviar_proposta(self, dados):
        return self.model.criar_proposta(dados)

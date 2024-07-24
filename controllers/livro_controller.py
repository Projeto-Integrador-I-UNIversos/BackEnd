from models.livro import LivroModel
from models.proposta import PropostaModel

class LivroController:
    @staticmethod
    def adicionar_livro(data):
        livro_id = LivroModel.adicionar_livro(
            data['titulo'],
            data['idioma'],
            data['quantidade_paginas'],
            data['pais'],
            data['sinopse'],
            data['status'],
            data['genero'],
            data['escritor_id']
        )
        return livro_id

    @staticmethod
    def enviar_proposta(data):
        proposta_id = PropostaModel.enviar_proposta(
            data['livro_id'],
            data['usuario_origem'],
            data['usuario_destino'],
            data['mensagem']
        )
        return proposta_id

from . import mysql

class PropostaModel:
    @staticmethod
    def enviar_proposta(livro_id, usuario_origem, usuario_destino, mensagem):
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO propostas (livro_id, usuario_origem, usuario_destino, mensagem) VALUES (%s, %s, %s, %s)', (
            livro_id, usuario_origem, usuario_destino, mensagem
        ))
        mysql.connection.commit()
        proposta_id = cursor.lastrowid

        # Criar chat automaticamente
        cursor.execute('SELECT titulo FROM livros WHERE id = %s', (livro_id,))
        livro = cursor.fetchone()
        nome_livro = livro[0]
        numero_sequencial = f'CHAT-{proposta_id}'
        cursor.execute('INSERT INTO chats (proposta_id, numero_sequencial, nome_livro) VALUES (%s, %s, %s)', (
            proposta_id, numero_sequencial, nome_livro
        ))
        mysql.connection.commit()
        cursor.close()

        return proposta_id

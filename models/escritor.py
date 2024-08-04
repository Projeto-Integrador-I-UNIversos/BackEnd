class Escritor:
    def __init__(self, mysql):
        self.mysql = mysql

    def criar_escritor(self, dados):
        with self.mysql.connection.cursor() as cursor:
            cursor.execute(
                'INSERT INTO tb_escritor (nome, dataNasc, telefone, cpf, instagram, linkedin, sexo, twitter, nacionalidade, idUsuario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                (dados['nome'], dados['dataNasc'], dados['telefone'], dados['cpf'], dados['instagram'], dados['linkedin'], dados['sexo'], dados['twitter'], dados['nacionalidade'], dados['idUsuario'])
            )
            self.mysql.connection.commit()
        return cursor.lastrowid

    def buscar_escritor_por_usuario(self, idUsuario):
        with self.mysql.connection.cursor(dictionary=True) as cursor:
            cursor.execute('SELECT * FROM tb_escritor WHERE idUsuario = %s', (idUsuario,))
            return cursor.fetchone()

    def atualizar_escritor(self, idEscritor, dados):
        with self.mysql.connection.cursor() as cursor:
            cursor.execute(
                'UPDATE tb_escritor SET nome = %s, dataNasc = %s, telefone = %s, cpf = %s, instagram = %s, linkedin = %s, sexo = %s, twitter = %s, nacionalidade = %s WHERE idEscritor = %s',
                (dados['nome'], dados['dataNasc'], dados['telefone'], dados['cpf'], dados['instagram'], dados['linkedin'], dados['sexo'], dados['twitter'], dados['nacionalidade'], idEscritor)
            )
            self.mysql.connection.commit()
        return cursor.rowcount > 0

    def deletar_escritor(self, idEscritor):
        with self.mysql.connection.cursor() as cursor:
            cursor.execute('DELETE FROM tb_escritor WHERE idEscritor = %s', (idEscritor,))
            self.mysql.connection.commit()
        return cursor.rowcount > 0

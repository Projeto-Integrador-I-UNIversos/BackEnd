class Editora:
    def __init__(self, mysql):
        self.mysql = mysql

    def criar_editora(self, dados):
        with self.mysql.connection.cursor() as cursor:
            cursor.execute(
                'INSERT INTO tb_editora (nome, cnpj, telefone, linkedin, siteInstitucional, twitter, instagram, pais, descricao, idUsuario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                (dados['nome'], dados['cnpj'], dados['telefone'], dados['linkedin'], dados['siteInstitucional'], dados['twitter'], dados['instagram'], dados['pais'], dados['descricao'], dados['idUsuario'])
            )
            self.mysql.connection.commit()
        return cursor.lastrowid

    def buscar_editora_por_usuario(self, idUsuario):
        with self.mysql.connection.cursor(dictionary=True) as cursor:
            cursor.execute('SELECT * FROM tb_editora WHERE idUsuario = %s', (idUsuario,))
            return cursor.fetchone()

    def atualizar_editora(self, idEditora, dados):
        with self.mysql.connection.cursor() as cursor:
            cursor.execute(
                'UPDATE tb_editora SET nome = %s, cnpj = %s, telefone = %s, linkedin = %s, siteInstitucional = %s, twitter = %s, instagram = %s, pais = %s, descricao = %s WHERE idEditora = %s',
                (dados['nome'], dados['cnpj'], dados['telefone'], dados['linkedin'], dados['siteInstitucional'], dados['twitter'], dados['instagram'], dados['pais'], dados['descricao'], idEditora)
            )
            self.mysql.connection.commit()
        return cursor.rowcount > 0

    def deletar_editora(self, idEditora):
        with self.mysql.connection.cursor() as cursor:
            cursor.execute('DELETE FROM tb_editora WHERE idEditora = %s', (idEditora,))
            self.mysql.connection.commit()
        return cursor.rowcount > 0

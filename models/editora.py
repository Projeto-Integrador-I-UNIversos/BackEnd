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
    
    def buscar_editora_por_id(self, idUsuario):
        with self.mysql.connection.cursor(dictionary=True) as cursor:
            cursor.execute(
                'SELECT * FROM tb_editora WHERE idUsuario = %s',
                (idUsuario,)
            )
            return cursor.fetchone()

    def deletar_editora(self, idUsuario):
        with self.mysql.connection.cursor() as cursor:
            cursor.execute(
                'DELETE FROM tb_editora WHERE idUsuario = %s',
                (idUsuario,)
            )
            self.mysql.connection.commit()

    def atualizar_editora(self, idUsuario, dados):
        set_clause = ', '.join([f"{key} = %s" for key in dados.keys()])
        values = list(dados.values())
        values.append(idUsuario)
        query = f'UPDATE tb_editora SET {set_clause} WHERE idUsuario = %s'
        
        with self.mysql.connection.cursor() as cursor:
            cursor.execute(query, values)
            self.mysql.connection.commit()
            return cursor.rowcount > 0
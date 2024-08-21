class Editora:

    def __init__(self, mysql):
        self.mysql = mysql

    def criar_editora(self, dados):
        required_keys = ['nome', 'cnpj', 'telefone', 'linkedin', 'siteInstitucional', 'twitter', 'instagram', 'pais', 'descricao', 'idUsuario']
        for key in required_keys:
            if key not in dados:
                raise ValueError(f"Faltando chave obrigatória: {key}")

        with self.mysql.connection.cursor() as cursor:
            cursor.execute(
                'INSERT INTO tb_editora (nome, cnpj, telefone, linkedin, siteInstitucional, twitter, instagram, pais, descricao, idUsuario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                (dados['nome'], dados['cnpj'], dados['telefone'], dados['linkedin'], dados['siteInstitucional'], dados['twitter'], dados['istagram'], dados['pais'], dados['descricao'], dados['idUsuario'])
            )
            self.mysql.connection.commit()
            return cursor.lastrowid
    
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
        
    def listar_todos_editoras(self):
        try:
            with self.mysql.connection.cursor(dictionary=True) as cursor:
                cursor.execute('SELECT * FROM tb_editora')
                editoras = cursor.fetchall()
            return editoras
        except Exception as e:
            print(f"Erro ao listar todas as editoras: {e}")
            return []

    def buscar_por_cnpj(self, cnpj):
        with self.mysql.connection.cursor(dictionary=True) as cursor:
            cursor.execute('SELECT * FROM tb_editora WHERE cnpj = %s', (cnpj,))
            return cursor.fetchone()

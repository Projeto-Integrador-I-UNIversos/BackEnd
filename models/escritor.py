class Escritor:

    def __init__(self, mysql):
        self.mysql = mysql

    def criar_escritor(self, dados):
        required_keys = ['nome', 'dataNasc', 'telefone', 'cpf', 'instagram', 'linkedin', 'sexo', 'twitter', 'nacionalidade', 'idUsuario']
        for key in required_keys:
            if key not in dados:
                raise ValueError(f"Faltando chave obrigatória: {key}")

        with self.mysql.connection.cursor() as cursor:
            cursor.execute(
                'INSERT INTO tb_escritor (nome, dataNasc, telefone, cpf, instagram, linkedin, sexo, twitter, nacionalidade, idUsuario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                (dados['nome'], dados['dataNasc'], dados['telefone'], dados['cpf'], dados['instagram'], dados['linkedin'], dados['sexo'], dados['twitter'], dados['nacionalidade'], dados['idUsuario'])
            )
            self.mysql.connection.commit()
            return cursor.lastrowid
    
    def deletar_escritor(self, idUsuario):
        with self.mysql.connection.cursor() as cursor:
            cursor.execute(
                'DELETE FROM tb_escritor WHERE idUsuario = %s',
                (idUsuario,)
            )
            self.mysql.connection.commit()

    def atualizar_escritor(self, idUsuario, dados):
        set_clause = ', '.join([f"{key} = %s" for key in dados.keys()])
        values = list(dados.values())
        values.append(idUsuario)
        query = f'UPDATE tb_escritor SET {set_clause} WHERE idUsuario = %s'
        
        with self.mysql.connection.cursor() as cursor:
            cursor.execute(query, values)
            self.mysql.connection.commit()
            return cursor.rowcount > 0
        
    def listar_todos_escritores(self):
        try:
            with self.mysql.connection.cursor(dictionary=True) as cursor:
                cursor.execute('SELECT * FROM tb_escritor')
                escritores = cursor.fetchall()
            return escritores
        except Exception as e:
            print(f"Erro ao listar todos os escritores: {e}")
            return []

    def buscar_escritor_por_usuario(self, idUsuario):
        with self.mysql.connection.cursor(dictionary=True) as cursor:
            cursor.execute('SELECT * FROM tb_escritor WHERE idUsuario = %s', (idUsuario,))
            return cursor.fetchone()

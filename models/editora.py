from . import mysql

class EditoraModel:
    @staticmethod
    def criar_editora(usuario_id, nome_fantasia, cnpj, telefone, linkedin, site_institucional, twitter, instagram, pais, descricao):
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO editoras (id, nome_fantasia, cnpj, telefone, linkedin, site_institucional, twitter, instagram, pais, descricao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (
            usuario_id, nome_fantasia, cnpj, telefone, linkedin, site_institucional, twitter, instagram, pais, descricao
        ))
        mysql.connection.commit()
        cursor.close()

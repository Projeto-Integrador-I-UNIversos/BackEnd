import mysql.connector

# Conectar ao banco de dados MySQL
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="admin",
    password="admin",
    database="universos_literarios"
)

def criar_tabelas():
    # Criar um cursor
    cursor = conn.cursor()

    # Definir o comando SQL para criar a tabela de usuário
    create_user_table_query = """
    CREATE TABLE IF NOT EXISTS tb_usuario(
        idUsuario INT AUTO_INCREMENT PRIMARY KEY,
        email VARCHAR(45) NOT NULL UNIQUE, 
        senha VARCHAR(45) NOT NULL,
        tipo VARCHAR(45) NOT NULL
    );
    """

    # Definir o comando SQL para criar a tabela de admin
    create_admin_table_query = """
    CREATE TABLE IF NOT EXISTS tb_Admin(
        idAdmin INT AUTO_INCREMENT PRIMARY KEY,
        idUsuario INT,
        FOREIGN KEY (idUsuario) REFERENCES tb_usuario(idUsuario)
    );
    """

    # Executar comandos de criação de tabela
    cursor.execute(create_user_table_query)
    cursor.execute(create_admin_table_query)

    # Fechar o cursor
    cursor.close()
"""
def deletar_usuario(idUsuario):
    try:
        # Criar um cursor
        cursor = conn.cursor()

        # Definir a consulta SQL para deletar o usuário
        delete_query = "DELETE FROM tb_Usuario WHERE idUsuario = %s"

        # Executar a consulta
        cursor.execute(delete_query, (idUsuario,))

        # Confirmar a transação
        conn.commit()

        print(f"Usuário com ID {idUsuario} deletado com sucesso.")
        
    except mysql.connector.Error as err:
        print(f"Erro ao deletar usuário: {err}")

    finally:
        # Fechar o cursor
        cursor.close()

# Criar as tabelas se não existirem
criar_tabelas()

# Exemplo de uso da função de deletar
deletar_usuario(1)
"""
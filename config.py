import mysql.connector

# Conectar ao banco de dados MySQL
conn = mysql.connector.connect(
    host= "127.0.0.1",
    user="lara",
    password="LaraVictoria123_@;",
    database="universos_literarios"
)

# Criar um cursor
cursor = conn.cursor()

# Definir o comando SQL para criar uma tabela
create_table_query = """
CREATE TABLE IF NOT EXISTS tb_Usuario(
    idUsuario INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(45) NOT NULL UNIQUE, 
    senha VARCHAR(45) NOT NULL,
    tipo VARCHAR(45) NOT NULL
);
"""
create_table_query = """
CREATE TABLE IF NOT EXISTS tb_Admin(
    idAdmin INT AUTO_INCREMENT PRIMARY KEY,
    idUsuario INT,
    FOREIGN KEY (idUsuario) REFERENCES tb_Usuario(idUsuario)
);
"""

connection = mysql.connector.connect(
    host= "127.0.0.1",
    user="lara",
    password="LaraVictoria123_@;",
    database="universos_literarios"
)

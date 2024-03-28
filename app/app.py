from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# Conectar ao banco de dados MySQL
conn = mysql.connector.connect(
    host= "127.0.0.1",
    user="root",
    password="root",
    database="universos_literarios"
)

# Função para buscar um usuário pelo ID
def find_user_by_id(user_id):
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    return user

@app.route("/Login", methods=['GET'])
def login():
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT email FROM usuarios")
    usernames = [user["email"] for user in cursor.fetchall()]
    cursor.close()
    return jsonify({"usuarios": usernames})

@app.route('/Cadastro', methods=['POST'])
def cadastro():
    data = request.json
    email = data['email']
    senha = data['senha']
    tipo = data['tipo']

    cursor = conn.cursor()
    # Inserir o usuário no banco
    cursor.execute("INSERT INTO usuarios (email, senha, tipo) VALUES (%s, %s, %s)", (email, senha, tipo))
    conn.commit()
    cursor.close()
    return jsonify({"status": "success", "message": "Usuário cadastrado com sucesso!"})

if __name__ == "__main__":
    app.run(port=8000)

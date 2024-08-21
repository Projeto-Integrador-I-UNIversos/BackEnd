from flask import Flask
from flask_cors import CORS
from models import db_init
from views.usuario_view import usuario_bp
from views.livro_view import livro_bp
from views.editora_view import editora_bp
from views.escritor_view import escritor_bp
from views.buscar_obras_view import buscar_obras_bp
from views.consultar_escritores_view import consultar_escritores_bp
from views.proposta_view import proposta_bp
from views.sugerir_obra_view import sugerir_obra_bp

app = Flask(__name__)

# Configuração do CORS
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

# Inicializa o banco de dados
db_init(app)

# Registra os blueprints
app.register_blueprint(usuario_bp)
app.register_blueprint(livro_bp)
app.register_blueprint(editora_bp)
app.register_blueprint(escritor_bp)
app.register_blueprint(buscar_obras_bp)
app.register_blueprint(consultar_escritores_bp)
app.register_blueprint(proposta_bp)
app.register_blueprint(sugerir_obra_bp)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
    return response

if __name__ == "__main__":
    app.run(debug=True)

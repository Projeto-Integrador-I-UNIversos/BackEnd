from flask import Flask
from flask_cors import CORS
from models import db_init
from views.usuario_view import usuario_bp
from views.livro_view import livro_bp

app = Flask(__name__)

# Inicializa o CORS permitindo todas as origens
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

# Inicializa a conexão MySQL
db_init(app)

# Registra os blueprints
app.register_blueprint(usuario_bp, url_prefix='/usuario')
app.register_blueprint(livro_bp, url_prefix='/livro')

if __name__ == '__main__':
    app.run(debug=True, port=5000)

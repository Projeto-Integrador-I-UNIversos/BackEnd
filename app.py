from flask import Flask
from config import Config
from models import __init__
from views.usuario_view import usuario_bp
from views.livro_view import livro_bp

app = Flask(__name__)
app.config.from_object(Config)

# Inicializa a conexão MySQL
__init__(app)

# Registra os blueprints
app.register_blueprint(usuario_bp, url_prefix='/usuario')
app.register_blueprint(livro_bp, url_prefix='/livro')

if __name__ == '__main__':
    app.run(debug=True)

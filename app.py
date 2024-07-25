from flask import Flask
from flask_cors import CORS
from models import __init__
from views.usuario_view import usuario_bp
from views.livro_view import livro_bp
from flask_mysql_connector import MySQL

app = Flask(__name__)
#app.config.from_object(Config)
CORS(app)
# Inicializa a conexão MySQL
__init__(app)

mysql = MySQL(app)

# Registra os blueprints
app.register_blueprint(usuario_bp, url_prefix='/usuario')
app.register_blueprint(livro_bp, url_prefix='/livro')

if __name__ == '__main__':
    app.run(debug=True)

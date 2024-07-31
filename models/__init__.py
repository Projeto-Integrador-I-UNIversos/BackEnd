from flask_mysql_connector import MySQL

mysql = MySQL()

def db_init(app):
    # Configurações do MySQL
    app.config['MYSQL_USER'] = 'admin'
    app.config['MYSQL_PASSWORD'] = 'admin'
    app.config['MYSQL_DATABASE'] = 'universos_literarios'
    app.config['MYSQL_HOST'] = 'localhost'  # host
    app.config['MYSQL_PORT'] = 3306         # porta

    # Inicializa o MySQL com as configurações fornecidas
    mysql.init_app(app)
from flask import Flask


def create_app(config_name):
    app = Flask(__name__)
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://elusuario:12345@localhost:5432/blacklist'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blacklist.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'no-hay-frase'
    app.config['PROPAGATE_EXCEPTIONS'] = True
    return app

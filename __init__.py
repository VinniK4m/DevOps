import os

from flask import Flask

hostname = os.environ['RDS_HOST']
user = os.environ['RDS_USERNAME']
password = os.environ['RDS_PASSWORD']
dbname = os.environ['RDS_DATABASE']


def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{hostname}/{dbname}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app

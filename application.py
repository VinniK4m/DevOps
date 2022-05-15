import os

from flask import request, Blueprint
from sqlalchemy.exc import NoResultFound, IntegrityError
import socket
from models import Email, db
from flask import Flask

hostname = os.environ['RDS_HOST']
user = os.environ['RDS_USERNAME']
password = os.environ['RDS_PASSWORD']
dbname = os.environ['RDS_DATABASE']


def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{hostname}/{dbname}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.register_blueprint(Blueprint('main', __name__, url_prefix='/'))
    return app


application = create_app('application')
app_context = application.app_context()
app_context.push()

db.init_app(application)

db.create_all()


@application.route('/')
def main():
    return 'DevOps'


def authorized(sesion_id):
    sesion_base = '123456789'
    if sesion_base == sesion_id:
        return True
    return False


@application.route('/blacklists/', methods=['POST'])
def insert_email():
    def extract_ip():
        st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            st.connect(('10.255.255.255', 1))
            IP = st.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            st.close()
        return IP

    sesion_id = request.headers.get('Authorization')
    if not authorized(sesion_id):
        return {"message": "Not authorized"}, 401
    email_new = Email(app_uuid=123456, email=request.json["email"], blocked_reason=request.json["blocked_reason"],
                      ip_client=extract_ip())
    try:
        db.session.add(email_new)
        db.session.commit()
    except IntegrityError:
        return {"message": "Email not created Integrity Error"}, 404
    return {"message": "Email created"}, 200


@application.route('/blacklists/<string:email>', methods=['GET'])
def find_email(email):
    sesion_id = request.headers.get('Authorization')
    if not authorized(sesion_id):
        return {"message": "Not authorized"}, 401
    try:
        db.session.query(Email).filter(Email.email == email).one()
        return {"message": "Found Email"}, 200
    except NoResultFound:
        return {"message": "El email no esta registrado en la lista negra"}, 404


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000, debug=True)

# Test
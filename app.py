from flask import request
from sqlalchemy.exc import NoResultFound, IntegrityError
from . import create_app
import socket
from models import Email, db

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)

db.create_all()


@app.route('/')
def main():
    return 'DevOps'


def authorized(sesion_id):
    sesion_base = '123456789'
    if sesion_base == sesion_id:
        return True
    return False


@app.route('/blacklists/', methods=['POST'])
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


@app.route('/blacklists/<string:email>', methods=['GET'])
def find_email(email):
    sesion_id = request.headers.get('Authorization')
    if not authorized(sesion_id):
        return {"message": "Not authorized"}, 401
    try:
        db.session.query(Email).filter(Email.email == email).one()
        return {"message": "Found Email"}, 200
    except NoResultFound:
        return {"message": "El email no esta registrado en la lista negra"}, 404

from flask import Flask, request
from sqlalchemy.exc import NoResultFound
import socket

from models import db, Email

app = Flask(__name__)
app_context = app.app_context()
app_context.push()

db.init_app(app)

db.create_all()


@app.route('/')
def main():
    return 'DevOps'

def authorized(sesion_id):
    sesion_base = 123456789
    if sesion_base == sesion_id:
        return True
    return False



@app.route('/blacklists/', methods=['POST'])
def insert_email():
    sesion_id = request.headers.get('Authorization')
    if not authorized(sesion_id):
        laIp = extract_ip()
        email_new = Email(app_uuid= 123456, email=request.json["email"], blocked_reason=request.json["blocked_reason"],
        ip_client=laIp)
        db.session.add(email_new)
        db.session.commit()
    return {"message": "Email create"}, 200


@app.route('/blacklists/<string:email>', methods=['GET'])
def find_email(email):
    try:
        result = db.session.query(Email).filter(Email.email == email).one()
    except NoResultFound:
        return {"message": "El email no esta registrado en la lista negra"}, 404
    return {"message": "Found Email"}, 200

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

    email_new = Email(app_uuid=123456, email=request.json["email"], blocked_reason=request.json["blocked_reason"],
                      ip_client=extract_ip())
    db.session.add(email_new)
    db.session.commit()
    return {"message": "Email create"}, 200


@app.route('/blacklists/<string:email>', methods=['GET'])
def find_email(email):
    try:
        db.session.query(Email).filter(Email.email == email).one()
    except NoResultFound:
        return {"message": "El email no esta registrado en la lista negra"}, 404
    return {"message": "Found Email"}, 200


if __name__ == '__main__':
    app.run(
        host="0.0.0.0", port=3000, debug=True
    )

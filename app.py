from flask import Flask
from models import db

app = Flask(__name__)


@app.route('/')
def main():
    return 'DevOps'


@app.route('/blacklists', methods=['POST'])
def insert_email():
    laIp = "127.0.0.1"
    email_new = Email(app_uuid= 123456, email=request.json["email"], blocked_reason=request.json["blocked_reason"],
    ip_client=laIp, date_create=request.json["date_create"])
    db.session.add(email_new)
    db.session.commit()
    return {"message": "Email create"}, 200


@app.route('/blacklists/<string:email>', methods=['GET'])
def find_email(email):
    return 'DevOps'


if __name__ == '__main__':
    app.run(
        host="0.0.0.0", port=3000, debug=True
    )

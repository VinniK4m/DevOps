from flask import Flask
#from .model import db

app = Flask(__name__)



@app.route('/')
def main():
    return 'DevOps'

@app.route('/blacklists', methods = ['POST'])
def insert_email():
    #laIp = request.json["ip"]
    #email_new = Email(email=request.json["email"], reason=request.json["reason"],
    #                  ip=laIp, fecha=request.json["fecha"])
    #db_connection.db.engine.execute(email_new)
    #db_connection.db.engine.execute.commit()
    return {"message": "Email create"}, 200


@app.route('/blacklists/<string:email>', methods = ['GET'])
def find_email(email):
    return 'DevOps'



if __name__ == '__main__':
    app.run(
        host="0.0.0.0", port=3000, debug=True
    )

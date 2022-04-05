import flask_sqlalchemy as SQLAlchemy
from sqlalchemy import Column, Text, String, DateTime, Float
from sqlalchemy.sql import func
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Email(db.Model):
    __tablename__ = "email"

    UUID = Column(db.Integer, primary_key=True)
    email = Column(db.String(128),unique=True)
    reason = Column(db.String(128)),
    ip = Column(db.String(50)),
    date_create = Column(DateTime(timezone=True), server_default=func.now())

class EmailSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Email
        include_relationships = True
        load_instants = True

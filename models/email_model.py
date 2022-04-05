from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()


class Email(db.Model):
    __tablename__ = "email"

    email = Column(db.String(128),primary_key=True, unique=True)
    UUID = Column(db.Integer)
    reason = Column(db.String(128))
    ip = Column(db.String(50))
    date_create = Column(DateTime(timezone=True), server_default=func.now())


class EmailSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Email
        include_relationships = True
        load_instants = True

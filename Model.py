from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(150), unique=False, nullable=False)
    prenom = db.Column(db.String(150), unique=False, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    phone =  db.Column(db.String(8), unique=False, nullable=False)
    pwd =  db.Column(db.String(150), unique=False, nullable=False)
    municipality =  db.Column(db.String(150), unique=False, nullable=False)
    lieu =  db.Column(db.String(150), unique=False, nullable=False)
    mtype = db.Column(db.Integer, unique=False, nullable=False)
    cin =  db.Column(db.String(150), unique=False, nullable=False)
    def __init__(self, email , nom , prenom , phone , pwd , municipality , lieu, mtype, cin ):
        self.email = email
        self.nom = nom
        self.prenom = prenom
        self.phone = phone
        self.pwd = pwd
        self.municipality = municipality
        self.lieu = lieu
        self.mtype = mtype
        self.cin = cin



class UserSchema(ma.Schema):
    id = fields.Integer()
    nom = fields.String(required=True)
    prenom = fields.String(required=True)
    email = fields.String(required=True)
    phone = fields.String(required=True)
    pwd = fields.String(required=True)
    municipality = fields.String(required=True)
    lieu = fields.String(required=True)
    mtype = fields.Integer(required=True)
    cin = fields.String(required=True)

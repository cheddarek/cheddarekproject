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




class Deliveries(db.Model):
    __tablename__ = 'deliveries'
    id = db.Column(db.Integer, primary_key=True)
    idClient = db.Column(db.Integer, unique=False, nullable=False)
    idVendor = db.Column(db.Integer, unique=False, nullable=True)
    idDeliveryMan = db.Column(db.Integer, unique=False, nullable=True)
    orderDate = db.Column(db.DateTime, nullable = False)
    deliveryDate = db.Column(db.DateTime, nullable = True)
    realDeliveryDate = db.Column(db.DateTime, nullable = True)
    content = db.Column(db.String (300), nullable = False)
    def __init__(self, id, idClient, idVendor, idDeliveryMan, orderDate, deliveryDate, realDeliveryDate, content):
        self.id = id
        self.idClient = idClient
        self.idVendor = idVendor
        self.idDeliveryMan = idDeliveryMan
        self.orderDate = orderDate
        self.deliveryDate = deliveryDate
        self.realDeliveryDate = realDeliveryDate
        self.content = content


class DeliveriesSchema(ma.Schema):
    id = fields.Integer()
    idClient = fields.Integer()
    idVendor = fields.Integer()
    idDeliveryMan = fields.Integer()
    orderDate = fields.DateTime()
    deliveryDate = fields.DateTime(required=True)
    realDeliveryDate = fields.DateTime()
    content = fields.String(required=True)

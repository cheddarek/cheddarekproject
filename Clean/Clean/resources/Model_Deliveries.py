from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()

class Deliveries(db.Model):
    __tablename__ = 'deliveries'
    id = db.Column(db.Integer, primary_key=True)
    idClient = db.Column(db.Integer, unique=True, nullable=False)
    idVendor = db.Column(db.Integer, unique=True, nullable=True)
    idDeliveryMan = db.Column(db.Integer, unique=True, nullable=True)
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
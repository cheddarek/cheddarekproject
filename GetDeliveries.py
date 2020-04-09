# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 18:51:22 2020

@author: Khawla
"""

from flask import request
from flask_restful import Resource
from Model import db, Deliveries, DeliveriesSchema

deliveries_schema = DeliveriesSchema(many=True)
delivery_schema = DeliveriesSchema()

class DeliveriesResource(Resource):
    def get(self):
        users = Deliveries.query.all()
        users = deliveries_schema.dump(users)
        return {'status': 'success', 'data': users}, 200
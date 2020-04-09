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
        deliveries = Deliveries.query.all()
        deliveries = deliveries_schema.dump(deliveries)
        return {'status': 'success', 'data': deliveries}, 200
    
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        
        delivery = Deliveries(
            id=json_data['id'],
            idClient=json_data['idClient'],
            idVendor=json_data['idVendor'],
            idDeliveryMan=json_data['idDeliveryMan'],
            orderDate=json_data['orderDate'],
            deliveryDate=json_data['deliveryDate'],
            realDeliveryDate=json_data['realDeliveryDate'],
            content=json_data['content']
        )

        db.session.add(delivery)
        db.session.commit()

        result = delivery_schema.dump(delivery)

        return {"status": 'success', 'data': result}, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data = delivery_schema.load(json_data)

        category = Deliveries.query.filter_by(id=data['id']).first()
        if not category:
            return {'message': 'Category does not exist'}, 400
        category.name = data['id']
        db.session.commit()

        result = delivery_schema.dump(category)

        return {"status": 'success', 'data': result}, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data = delivery_schema.load(json_data)
        user = Deliveries.query.filter_by(id=data['id']).delete()
        db.session.commit()
        result = delivery_schema.dump(user)
        return {"status": 'success', 'data': result}, 204
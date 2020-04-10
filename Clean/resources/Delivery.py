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

        delivery = Deliveries.query.filter_by(id=data['id']).first()
        if not delivery:
            return {'message': 'Delivery does not exist'}, 400
        delivery.idClient = data['idClient']
        db.session.commit()

        result = delivery_schema.dump(delivery)

        return {"status": 'success', 'data': result}, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data = delivery_schema.load(json_data)
        delivery = Deliveries.query.filter_by(id=data['id']).delete()
        db.session.commit()
        result = delivery_schema.dump(delivery)
        return {"status": 'success', 'data': result}, 204
    def listproducts(self):
        deliveries = Deliveries.query.all()
        deliveries = deliveries_schema.dump(deliveries)
        tmp = deliveries[0]['content']
        return {'status': 'success', 'data': deliveries}, 200
from flask import request
from flask_restful import Resource
from Model import db, Municipality, MunicipalitySchema

municipalities_schema = MunicipalitySchema(many=True)
municipality_schema = MunicipalitySchema()

class MunicipalityResource(Resource):
    def get(self):
        municipalities = Municipality.query.all()
        municipalities = municipalities_schema.dump(municipalities)
        return {'status': 'success', 'data': municipalities}, 200

    def post(self):
        json_data = request.get_json(force=True)
        municipality = Municipality(
            nom=json_data['nom']
        )
        db.session.add(municipality)
        db.session.commit()
        result = municipality_schema.dump(municipality)
        return {"status": 'success', 'data': result}, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data = municipality_schema.load(json_data)

        municipality = Municipality.query.filter_by(id=data['id']).first()
        if not municipality:
            return {'message': 'User does not exist'}, 400
        municipality.nom = data['nom']
        db.session.commit()

        result = municipality_schema.dump(municipality)

        return {"status": 'success', 'data': result}, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data = municipality_schema.load(json_data)
        user = Municipality.query.filter_by(id=data['id']).delete()
        db.session.commit()
        result = municipality_schema.dump(user)
        return {"status": 'success', 'data': result}, 204
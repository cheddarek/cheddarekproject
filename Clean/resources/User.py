from flask import request
from flask_restful import Resource
from Model import db, User, UserSchema

users_schema = UserSchema(many=True)
user_schema = UserSchema()

class UserResource(Resource):
    def get(self):
        users = User.query.all()
        users = users_schema.dump(users)
        return {'status': 'success', 'data': users}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data= user_schema.load(json_data)
        user = User.query.filter_by(email=data['email']).first()


        if user:
            return {'message': 'User already exists'}, 400
        user = User(
            email=json_data['email'],
            nom=json_data['nom'],
            prenom=json_data['prenom'],
            phone=json_data['phone'],
            pwd=json_data['pwd'],
            municipality=json_data['municipality'],
            lieu=json_data['lieu'],
            mtype=json_data['mtype'],
            cin=json_data['cin']

        )

        db.session.add(user)
        db.session.commit()

        result = user_schema.dump(user)

        return {"status": 'success', 'data': result}, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data = user_schema.load(json_data)

        user = User.query.filter_by(id=data['id']).first()
        if not user:
            return {'message': 'User does not exist'}, 400
        user.nom = data['nom']
        db.session.commit()

        result = user_schema.dump(user)

        return {"status": 'success', 'data': result}, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data = user_schema.load(json_data)
        user = User.query.filter_by(id=data['id']).delete()
        db.session.commit()
        result = user_schema.dump(user)
        return {"status": 'success', 'data': result}, 204
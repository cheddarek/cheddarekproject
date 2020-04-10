from flask import request, jsonify, make_response
from flask_restful import Resource
from Model import Product, ProductSchema, db

products_schema = ProductSchema(many=True)
product_schema = ProductSchema()
class ProductResource(Resource):
    def get(self):
        products = Product.query.all()
        products = products_schema.dump(products)
        return {'status': 'success', 'data': products}, 200

    def post(self):
        json_data = request.get_json(force=True)
        data = product_schema.load(json_data)
        product = Product(
            nom=json_data['nom'],
            description=json_data['description'],
            prix=json_data['prix'],
            image=json_data['image']
        )
        db.session.add(product)
        db.session.commit()
        result = product_schema.dump(product)
        return {"status": 'success', 'data': result}, 201

    def put(self):
        json_data = request.get_json()
        product = Product.query.filter_by(id=json_data['id']).first()
        if json_data.get('nom'):
            product.nom = json_data['nom']
        if json_data.get('description'):
            product.description = json_data['description']
        if json_data.get('prix'):
            product.prix = json_data['prix']
        if json_data.get('image'):
            product.image = json_data['image']
        db.session.add(product)
        db.session.commit()
        product_schema = ProductSchema(only=['id', 'nom', 'description', 'prix', 'image'])
        product = product_schema.dump(product)
        return make_response(jsonify({"product": product}))

    def delete(self):
        json_data = request.get_json()
        product = Product.query.filter_by(id=json_data['id']).first()
        db.session.delete(product)
        db.session.commit()
        return make_response("", 204)


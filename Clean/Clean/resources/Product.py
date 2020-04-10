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
        data = request.get_json()
        get_product = Product.query.get(id)
        if data.get('nom'):
            get_product.nom = data['nom']
        if data.get('description'):
            get_product.description = data['description']
        if data.get('prix'):
            get_product.prix = data['prix']
        if data.get('image'):
            get_product.image = data['image']
        db.session.add(get_product)
        db.session.commit()
        product_schema = ProductSchema(only=['id', 'nom', 'description', 'prix', 'image'])
        product = product_schema.dump(get_product)
        return make_response(jsonify({"product": product}))

    def delete(self):
        get_product = Product.query.get(id)
        db.session.delete(get_product)
        db.session.commit()
        return make_response("", 204)


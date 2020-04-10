from flask import Flask, request, jsonify, make_response
from Model import Product, ProductSchema
from flask_restful import Resource
from Model import db, User, UserSchema

class ProductResource(Resource):
    def get(self):
        get_products = Product.query.all()
        product_schema = ProductSchema(many=True)
        products = product_schema.dump(get_products)
        return make_response(jsonify({"product": products}))

    def post(self):
        data = request.get_json(force=True)
        product_schema = ProductSchema()
        product = product_schema.load(data)
        result = product_schema.dump(product)
        return make_response(jsonify({"product": result}), 200)

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


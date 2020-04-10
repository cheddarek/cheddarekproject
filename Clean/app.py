from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello
from resources.User import UserResource
from resources.Delivery import DeliveriesResource
from resources.Product import ProductResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)


api.add_resource(Hello, '/Hello')
api.add_resource(UserResource, '/User')
api.add_resource(DeliveriesResource, '/Delivery')
api.add_resource(ProductResource, '/Product')
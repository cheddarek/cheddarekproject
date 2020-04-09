from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost/cheddarek'
db = SQLAlchemy(app)

###Models####
class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(10))
    description = db.Column(db.String(20))
    prix = db.Column(db.Float)
    image = db.Column(db.String(100))



    def create(self):
      db.session.add(self)
      db.session.commit()
      return self
    def __init__(self,nom,description,prix, image):
        self.nom = nom
        self.description = description
        self.prix = prix
        self.image = image
    def __repr__(self):
        return '' % self.id

db.create_all()



class ProductSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Product
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    nom = fields.String(required=True)
    description = fields.String(required=True)
    prix = fields.Number(required=True)
    image = fields.String(required=True)

@app.route('/products', methods = ['GET'])
def index():
    get_products = Product.query.all()
    product_schema = ProductSchema(many=True)
    products = product_schema.dump(get_products)
    return make_response(jsonify({"product": products}))

@app.route('/products', methods = ['POST'])
def create_product():
    data = request.get_json()
    product_schema = ProductSchema()
    product = product_schema.load(data)
    result = product_schema.dump(product.create())
    return make_response(jsonify({"product": result}),200)

@app.route('/products/<id>', methods = ['PUT'])
def update_product_by_id(id):
    data = request.get_json()
    get_product = Product.query.get(id)
    if data.get('nom'):
        get_product.nom = data['nom']
    if data.get('description'):
        get_product.description = data['description']
    if data.get('prix'):
        get_product.prix= data['prix']
    if data.get('image'):
        get_product.image = data['image']
    db.session.add(get_product)
    db.session.commit()
    product_schema = ProductSchema(only=['id', 'nom', 'description','prix','image'])
    product = product_schema.dump(get_product)
    return make_response(jsonify({"product": product}))

@app.route('/products/<id>', methods = ['DELETE'])
def delete_product_by_id(id):
    get_product = Product.query.get(id)
    db.session.delete(get_product)
    db.session.commit()
    return make_response("",204)

@app.route('/')
def test():
    return 'Server Works!'


@app.route('/greet')
def say_hello():
    return 'Hello from Server'

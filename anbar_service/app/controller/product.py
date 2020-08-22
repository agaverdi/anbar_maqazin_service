from flask import jsonify, Blueprint, request
from http import HTTPStatus
from app.models.model import Product, Category
from marshmallow.exceptions import ValidationError
from app.schemas.schemas import ProductSchema , CategorySchema
from app.utils.helper import check_category_id, check_product_name_and_count


product = Blueprint("product", __name__)


@product.route("/", methods=["GET"])

def test():

    return jsonify({"result": True})


@product.route("/products", methods=["GET"])
def get_products():

    products=Product.query.all()

    return ProductSchema().jsonify(products, many=True), HTTPStatus.OK

@product.route("/product/<uuid:id>", methods=["GET"])
def get_product(id):
    
    product=Product.query.filter_by(id=id).first()
    
    if product:
        return ProductSchema().jsonify(product), HTTPStatus.OK

    else:
        return jsonify({"result":False})

@product.route("/product/<uuid:id>", methods=["POST"])
def post_product(id):
    
    product=Product.query.filter_by(id=id).first()
    data =request.get_json()
    
    if data==None:
        return jsonify({"result":False})

    else:
        
        product.count=data.get('count')
        product.save()
        
        return jsonify({"result":True})

@product.route("/product", methods=["POST"])
def create_product():

        try:
            
            data = request.get_json()

            data_name=data.get("name")
            
            data_count=data.get("count")

            check=check_category_id(data.get("category_id"))

            if not check:
                return jsonify({"result":False, "message":"error happened, check data if correct"}) , HTTPStatus.BAD_REQUEST

            elif check: 
                return check_product_name_and_count(data.get("name"),data.get("count"))

            else: 
                product=ProductSchema().load(data)

                product.save()

                return ProductSchema().jsonify(product), HTTPStatus.OK

        except ValidationError as err:
            return jsonify(err.messages), HTTPStatus.NOT_FOUND



@product.route("/product/<uuid:id>", methods=["PUT"])
def update_product(id):
    data=request.get_json()

    product=Product.query.filter_by(id=id).first()

    if product:

        serializer=ProductSchema()

        product_up=serializer.dump(data)

        product_update==product.update(**product_up)

        return ProductSchema().jsonify(product), HTTPStatus.OK
    
    else:
        return jsonify({"res":False}), HTTPStatus.BAD_REQUEST

@product.route("/product/<uuid:id>", methods=["DELETE"])
def delete_product(id):

    product=Product.query.get(id)
    
    if Product:

        product.delete()
        
        return jsonify({"res":True}), HTTPStatus.OK

    else:
        return jsonify({"res":False, "message":"this post user not found"}), HTTPStatus.NOT_FOUND

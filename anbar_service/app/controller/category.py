from flask import jsonify, Blueprint, request
from http import HTTPStatus
from app.models.model import Category
from marshmallow.exceptions import ValidationError
from app.schemas.schemas import CategorySchema
from app.utils.helper import check_category_name


category = Blueprint("category", __name__)

@category.route("/categories", methods=["GET"])
def get_categories():
    
    categories=Category.query.all()

    return CategorySchema().jsonify(categories, many=True), HTTPStatus.OK

@category.route("/category/<uuid:id>", methods=["GET"])
def get_category(id):
    
    category=Category.query.filter_by(id=id)
    if category:
        
        return CategorySchema().jsonify(category), HTTPStatus.OK

    else:
        return jsonify({"result":False})

@category.route("/category", methods=["POST"])
def create_category():
    try:

        data=request.get_json()

        check=check_category_name(data.get("name"))

        if not check:
            return jsonify({"result":False,  'message': "This category is already exists"}), HTTPStatus.NOT_FOUND

        serializer=CategorySchema()
        new_category=serializer.load(data)
        new_category.save()

        return serializer.jsonify(new_category), HTTPStatus.OK
    
    except ValidationError as err:

        return jsonify({err.messages}), HTTPStatus.NOT_FOUND

@category.route("/category/<uuid:id>", methods=['PUT'])
def update_category(id):
    data = request.get_json()

    category=Category.query.filter_by(id=id).first()

    if category:
        serializer=CategorySchema()

        category_up=serializer.dump(data)

        category_update= category.update(**category_up)

        return jsonify({
            "message":"Updated succesfully"
        }) , HTTPStatus.OK
    
    else:
        return jsonify({"res":False}) , HTTPStatus.BAD_REQUEST

@category.route("category/<uuid:id>", methods=["DELETE"])
def delete_category(id):

    category=Category.query.filter_by(id=id).first()

    if category:

        category.delete()

        return jsonify({"result":True}), HTTPStatus.OK

    else:
        return jsonify({"result":False}), HTTPStatus.NOT_FOUND





        


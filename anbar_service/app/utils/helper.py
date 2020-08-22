from app.models.model import Category ,Product
from flask import Flask, jsonify, request
from app.schemas.schemas import ProductSchema
from http import HTTPStatus

def check_category_name(name):

    if Category.query.filter_by(name=name).first():
        return False
    else:
        return True


def check_category_id(category_id):

    return True if Category.query.filter_by(id=category_id).first() else False


def check_product_name_and_count(name,count):
    if Product.query.filter_by(name=name).first():

        product=Product.query.filter_by(name=name).first()
        
        product_count=product.count+int(count)
        product.count=product_count
        product.save()
        return ProductSchema().jsonify(product), HTTPStatus.OK 

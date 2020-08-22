from flask import jsonify, Blueprint, request
from app.schemas.schemas import ProductCountSchema,ProductSchema, ProductCategorySchema
import requests
from http import HTTPStatus

maqazin = Blueprint("maqazin", __name__)


@maqazin.route("/", methods=["GET"])

def test():

    return jsonify({"result": True})


@maqazin.route("/maqazin", methods=["GET"])
def depo():
    req=requests.get('http://127.0.0.1:5000/categories')

    data=req.json()
    print(data)

    return jsonify(data), HTTPStatus.OK

@maqazin.route("/sale/<uuid:id>", methods=["POST"])
def depo_category(id):
    new_data=request.get_json()
    
    new_data_count=new_data.get("count"); #2

    req1=requests.get("http://127.0.0.1:5000/product/{}".format(id))
    
    count=req1.json().get("count")#15
    
    
    new_count=int(count)-int(new_data_count)
    if new_count<0:
        return jsonify({"result":"yoxdur"})
    
    else:
        
        
        req=requests.post("http://127.0.0.1:5000/product/{}".format(id),json={ "count" : str(new_count)})
        
        
        if req.status_code==200:
            return req.json()

        else:
            return False

    
    


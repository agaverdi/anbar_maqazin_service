from app.models.model import Category , Product
from app.config.settings.extensions import ma
from marshmallow import fields
from marshmallow.fields import String,Email, UUID, Nested, Integer
from marshmallow import validates_schema

class CategorySchema(ma.SQLAlchemyAutoSchema):

    name=fields.String(required=True)
    products=Nested("ProductSchema", many=True)


    class Meta:
        model=Category
        load_instance= True

class ProductSchema(ma.SQLAlchemyAutoSchema):

    name = String(required=True)
    count= Integer(required=True)


    
    
class ProductCountSchema(ma.Schema):
    name = String()
    count = Integer()

    

class ProductCategorySchema(ma.Schema):
    name=String()
    products=String()
        
    def format_name(self, products):
        return "{}, {}".format(products.get("name"), products.get("count"))
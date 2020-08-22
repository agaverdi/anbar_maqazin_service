from app.models.model import Category , Product
from app.config.settings.extensions import ma
from marshmallow import fields
from marshmallow.fields import String,Email, UUID, Nested, Integer
from marshmallow import validates_schema

class CategorySchema(ma.SQLAlchemyAutoSchema):

    name     = fields.String(required=True, unique=True)
    products = Nested("ProductSchema", many=True)


    class Meta:
        model         = Category
        load_instance = True

class ProductSchema(ma.SQLAlchemyAutoSchema):

    name    = String(required=True)
    count   = String(required=True)
    category_id = UUID(required=True)

    class Meta:
        model = Product
        load_instance=True
    

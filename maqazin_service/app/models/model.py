from app.config.db.conf import Model, Integer,String,BOOLEAN, DateTime, Column, ForeignKey,relationship, UUIDType
from app.app import db

class Category(Model):
    __tablename__="category"

    name=Column(String(20),nullable=False, unique=True)
    products=relationship("Product", backref="category", lazy=True)



class Product(Model):
    __tablename__= "product"

    name = Column(String(40), nullable=False)
    count=Column(Integer, nullable=False)
    category_id=Column(UUIDType(), ForeignKey("category.id"),nullable=True)








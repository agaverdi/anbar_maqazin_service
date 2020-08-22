from app.app import create_app,db
import os


settings_name = os.getenv("APP_SETTINGS")

app = create_app(settings_name)

# from app import app
from app.models.model import Product, Category

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Product': Product, 'Category': Category}
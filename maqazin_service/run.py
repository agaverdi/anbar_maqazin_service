from app.app import create_app,db
import os

settings_name = os.getenv("APP_SETTINGS")

app = create_app(settings_name)

# db.create_all(app=create_app(settings_name))
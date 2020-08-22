from .base import  Config
from datetime import timedelta
import os

class Development(Config):

    SQLALCHEMY_DATABASE_URI = "postgres:///anbar_db"

    
    DEVELOPMENT = True
    ASSETS_DEBUG = True   
    DEBUG = True
    
    




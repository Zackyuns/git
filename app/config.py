import os
from dotenv import load_dotenv

load_dotenv()

class config:
    
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.geetenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
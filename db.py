from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
database = os.getenv('DB_DATABASE')

engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")

def services():
    with engine.connect() as connection:
        result = connection.execute(text("select * from services"))
        return result.all()

def subservices():
    with engine.connect() as connection:
        result = connection.execute(text("select * from services"))
        result = result.all()
        sub = []
        for row in result:
            temp = row.service.split('|')
            sub.append(temp)
        return sub

def highlights():
    with engine.connect() as connection:
        result = connection.execute(text("select * from highlights"))
        result = result.all()
        return result
    
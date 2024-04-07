from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from os import environ
load_dotenv()

# DB_URL = "mysql+mysqlconnector://root:root@localhost/sampledb"

engine = create_engine(environ.get("DB_URL"))
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()
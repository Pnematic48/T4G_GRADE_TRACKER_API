from sqlalchemy import create_engine
from  sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

connection_str = os.environ.get("DATABASE_URL")

engine = create_engine(connection_str, pool_pre_ping=True)
session = sessionmaker(bind=engine)

Base = declarative_base()
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()  

def create_tables():
    Base.metadata.create_all(bind=engine)

try:
    with engine.connect() as connection:
        print("Sucessfully connected to the database")
        connection.close()
except Exception as e:
    print(f"failed to connect to the database: {e}")
            


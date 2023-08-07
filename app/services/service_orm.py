from decouple import config
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class ORMService:
    def __init__(self):
        self.config = config("CONF_NAME")
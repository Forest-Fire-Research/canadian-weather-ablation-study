from dotenv import load_dotenv
from sqlalchemy import create_engine
from os import getenv

class Database():
    def __init__(self):
        # load the .env file variables 
        load_dotenv()

        # get the varaibles 
        self.db_name = getenv("POSTGRES_DB")
        self.host = getenv("POSTGRES_HOST")
        self.username = getenv("POSTGRES_USER")
        self.port = getenv("POSTGRES_HOST_PORT")
        self.password = getenv("POSTGRES_PASSWORD")

    def __get_engine_url__(self):
        return f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.db_name}"
    
    def get_connection(self):
        return create_engine(self.__get_engine_url__())

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from os import getenv

class Database():
    def __init__(self):
        # load the .env file variables 
        load_dotenv()

        # get the varaibles 
        self.__db_name = getenv("POSTGRES_DB")
        self.__host = getenv("POSTGRES_HOST")
        self.__username = getenv("POSTGRES_USER")
        self.__port = getenv("POSTGRES_HOST_PORT")
        self.__password = getenv("POSTGRES_PASSWORD")

        # establish connection
        self.connection = create_engine(self.__get_engine_url__())
        print(f"Connection Established!!!\n\t{self.connection}")

    def __get_engine_url__(self):
        return f"postgresql://{self.__username}:{self.__password}@{self.__host}:{self.__port}/{self.__db_name}"
    
    def get_connection(self):
        return self.connection

    def execute_sql(self, statement:str):
        with self.connection.connect() as con:
            con.execute(
                text(
                    statement
                )
            )

# pylint: disable=all
import logging
from psycopg2 import connect, OperationalError
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class DatabaseService:
    def __init__(self):
        db_name="home_temp"
        db_user="postgres"
        db_password="110102ee"
        db_host="localhost"
        db_port="5432"
        
        try:
            self.__connection=connect(
                host=db_host,
                user=db_user,
                dbname=db_name,
                password=db_password,
                port=db_port,
            )
            logger.info("Database connection succeed")
        except OperationalError as error:
            logger.error(f"Error connecting to the database: {error}")
            self.__connection = None
    def get_connection(self):
        return self.__connection
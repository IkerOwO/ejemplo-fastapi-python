import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

def get_db_connection():
    host = os.getenv("MYSQL_HOST")
    user = os.getenv("MYSQL_USER")
    password = os.getenv("MYSQL_PASSWORD")
    database = os.getenv("MYSQL_DB")

    if not all([host, user, password, database]):
        raise RuntimeError(
            "Faltan variables de entorno de la base de datos: MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB"
        )

    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

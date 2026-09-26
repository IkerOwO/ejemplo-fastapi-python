from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

app = FastAPI()

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

class User(BaseModel):
    username: str
    email: str
    password: str

@app.get("/users")
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return users

@app.post("/create")
def insert_user(user: User):
    try: 
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
        values = (user.username, user.email, user.password)
        cursor.execute(query, values)
        
        conn.commit()

        cursor.close()
        conn.close()
        return {"message": "Usuario creado con exito!"}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error en la base de datos: {err}")
    


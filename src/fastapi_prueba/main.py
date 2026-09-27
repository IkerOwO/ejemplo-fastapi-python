from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector
from fastapi_prueba.database import get_db_connection

app = FastAPI()

class User(BaseModel):
    username: str
    email: str
    password: str

class PasswordUpdate(BaseModel):
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
    
@app.put("/user/{user_id}")
def update_password(user_id: int, passw: PasswordUpdate):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        query = "UPDATE users SET password = %s WHERE id = %s"
        values = (passw.password, user_id)
        cursor.execute(query, values)

        conn.commit()

        cursor.close()
        conn.close()
        return {"message": "Contraseña cambiada con exito!"}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f'Error en el update: {err}')

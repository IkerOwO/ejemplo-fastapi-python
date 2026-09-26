from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Definimos una clase Persona
class Person(BaseModel): 
    name: str
    surname: str
    age: int

# Endpoint GET
@app.get("/person")
def return_person(person: Person):
    return {
        "name" : person.name,
        "surname": person.surname,
        "age": person.age
    }

# Endpoint POST
@app.post("/create/")
def create_person(person: Person):
    return person

# Endpoint PUT
@app.put("/person/{person_id}")
def update_age(person_id: int, person: Person):
    return {
        "person_age": person.age,
        "person_id": person_id
    }
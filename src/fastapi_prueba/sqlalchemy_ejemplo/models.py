import fastapi_prueba.sqlalchemy_ejemplo.db as db
from sqlalchemy import Column, Integer, String, Float

class Producto(db.Base):
    __tablename__ = 'producto'

    id = Column(Integer, autoincrement=True, primary_key=True)
    nombre = Column(String(40), nullable=False)
    precio = Column(Float, nullable=False)

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __repr__(self):
        return f'Producto({self.nombre, {self.precio}})'

    def __str__(self):
        return self.nombre


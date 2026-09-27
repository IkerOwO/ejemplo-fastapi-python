from fastapi_prueba.sqlalchemy_ejemplo.db import *
from fastapi_prueba.sqlalchemy_ejemplo.models import *
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

@app.get("/products")
def get_all(db: Session = Depends(get_db)):
    query = db.session.query(Producto).all()
    return query

@app.get("/products/{product_id}")
def get_by_id(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Producto).filter(Producto.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado!")
    return product

@app.post("/products/create")
def create_product(name: str, price: float, db: Session = Depends(get_db)):
    db_product = Producto(nombre=name, precio=price)
    db.add(db_product)
    db.commit()
    db.refresh()
    return db_product


#def run():
    #arroz = Producto('Arroz', 1.25)
    #db.session.add(arroz)
    #print(arroz.id)
    #agua = Producto('Agua', 0.3)
    #db.session.add(agua)
    #db.session.commit()
    #print(arroz.id)
#    pass

#if __name__ == '__main__':
#    db.Base.metadata.create_all(db.engine)
#    run()


# Realizar consultas
#consulta = db.session.query(Producto)

# Obtener objeto a partir de id
#ob = db.session.query(Producto).get(1)

# Obtener los objetos de una consulta
#productos = db.session.query(Producto).all()

# Contar el numero de elementos devueltos por una consulta
#num_productos = db.session.query(Producto).count()

# Aplicar filtros
#agua = db.session.query(Producto).filter_by(nombre='Agua').first

#menos_de_1 = db.session.query(Producto).filter(Producto.precio < 1).all()
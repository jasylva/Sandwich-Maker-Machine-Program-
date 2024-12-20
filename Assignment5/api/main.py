from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from .models import models, schemas
from .controllers import orders
from .dependencies.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Order CRUD
@app.post("/orders/", response_model=schemas.Order, tags=["Orders"])
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return orders.create(db=db, order=order)


@app.get("/orders/", response_model=list[schemas.Order], tags=["Orders"])
def read_orders(db: Session = Depends(get_db)):
    return orders.read_all(db)


@app.get("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def read_one_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order


@app.put("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def update_one_order(order_id: int, order: schemas.OrderUpdate, db: Session = Depends(get_db)):
    order_db = orders.read_one(db, order_id=order_id)
    if order_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.update(db=db, order=order, order_id=order_id)


@app.delete("/orders/{order_id}", tags=["Orders"])
def delete_one_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.delete(db=db, order_id=order_id)


# OrderDetail CRUD
@app.post("/order_details/", response_model=schemas.OrderDetail, tags=["OrderDetails"])
def create_order_detail(order_detail: schemas.OrderDetailCreate, db: Session = Depends(get_db)):
    return orders.create(db=db, order=order_detail)

@app.get("/order_details/", response_model=list[schemas.OrderDetail], tags=["OrderDetails"])
def read_order_details(db: Session = Depends(get_db)):
    return orders.read_all(db)

@app.get("/order_details/{order_detail_id}", response_model=schemas.OrderDetail, tags=["OrderDetails"])
def read_one_order_detail(order_detail_id: int, db: Session = Depends(get_db)):
    order_detail = orders.read_one(db, order_id=order_detail_id)
    if order_detail is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order_detail

@app.put("/order_details/{order_detail_id}", response_model=schemas.OrderDetail, tags=["OrderDetails"])
def update_one_order_detail(order_detail_id: int, order_detail: schemas.OrderDetailUpdate, db: Session = Depends(get_db)):
    order_detail_db = orders.read_one(db, order_id=order_detail_id)
    if order_detail_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.update(db=db, order=order_detail, order_id=order_detail_id)

@app.delete("/order_details/{order_detail_id}", tags=["OrderDetails"])
def delete_one_order_detail(order_detail_id: int, db: Session = Depends(get_db)):
    order_detail = orders.read_one(db, order_id=order_detail_id)
    if order_detail is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.delete(db=db, order_id=order_detail_id)

# Recipe CRUD
@app.post("/recipes/", response_model=schemas.Recipe, tags=["Recipes"])
def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return orders.create(db=db, order=recipe)

@app.get("/recipes/", response_model=list[schemas.Recipe], tags=["Recipes"])
def read_recipes(db: Session = Depends(get_db)):
    return orders.read_all(db)

@app.get("/recipes/{recipe_id}", response_model=schemas.Recipe, tags=["Recipes"])
def read_one_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = orders.read_one(db, order_id=recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="User not found")
    return recipe

@app.put("/recipes/{recipe_id}", response_model=schemas.Recipe, tags=["Recipes"])
def update_one_recipe(recipe_id: int, recipe: schemas.RecipeUpdate, db: Session = Depends(get_db)):
    recipe_db = orders.read_one(db, order_id=recipe_id)
    if recipe_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.update(db=db, order=recipe, order_id=recipe_id)

@app.delete("/recipes/{recipe_id}", tags=["Recipes"])
def delete_one_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = orders.read_one(db, order_id=recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.delete(db=db, order_id=recipe_id)

# Resource CRUD
@app.post("/resources/", response_model=schemas.Resource, tags=["Resources"])
def create_resource(resource: schemas.ResourceCreate, db: Session = Depends(get_db)):
    return orders.create(db=db, order=resource)

@app.get("/resources/", response_model=list[schemas.Resource], tags=["Resources"])
def read_resources(db: Session = Depends(get_db)):
    return orders.read_all(db)

@app.get("/resources/{resource_id}", response_model=schemas.Resource, tags=["Resources"])
def read_one_resource(resource_id: int, db: Session = Depends(get_db)):
    resource = orders.read_one(db, order_id=resource_id)
    if resource is None:
        raise HTTPException(status_code=404, detail="User not found")
    return resource

@app.put("/resources/{resource_id}", response_model=schemas.Resource, tags=["Resources"])
def update_one_resource(resource_id: int, resource: schemas.ResourceUpdate, db: Session = Depends(get_db)):
    resource_db = orders.read_one(db, order_id=resource_id)
    if resource_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.update(db=db, order=resource, order_id=resource_id)

@app.delete("/resources/{resource_id}", tags=["Resources"])
def delete_one_resource(resource_id: int, db: Session = Depends(get_db)):
    resource = orders.read_one(db, order_id=resource_id)
    if resource is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.delete(db=db, order_id=resource_id)

# Sandwich CRUD
@app.post("/sandwiches/", response_model=schemas.Sandwich, tags=["Sandwiches"])
def create_sandwich(sandwich: schemas.SandwichCreate, db: Session = Depends(get_db)):
    return orders.create(db=db, order=sandwich)

@app.get("/sandwiches/", response_model=list[schemas.Sandwich], tags=["Sandwiches"])
def read_sandwiches(db: Session = Depends(get_db)):
    return orders.read_all(db)

@app.get("/sandwiches/{sandwich_id}", response_model=schemas.Sandwich, tags=["Sandwiches"])
def read_one_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    sandwich = orders.read_one(db, order_id=sandwich_id)
    if sandwich is None:
        raise HTTPException(status_code=404, detail="User not found")
    return sandwich

@app.put("/sandwiches/{sandwich_id}", response_model=schemas.Sandwich, tags=["Sandwiches"])
def update_one_sandwich(sandwich_id: int, sandwich: schemas.SandwichUpdate, db: Session = Depends(get_db)):
    sandwich_db = orders.read_one(db, order_id=sandwich_id)
    if sandwich_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.update(db=db, order=sandwich, order_id=sandwich_id)

@app.delete("/sandwiches/{sandwich_id}", tags=["Sandwiches"])
def delete_one_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    sandwich = orders.read_one(db, order_id=sandwich_id)
    if sandwich is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.delete(db=db, order_id=sandwich_id)


from fastapi import FastAPI, Path
import logging
from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    name : str
    price : float
    brand : Optional[str] = None
    
class UpdateItem(BaseModel):
    name : Optional[str] = None
    price : Optional[float] = None
    brand : Optional[str] = None
    

app = FastAPI()

inventory = {}

@app.get("/")
def index():
    return {"message": "Hello World"}


@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(description="Item ID", default=None, ge=0)):
    return inventory[item_id]


@app.get("/get-by-name/")
def get_item(name : str = None): # remove or insert the `= None` to make it not required 
    
    item_id = [key for key, value in inventory.items() if value.name == name]
    
    if item_id:
        return inventory[item_id[0]]
    else:
        return {"message": "Item not found"}
    
@app.post("/create-item/{item_id}")
def create_item(item_id: int, item : Item):
    if item_id in inventory:
        return {"message": "Item already exists"}
    inventory[item_id] = item
    return inventory[item_id]

@app.put("/update-item/{item_id}")
def create_item(item_id: int, item : UpdateItem):
    if item_id not in inventory:
        return {"message": "Item don't exist"}
    inventory[item_id].update(item)
    return inventory[item_id]
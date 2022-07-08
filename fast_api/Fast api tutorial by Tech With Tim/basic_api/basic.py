from fastapi import FastAPI, Path, Query, HTTPException, status
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
    if item_id in inventory:
        return inventory[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item ID not found")

@app.get("/get-by-name/")
def get_item(name : str = None): # remove or insert the `= None` to make it not required 
    
    item_id = [key for key, value in inventory.items() if value.name == name]
    
    if item_id:
        return inventory[item_id[0]]
    else:
        raise HTTPException(status_code=404, detail="Item name not found")
    
@app.post("/create-item/{item_id}")
def create_item(item_id: int, item : Item):
    if item_id in inventory:
        raise HTTPException(status_code=400, detail="Item ID Already Exists")
    inventory[item_id] = item
    return inventory[item_id]

@app.put("/update-item/{item_id}")
def create_item(item_id: int, item : UpdateItem):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item ID not found")
    
    if item.name:
        inventory[item_id].name = item.name
    
    if item.price:
        inventory[item_id].price = item.price
    
    if item.brand:
        inventory[item_id].brand = item.brand
    
    return inventory[item_id]

@app.delete('/delete-item')
def delete_item(item_id: int = Query(None, description="Item ID of the item you want to delete")):
    if item_id in inventory:
        del inventory[item_id]
        return {"message": "Item deleted"}
    else:
        raise HTTPException(status_code=404, detail="Item ID not found")
    
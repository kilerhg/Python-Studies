from fastapi import FastAPI, Path

app = FastAPI()

inventory = {
    1 : {
        'name': 'banana',
        'price': 3.0,
        'brand': 'Safeway',
    },
    
}

@app.get("/")
def index():
    return {"message": "Hello World"}


@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(description="Item ID", default=None, ge=0)):
    return inventory[item_id]
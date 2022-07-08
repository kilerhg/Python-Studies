# Notes about Fast API Studies

## Creating a simple fastapi API

```python

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello World"}

```

## End Point

### Defining http methods

Right after the decorator `@app.` you should insert the http method

#### Usual ones

* `@app.get('/')`
* `@app.post('/')`
* `@app.put('/')`
* `@app.delete('/')`

### Query Parameters

Query parameters are also on the endpoint but at the with `?variable=content`, to define in fast api is simply having a function parameter and not having it on the endpoint.

```python
@app.get("/get-by-name/")
def get_item(query_parameter : str = None): # remove or insert the `= None` to make it not required 
    
    return {'message': f'your query parameter is {query_parameter}'}
```

Accessing this query parameter: `endpoint/get-by/name/?query_parameter=something`

### Request body

Using a request body is very easy, just create a class child from BaseModel, set the parameters and if they are optional, at the function receive a parameter with this class at type hint.

```python
from typing import Optional # this Optional is complete up to you, just to make the code more readable.
from pydantic import BaseModel


# Create the class with the request body structure and types
class Item(BaseModel):
    name : str
    price : float
    brand : Optional[str] = None

# Create the endpoint with the function receiving an parameter with type hint of the class that we did.
@app.post("/create-item/{item_id}")
def create_item(item_id: int, item : Item):
    if item_id in inventory:
        return {"message": "Item already exists"}
    inventory[item_id] = item
    return inventory[item_id]
```

### Endpoint Parameters

inside a endpoint you can specify a parameter to be used inside the function, the name of the parameter inside the `{}` needs to be the same as the function parameter.

#### Example Endpoint parameters

```python
@app.get('/item/{item_code}')
def index(item_code: int)
```

### Documentation

The fastapi generates for you an auto docs (Swagger UI), where you can see the structure and test end points with parameters and json content, to make your docs better look after the (type hint)[] and Path, where is possible to set the expected type and description, title about the field

#### Type hint

With python Type hint is simply telling the expected type of a parameter in a function, but in fastapi this is actually used as a filter, and the request will only be valid once the type is correct.

```python
def test(value : int): # Example of type hint
```

#### Path

Used to insert more details to the documentation of a parameter.

```python
def test(value : int = Path(description="Description of the field", default="Default value"))
```

##### Filter numeric inputs whiting a specific range


Inside Path you can use the following parameters to specify range of number

* gt - Greater Then
* lt - Less Then
* ge - Greater Or equal to
* le - Less Or equal to

```python
def test(value : int = Path(description="Description of the field", default="Default value", ge=0))
```


## Links

* [Basic fastapi with Tech with tim](https://www.youtube.com/watch?v=-ykeT6kk4bk)
* [FastAPI Authentication with JWT (JSON Web Tokens)](https://www.youtube.com/watch?v=0_seNFCtglk)
* [Building Bigger Applications with FastAPI](https://www.youtube.com/watch?v=SWedfF6ftpA)
* [FastAPI Authentication Example With OAuth2, JSON Web Tokens and Tortoise ORM](https://www.youtube.com/watch?v=6hTRw_HK3Ts)
* [Python Asynchronous Programming - AsyncIO & Async/Await](https://www.youtube.com/watch?v=t5Bo1Je9EmE)
* [https://www.youtube.com/watch?v=_yXOJvr5vOM](https://www.youtube.com/watch?v=_yXOJvr5vOM)
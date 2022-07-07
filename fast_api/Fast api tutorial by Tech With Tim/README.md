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

### Parameters

inside a endpoint you can specify a parameter to be used inside the function

#### Example parameters

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

* (Basic fastapi with Tech with tim)[https://www.youtube.com/watch?v=-ykeT6kk4bk]
# Notes about Fast API Studies

## About

How to create tests with python

## Tests methods

### Given - When - Then

Using this way of test development, u'll need to follow the steps of:

1. Arrange - Create the setup for run the test

1. Act - Run the action with setup done, and get the result

1. Assert - Verify if the result is what we expect

## TDD

A way of developing the software, doing first the tests and then the code to satisfact the test.

## Creating Tests

We have 2 major libs to create tests in python, the built-in one: unittest and the popular one: pytest.

### PyTest

1. Create a folder named `tests` and enter this folder `cd tests`
1. Create the file `__init__.py`
1. Create a file starting with `test_` example: `test_my_app.py`
1. Inside the test file, create a class with the group of tests correlated
1. Create the function of the test, always starting with `test`, example `def test_my_func`
1. Create the assert syntax, which will work as a return, example `assert 1 == 1`
1. and finally to run, just execute in the main folder: `pytest`, or `pytest -v` to verbose mode, showing each test with description


#### Example

```python
# import the classes or functions that you wanna test.

def sum_num(a,b): # in a real code this would be somewhere else
    return a+b

class TestClass:
    def test_when_sum_receive_1_1_should_return_2(self):
        entry1 = 1 # Given-Arrange
        entry2 = 1 # Given-Arrange
        expect = 2

        result = sum_num(entry1, entry2) # When-Action

        assert result == expect # Then-Assert
```

#### Filtering

while writing tests, soon you will probably have a lot of tests, and you may want to execute just a few of then, how can you do that?

##### Key

Execute the tests that has the key word in the test func name, example: `pytest -k keyword`

##### Mark

Marks are a good way to label some tests, there are a few [default ones](https://pytest.org/en/6.2.x/mark.html), but you can [create your owns](https://pytest.org/en/6.2.x/example/markers.html#mark-examples).

###### Creating Marks

###### Setup

to create marks you need to import them from pytest with `from pytest import mark`

###### Using Marks

You will use marks just like other python decorators, example:

```python
@mark.name_mark
def test_name_test(self):
  # content of test
```

## Coverage percent

## Links

* [Pytest Docs](https://pytest.org/en/6.2.x/contents.html)
* [Pytest Default Marks](https://pytest.org/en/6.2.x/example/marker)
* [Pytest Custom Marks](https://pytest.org/en/6.2.x/example/markers.html#mark-examples)

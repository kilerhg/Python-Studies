# Notes about Test with Python

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

#### Handling Exceptions

Sometimes you may wan't to your test return an exception, then the `raises` of pytest will help you.

##### Using Raises

by using the with sintax, and then writing the code inside of it, the Exceptions will be handled, see an example below.

##### Example of handling exceptions

```python
def test_name(self):
  with pytest.raises(Exception):
      # cotent
      result = 0/0
      assert result
```

#### Filtering

while writing tests, soon you will probably have a lot of tests, and you may want to execute just a few of then, how can you do that?

Tip: you can use the filter with other parameter, example: `pytest -v -k keyword` or `pytest -v -m mark`

##### Key

Execute the tests that has the key word in the test func name, example: `pytest -k keyword`

##### Mark

Marks are a good way to label some tests, there are a few [default ones](https://pytest.org/en/6.2.x/mark.html), but you can [create your owns](https://pytest.org/en/6.2.x/example/markers.html#mark-examples).

###### Setup for custom marks

create a file called `pytest.ini` inside the master folder of your project, inside this file write the custom marks you want, example:

```ini
[pytest]
markers = 
    marker_name: Marker Description Here
```

###### Creating Marks

to create marks you need to import them from pytest with `from pytest import mark`

You will use marks just like other python decorators, example:

```python
@mark.name_mark
def test_name(self):
  ...
```

###### Default Marks

####### Skip

Skip a test always, can specify a reason

```python
@pytest.mark.skip(reason="write the reason here")
def test_some():
    ...
```

####### SkipIF

Skip a test if the condition is True.

```
import sys

@pytest.mark.skipif(sys.version_info < (3, 7), reason="Needs python 3.7 or newer")
def test_name():
    ...
```

####### Xfail

The Test should fail

```python
@pytest.mark.xfail
def test_name():
    ...
```

###### Using Marks

To use the mark, you will need to use the default statement `pytest` with the parameter `-m`, example: `pytest -m mark`

### Coverage

#### Setup

first you need to install the lib pytest-cov, with the following command:

`pip install pytest-cov`

#### Running
To run the coverage test use:

`pytest --cov`

##### Parameters

There are several userfull parameters to use, like:

`--cov=folder_with_code test/`  - Select the folder you wan't to verify the coverage
`--cov-report term-missing` - Return the lines that don't have tests

###### Examples of coverage

`pytest --cov=folder_with_code tests/` - Verify the percentage of coverage
`pytest --cov=folder_with_code tests/ --cov-report term-missing` - Verify percent of coverage and the lines that has missing test

## Links

* [Pytest Docs](https://pytest.org/en/6.2.x/contents.html)
* [Pytest Default Marks](https://pytest.org/en/6.2.x/example/marker)
* [Pytest Custom Marks](https://pytest.org/en/6.2.x/example/markers.html#mark-examples)
* [Pytest Init file](https://docs.pytest.org/en/6.2.x/reference.html#ini-options-ref)
* [Alura course]()

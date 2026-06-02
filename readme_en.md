# [🇧🇷 Português](./readme.md) [🇪🇸 Español](./readme_es.md) [🇺🇸 English](./readme_en.md)

# Python Notes

## Summary

* [Python Notes](#python-notes)
* [Summary](#summary)
* [General Notes](#general-notes)
* [Primitive Types](#primitive-types)
* [Arithmetic Operations](#arithmetic-operations)
* [Order Of Precedence](#order-of-precedence)
* [Print Notes](#print-notes)
* [Libraries](#libraries)
  * [Math](#math)
  * [Random](#random)
  * [Time](#time)
  * [Datetime](#datetime)
  * [Operator](#operator)
  * [Urllib](#urllib)
* [Manipulação De Texto](#manipulação-de-texto)
  * [Location](#location)
  * [Transformations](#transformations)
  * [Division](#division)
  * [Joining](#joining)
* [Simple and Compound Conditional Structures](#estrutura-condicional-simple-e-composta)
  * [Types](#types)
  * [Sequential](#sequential)
  * [Pythonize](#pythonize)
  * [Simple](#simple)
  * [Compound](#compound)
  * [Nested](#nested)
  * [If](#if)
* [Repetition Structure or Loops or Iterations](#estrutura-de-repetição-ou-laços-ou-iterações)
  * [Loop With Control Variable](#loop-with-control-variable)
    * [For](#for)
  * [Loop With Logical Test](#loop-with-logical-test)
    * [While](#while)
* [Coleções](#coleções)
  * [Notes](#notes)
  * [Tuples](#tuples)
  * [Lists](#lists)
  * [Dictionaries](#dictionaries)
* [Colors in the Python Terminal](#cores-no-terminal-python)
  * [Ansi](#ansi)
  * [Style](#style)
  * [Text](#text)
  * [Back](#back)
* [Extra data conversion](#conversão-base-de-dados)
* [Functions](#functions)
  * [What Is It](#what-is-it)
  * [Basic Function Declaration Without Parameters](#basic-function-declaration-without-parameters)
  * [Basic Function Declaration With Parameters](#basic-function-declaration-with-parameters)
  * [Pack Parameters - Receive Multiple Parameters](#pack-parameters---receive-multiple-parameters)
  * [Interactive Help](#interactive-help)
  * [Docstrings](#docstrings)
    * [What Is It](#what-is-it)
    * [How To Create](#how-to-create)
    * [Example](#example)
  * [Optional Parameters](#optional-parameters)
    * [What Is It](#what-is-it)
    * [How To Create](#how-to-create)
    * [Example](#example)
  * [Variable Scope](#variable-scope)
    * [Scope Definition](#scope-definition)
    * [Local Scope](#local-scope)
    * [Global Scope](#global-scope)
    * [Hint](#hint)
    * [Example](#example)
  * [Return Results](#return-results)
    * [How To Create](#how-to-create)
    * [Example](#example)
* [Modularização](#modularização)
  * [What Is It](#what-is-it)
  * [Focus](#focus)
  * [How To Create](#how-to-create)
  * [Advantages](#advantages)
* [Pacotes](#pacotes)
  * [What Is It](#what-is-it)
  * [How To Create](#how-to-create)
  * [When To Use](#when-to-use)
* [Error Handlings E Exceções](#error-handlings-e-exceções)
  * [Error Types](#error-types)
    * [Syntax](#syntax)
    * [Exception](#exception)
  * [Error Handling](#error-handling)
    * [What Is It](#what-is-it)
    * [How To Create](#how-to-create)
    * [Example](#example)
    * [Except](#except)
* [Manipulação De Arquivo Txt](#manipulação-de-arquivo-txt)
  * [Prepare To Read Save Replace](#prepare-to-read-save-replace)
    * [Parameters To Create Read](#parameters-to-create-read)
  * [Save Text](#save-text)
  * [Read Text File](#read-text-file)


## General Notes
Successive refinement: partition an application and run tests while developing it, for example to avoid errors early on, and correct them while in the development phase.<br />
Invert typed string with: ```var[::-1]```<br />
Flag - Stopping point<br />
You can get the same value for multiple variables using:<br />
```ex = ex1 = ex2 = ex3 = 0```<br />
reverse = True - makes some functions inverted ex: ```L.sort()```<br />
function == Method<br />
every function opens and closes parentheses after the name ex: f()<br />

## Primitive Types
* int - integer
* bool - boolean / true, false
* float - floating point numbers
* str - text string

## Arithmetic Operations
* Addition: +
* Subtraction: -
* Multiplication: *
* Division: /
* Power: **
* Division (floor): //
* Remainder/Modulo: %
* Comparison: ==
* Assignment: =

## Order Of Precedence
1. :()
1. :**
1. :*,/,//,%
1. :+,-
## Print Notes

Inside a print with f-string or .format you can use ```:.3f``` inside the braces to define only 3 digits after the decimal point<br />
```end=’ ’``` does not break the line<br />
```\n``` - line break<br />
3 double quotes to span multiple lines<br />
f-string - ```f'test : {variable}'```

## Libraries

### Math
```ceil(N)``` : rounds up<br />
```floor(N)``` : rounds down<br />
```trunc(N)``` : reduces decimal places without rounding<br />
```pow(N)``` : power<br />
```sqrt(N)``` : square root<br />
```factorial(N```) : factorial<br />

### Random

```random()``` : generates a random number between 0 and 1<br />
```randint(start number, End Number)``` : generates a random integer in a given range<br />
```shuffle(L)``` : Shuffles a list<br />

### Time

```sleep(seconds)```: pauses the process for the specified amount of time before continuing execution<br />

### Datetime

```date.today().year``` : current year<br />

### Operator

```itemgetter``` - used to fetch items inside dictionaries<br />

### Urllib

```urllib.request.urlopen( URL of a site )``` - attempts to access a site<br />
```variable_with_site_url.getcode()``` - Returns a code for the access attempt, with 200 meaning successful.<br />

## Manipulação De Texto

### Location

```phrase[9:21]``` - Returns the value of phrase starting at position 9 and going up to 20 (python ignores the last one)<br />
```len(f)``` - number of characters in a string or list<br />
```(T).count()``` - counts the amount of a character within a string / list<br />
```(T).find()``` - shows the position of a character within a string / list. if it doesn't exist it returns -1<br />
```(T).index(Searched value, Start)``` - shows the position of the searched value inside a compound variable<br />
```in``` - returns a boolean value<br />
```del(Variable)```
 


### Transformations
```replace()``` - Replaces a string/list value with another typed string<br />
```upper()``` - Converts a string to uppercase<br />
```lower()``` - Converts a string to lowercase<br />
```capitalize()``` - Converts a string to lowercase and makes the first letter uppercase<br />
```title()``` - Capitalizes the first letter of each word in a string<br />
```strip()``` - Removes useless spaces at the beginning and end of the string<br />
```rstrip()``` - Removes spaces on the right<br />
```lstrip()``` - Removes spaces on the left<br />
```string.center(Number of characters)``` - Centers the text in the defined Number of characters<br />

### Division

```split()``` - Splits a string into a list<br />

### Joining
```'separator'.join(phrase)``` - joins a string // example '-'.join(phrase) joins the string and separates it by '-'<br />
```zfill(number)``` - adds a certain amount of zeros to a string<br />

## Simple and Compound Conditional Structures

### Types

#### Sequential

runs the program linearly from top to bottom executing all commands<br />

#### Pythonize

Write everything in one line example:``` print('1' if var <=3 else '2')```

#### Simple

It executes only one conditional block<br />

#### Compound

executes more than one conditional block ex : else<br />

#### Nested

Conditions within conditions<br />

### If
```if``` - ```if```
```elif``` - Always needs an if beforehand<br />
```else``` - Can only be used once in the Nest block with if or elif<br />

## Repetition Structure or Loops or Iterations
### Loop With Control Variable

### For

```for x in range(Start Number, End Number(The Result being EN-1)```, what is the iteration (Example Add(1) or subtract(-1)) )<br />
```for x enumerated( Compound Variable )``` returns the value and the index.<br />

### Loop With Logical Test

#### While
```while not``` (Boolean Value):<br />
```while true```: infinite loop<br />
```break``` - interrupts the repetition loop<br />
```continue``` - continues the loop, and if it runs a part without a continue, it skips the rest of the current loop iteration<br />



## Coleções

### Notes

You can interpolate collections, for example: Dictionaries inside lists<br />

### Tuples

Character - ()

Tuples are Immutable
```sorted(T```) - sorts the tuple but doesn't store the value, use a variable to store it<br />

### Lists

Character - []

```sum(L)``` - sums all values in a list<br />
```L.append()``` - adds a value to the list<br />
```L[index]``` - shows the item at the indicated position<br />
```L.insert(Position,Value)``` - adds a value at a selected position <br />
```L.remove()``` - removes a value from the list<br />
```max(L)``` - Shows the highest value in the list<br />
```min(L)``` - Shows the lowest value in the list<br />
```(L).sort``` - Sorts the list<br />
```del L[Index]``` - Delete an item from a list by the chosen Index<br />
```L.pop(Index)``` - Delete an item from a list by the chosen Index, or if no argument is passed it removes the last value.<br />
```L.remove(value)``` - Remove the searched item by the defined value(Content)<br />
```L1 = L2``` - the '=' sign creates a link between lists, where changing one affects the other<br />
```L1 = L2[:]``` - copies the list, without creating a link<br />
```L1.append(L2[:])``` - Copies list L2 Inside list L1<br />
```L1 = [['Value1','Value2'],['Value1','Value2']]``` - Declares a list inside a list<br />
```print(L[0][0])``` - shows index 0 inside list [0]<br />
```L.clear()``` - Clears a list<br />
```L.choice``` - Curates an item randomly inside the list<br />

### Dictionaries

Character - {}

Main difference between a list : Has Literal indexes (Letters/Words)<br />

```D['Literal Index']``` = 'Value' - Adds a value to the variable<br />
```del D['Literal Index']``` - Deletes the value at the typed index. <br />
```D.values()``` - Returns the Values<br />
```D.keys()``` - Returns the Literal Indexes<br />
```D.items()``` - Returns both the Indexes(Keys), and the Values(values)<br />
```D.copy()``` - Copies the values from a dictionary without creating a link, (for using in loops etc)<br />
```D1 = sorted(D2.items(), key=itemgetter(dictionary index being 0 for keys, and 1 for values) )``` - Sorts in ascending order<br /> a dictionary based on the values

## Colors in the Python Terminal

### Ansi
```\033[Style;Text;Back;m```
```\033[0;33;44m```

### Style
0 - none <br />
1 - bold<br />
4 - underline<br />
7 - negative<br />
### Text
30 - white<br />
31 - red<br />
32 - green<br />
33 - yellow<br />
34 - blue<br />
35 - magenta<br />
36 - cyan<br />
37 - gray<br />
### Back
40 - white<br />
41 - red<br />
42 - green<br />
43 - yellow<br />
44 - blue<br />
45 - magenta<br />
46 - cyan<br />
47 - gray<br />

## Extra data conversion

```bin()``` - convert from decimal to binary<br />
```oct()``` - convert from decimal to Octal<br />
```hex()``` - convert from decimal to hexadecimal<br />

## Functions
### What Is It
They are routines, which may or may not return values and may or may not use parameters<br />
### Basic Function Declaration Without Parameters
```
def function():
 Routine/algorithm
 ```
    
### Basic Function Declaration With Parameters

```
def function(parameter):
    print('-'*10)
    print(parameter)
print('-'*10)
```

### Pack Parameters - Receive Multiple Parameters
```def counter(*num)``` - receives multiple parameters<br />



### Interactive Help
```help(internal function)``` - Returns help about an internal function <br />

### Docstrings
#### What Is It
Documentation string, that is, Help for a function you created<br />
#### How To Create
One line after defining the function, create 3 double quotes and close them. Anything inside is the 'manual on how to use your function'<br />
#### Example
```
def function(a,b,c):
    """
    -> here goes a direct description
    :param a: Description of parameter a
:param b: Description of parameter b
:param c: Description of parameter c
:return: whether the function returns or not and if so what the return is
    """
    Function code starts here
```






### Optional Parameters
#### What Is It
creates parameters that may or may not be inserted without influencing the functionality of the program<br />
#### How To Create
assign a value to a variable in case it is not inserted<br />
#### Example
```
def function(a,b,c=0(if c receives no value it will receive 0)):
    s = a + b + c
print(s)
```

### Variable Scope

#### Scope Definition
place where the variable will exist and where it will no longer exist<br />
#### Local Scope
exists only in one part of the program<br />
#### Global Scope
exists everywhere in the program<br />
#### Hint
In python, when defining a global and a local variable with the same name, it will create 2 different unlinked variables. To link them, you must use the global command<br />

##### Example
```
def function():
    global (variable name)
    function code starts here
```
    

### Return Results
#### How To Create

place the return command on the last line of the function along with a variable containing the value you want to return<br />

#### Example
```
def function(a,b,c):
    s = a + b + c
    return s
```

## Modularização
### What Is It
the separation of the main program from the functions<br />
### Focus
* Divide a Large program
* Increase readability
* Facilitate maintenance

### How To Create
Create a .py file in the same folder as the main program with the desired name<br />
inside put all the functions you need, after that in the main program use ```import file_name```, or ```from file_name import function_name```

### Advantages
* Code organization
* Easy maintenance
* Hiding detailed code
* Reusability in other projects

## Pacotes

### What Is It
A folder with various Modules, allowing you to separate modules by subject<br />
### How To Create
Just create a folder, within the project it already recognizes that it can potentially be a package<br />
Always inside a package you must have a file named: ```__init__.py``` where the functions will reside<br />
### When To Use
When projects start to get very large<br />

## Error Handlings E Exceções
### Error Types
#### Syntax
Typing errors, the typed command does not exist<br />
#### Exception
they are errors that happen due to incorrect assignment, receiving a number different from what was expected, etc<br />

### Error Handling
#### What Is It
check if something is possible to execute without resulting in an error, if there is a problem, perform another command<br />
#### How To Create
put ```try:``` break a line and write the command it should try, after writing the command block break a line '```except:```' break a line, and write what to do in case of an error, and if necessary ```else:``` and put what succeeded. ```finally:```, writes either way with or without an error<br />
#### Example
```
try:
    Command block
except: / variant / except Exception as error:
    if evaluating resulted in an error / variant / print(error.__class__) it shows what the error was
(optional) else:
    if it succeeded
(optional) finally:
    executes either way if it succeeded or not
```

#### Except
you can create numerous excepts and specify for each of them what the error is and how to handle each one:<br />
```
except TypeError:
    Handling for the TypeError.
except ValueError:
    Handling for the ValueError
```

## Manipulação De Arquivo Txt
### Prepare To Read Save Replace

```variable = open('Path you want to create/Read',Parameter)```

### Parameters To Create Read
```‘r’``` - Transforms into a variable ready for reading<br />
```‘a’``` - Transforms into a variable ready to append text<br />
```‘w’``` - Transforms into a variable ready to replace everything and put new text<br />
after each letter you can put ```+``` so that if the file doesn't exist it creates it, example: ```a+```<br />
```encoding=’utf-8’``` - Additional Parameter to write/read/save files containing accents<br />

### Save Text

```variable_ready_to_[append/replace]_text.write(‘desired text\n’)``` (the ‘\n’ is optional since it breaks the line, but it is highly recommended because if you add multiple texts it won't break lines automatically)<br />

### Read Text File

```print(variable_ready_to_read_text.read())``` - reads the file value including line breaks<br />

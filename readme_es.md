# [🇧🇷 Português](./readme.md) [🇪🇸 Español](./readme_es.md) [🇺🇸 English](./readme_en.md)

# Anotaciones Python

## Índice

* [Anotaciones Python](#anotaciones-python)
* [Índice](#índice)
* [Anotaciones Generales](#anotaciones-generales)
* [Tipos Primitivos](#tipos-primitivos)
* [Operaciones Aritméticas](#operaciones-aritméticas)
* [Orden De Precedencia](#orden-de-precedencia)
* [Anotaciones Print](#anotaciones-print)
* [Bibliotecas](#bibliotecas)
  * [Math](#math)
  * [Random](#random)
  * [Time](#time)
  * [Datetime](#datetime)
  * [Operator](#operator)
  * [Urllib](#urllib)
* [Manipulação De Texto](#manipulação-de-texto)
  * [Localización](#localización)
  * [Transformaciones](#transformaciones)
  * [División](#división)
  * [Fusión](#fusión)
* [Estrutura Condicional Simple E Composta](#estrutura-condicional-simple-e-composta)
  * [Tipos](#tipos)
  * [Secuencial](#secuencial)
  * [Pythonizar](#pythonizar)
  * [Simple](#simple)
  * [Compuesto](#compuesto)
  * [Anidadas](#anidadas)
  * [If](#if)
* [Estrutura De Repetição Ou Laços Ou Iterações](#estrutura-de-repetição-ou-laços-ou-iterações)
  * [Bucle Con Variable De Control](#bucle-con-variable-de-control)
    * [For](#for)
  * [Bucle Con Prueba Lógica](#bucle-con-prueba-lógica)
    * [While](#while)
* [Coleções](#coleções)
  * [Anotaciones](#anotaciones)
  * [Tuplas](#tuplas)
  * [Listas](#listas)
  * [Diccionarios](#diccionarios)
* [Cores No Terminal Python](#cores-no-terminal-python)
  * [Ansi](#ansi)
  * [Style](#style)
  * [Text](#text)
  * [Back](#back)
* [Conversão Base De Dados](#conversão-base-de-dados)
* [Funciones](#funciones)
  * [Qué Es](#qué-es)
  * [Declaración Básica Función Sin Parámetros](#declaración-básica-función-sin-parámetros)
  * [Declaración Básica Función Con Parámetros](#declaración-básica-función-con-parámetros)
  * [Empaquetar Parámetros - Reciba Varios Parámetros](#empaquetar-parámetros---reciba-varios-parámetros)
  * [Ayuda Interactiva](#ayuda-interactiva)
  * [Docstrings](#docstrings)
    * [Qué Es](#qué-es)
    * [Cómo Crear](#cómo-crear)
    * [Ejemplo](#ejemplo)
  * [Parámetros Opcionales](#parámetros-opcionales)
    * [Qué Es](#qué-es)
    * [Cómo Crear](#cómo-crear)
    * [Ejemplo](#ejemplo)
  * [Alcance De Variables](#alcance-de-variables)
    * [Definición De Alcance](#definición-de-alcance)
    * [Alcance Local](#alcance-local)
    * [Alcance Global](#alcance-global)
    * [Consejo](#consejo)
    * [Ejemplo](#ejemplo)
  * [Retorno De Resultados](#retorno-de-resultados)
    * [Cómo Crear](#cómo-crear)
    * [Ejemplo](#ejemplo)
* [Modularização](#modularização)
  * [Qué Es](#qué-es)
  * [Focos](#focos)
  * [Cómo Crear](#cómo-crear)
  * [Ventajas](#ventajas)
* [Pacotes](#pacotes)
  * [Qué Es](#qué-es)
  * [Cómo Crear](#cómo-crear)
  * [Cuándo Utilizar](#cuándo-utilizar)
* [Manejo De Erroress E Exceções](#manejo-de-erroress-e-exceções)
  * [Tipos De Errores](#tipos-de-errores)
    * [Sintaxis](#sintaxis)
    * [Excepción](#excepción)
  * [Manejo De Errores](#manejo-de-errores)
    * [Qué Es](#qué-es)
    * [Cómo Crear](#cómo-crear)
    * [Ejemplo](#ejemplo)
    * [Except](#except)
* [Manipulação De Arquivo Txt](#manipulação-de-arquivo-txt)
  * [Preparar Para Leer Guardar Reemplazar](#preparar-para-leer-guardar-reemplazar)
    * [Parámetros Para Crear Leer](#parámetros-para-crear-leer)
  * [Guardar Texto](#guardar-texto)
  * [Leer Archivo De Texto](#leer-archivo-de-texto)


## Anotaciones Generales
Refinamiento sucesivo: dividir una aplicación y realizar pruebas al desarrollar, para evitar errores al principio o en medio, y corregirlos en la fase de desarrollo.<br />
Invertir cadena escrita con: ```var[::-1]```<br />
Flag - Punto de parada<br />
Se puede recibir el mismo valor para varias variables utilizando:<br />
```ex = ex1 = ex2 = ex3 = 0```<br />
reverse = True - hace que algunas funciones se inviertan ej: ```L.sort()```<br />
función == Método<br />
toda función abre y cierra paréntesis después del nombre ej: f()<br />

## Tipos Primitivos
* int - entero
* bool - booleano / true, false
* float - números con coma/decimales
* str - cadena de texto

## Operaciones Aritméticas
* Adición: +
* Sustracción: -
* Multiplicación: *
* División: /
* Potencia: **
* División (entera): //
* Resto de la división/Módulo: %
* Comparación: ==
* Asignación: =

## Orden De Precedencia
1. :()
1. :**
1. :*,/,//,%
1. :+,-
## Anotaciones Print

dentro de un print con f-string o .format se puede utilizar ```:.3f``` dentro de las llaves para definir solo 3 dígitos después del punto decimal<br />
```end=’ ’``` no rompe la línea<br />
```\n``` - salto de línea<br />
3 comillas dobles para abarcar más de una línea<br />
f-string - ```f'prueba : {variable}'```

## Bibliotecas

### Math
```ceil(N)``` : redondea hacia arriba<br />
```floor(N)``` : redondea hacia abajo<br />
```trunc(N)``` : reduce lugares decimales sin redondear<br />
```pow(N)``` : potencia<br />
```sqrt(N)``` : raíz cuadrada<br />
```factorial(N```) : factorial<br />

### Random

```random()``` : genera número aleatorio entre 0 y 1<br />
```randint(número inicial, Número Final)``` : genera un número entero aleatorio en un rango determinado<br />
```shuffle(L)``` : Baraja una lista<br />

### Time

```sleep(segundos)```: hace que el proceso espere la cantidad de tiempo definida antes de continuar la ejecución<br />

### Datetime

```date.today().year``` : año actual<br />

### Operator

```itemgetter``` - usado para buscar elementos dentro de diccionarios<br />

### Urllib

```urllib.request.urlopen( URL de algún sitio )``` - intenta acceder a algún sitio<br />
```variable_con_url_sitio.getcode()``` - Devuelve un código para el intento de acceso, siendo 200 exitoso.<br />

## Manipulação De Texto

### Localización

```frase[9:21]``` - Devuelve el valor de la frase comenzando en la posición 9 y yendo hasta la 20 (python ignora la última)<br />
```len(f)``` - cantidad de caracteres en una cadena o lista<br />
```(T).count()``` - cuenta la cantidad de un carácter dentro de una cadena / lista<br />
```(T).find()``` - muestra la posición de un carácter dentro de una cadena / lista. si no existe, devuelve -1<br />
```(T).index(Valor buscado, Inicio)``` - muestra la posición del valor buscado dentro de una variable compuesta<br />
```in``` - devuelve valor booleano<br />
```del(Variable)```
 


### Transformaciones
```replace()``` - Reemplaza una cadena/valor de lista por otra cadena digitada<br />
```upper()``` - Convierte una cadena a mayúsculas<br />
```lower()``` - Convierte una cadena a minúsculas<br />
```capitalize()``` - Convierte una cadena a minúsculas y pone la primera letra en mayúscula<br />
```title()``` - Capitaliza la primera letra de cada palabra en una cadena<br />
```strip()``` - Elimina los espacios inútiles al principio y al final de la cadena<br />
```rstrip()``` - Elimina los espacios a la derecha<br />
```lstrip()``` - Elimina los espacios a la izquierda<br />
```string.center(Número de caracteres)``` - Centra el texto en el Número de caracteres definido<br />

### División

```split()``` - Divide una cadena en una lista<br />

### Fusión
```'separador'join(frase)``` - une una cadena // ejemplo '-'.join(frase) une la cadena y separa por '-'<br />
```zfill(número)``` - añade una cantidad de ceros a una cadena<br />

## Estrutura Condicional Simple E Composta

### Tipos

#### Secuencial

ejecuta el programa de forma lineal de arriba hacia abajo ejecutando todos los comandos<br />

#### Pythonizar

Escríbelo todo en una línea ejemplo:``` print('1' if var <=3 else '2')```

#### Simple

Ejecuta solo un bloque condicional<br />

#### Compuesto

ejecuta más de un bloque condicional ej : else<br />

#### Anidadas

Condiciones dentro de condiciones<br />

### If
```if``` - ```si```
```elif``` - Siempre necesita un if previamente<br />
```else``` - Solo se puede utilizar una vez dentro del Bloque anidado con if o elif<br />
## Estrutura De Repetição Ou Laços Ou Iterações
### Bucle Con Variable De Control

### For

```for x in range(Número Inicial, Número Final(Siendo el Resultado NF-1)```, cuál es la iteración (Ejemplo Sumar(1) o restar(-1)) )<br />
```for x enumerated( Variable Compuesta )``` devuelve el valor y el índice.<br />

### Bucle Con Prueba Lógica

#### While
```while not``` (Valor Booleano):<br />
```while true```: bucle infinito<br />
```break``` - interrumpe el bucle de repetición<br />
```continue``` - continúa el bucle y si el programa se salta la sección, salta a la siguiente iteración<br />



## Coleções

### Anotaciones

Puedes interpolar colecciones, por ejemplo: Diccionarios dentro de listas<br />

### Tuplas

Carácter - ()

Las tuplas son inmutables
```sorted(T```) - ordena la tupla pero no almacena el valor, para guardarlo usar variable<br />

### Listas

Caracter - []

```sum(L)``` - suma todos los valores de una lista<br />
```L.append()``` - añade un valor a la lista<br />
```L[índice]``` - muestra el elemento que está en la posición indicada<br />
```L.insert(Posición,Valor)``` - añade un valor en una posición seleccionada <br />
```L.remove()``` - elimina un valor de la lista<br />
```max(L)``` - Muestra el mayor valor de la lista<br />
```min(L)``` - Muestra el menor valor de la lista<br />
```(L).sort``` - Ordena la lista<br />
```del L[Índice]``` - Eliminar un elemento de una lista por el Índice elegido<br />
```L.pop(Índice)``` - Elimina un elemento de una lista por el Índice elegido o, si no se le pasa argumento, elimina el último valor.<br />
```L.remove(valor)``` - Elimina el elemento buscado por el valor(Contenido) definido<br />
```L1 = L2``` - el signo '=' crea un enlace entre las listas, donde cambiar una afecta a la otra<br />
```L1 = L2[:]``` - copia la lista, sin crear enlace<br />
```L1.append(L2[:])``` - Copia la lista L2 Dentro de la lista L1<br />
```L1 = [['Valor1','Valor2'],['Valor1','Valor2']]``` - Declara una lista dentro de una lista<br />
```print(L[0][0])``` - muestra el índice 0 dentro de la lista [0]<br />
```L.clear()``` - Limpia una lista<br />
```L.choice``` - Elige un elemento aleatoriamente dentro de la lista<br />

### Diccionarios

Caracter - {}

Principal diferencia con la lista: Tiene índices Literales (Letras/Palabras)<br />

```D['Índice Literal']``` = 'Valor' - Añade un valor a la variable<br />
```del D['Índice Literal']``` - Elimina el valor que está en el índice digitado. <br />
```D.values()``` - Devuelve los Valores<br />
```D.keys()``` - Devuelve los Índices Literales<br />
```D.items()``` - Devuelve tanto los Índices(Keys), como los Valores(values)<br />
```D.copy()``` - Copia los valores de un diccionario sin crear enlace, (para utilizar en bucles, etc.)<br />
```D1 = sorted(D2.items(), key=itemgetter(índice del diccionario siendo 0 para keys, y 1 para values) )``` - Ordena en orden<br /> ascendente un diccionario basado en los valores

## Cores No Terminal Python

### Ansi
```\033[Style;Text;Back;m```
```\033[0;33;44m```
### Style
0 - ninguno / none <br />
1 - negrita<br />
4 - subrayado<br />
7 - negativo<br />
### Text
30 - blanco<br />
31 - rojo<br />
32 - verde<br />
33 - amarillo<br />
34 - azul<br />
35 - magenta<br />
36 - cian<br />
37 - gris<br />
### Back
40 - blanco<br />
41 - rojo<br />
42 - verde<br />
43 - amarillo<br />
44 - azul<br />
45 - magenta<br />
46 - cian<br />
47 - gris<br />
## Conversão Base De Dados

```bin()``` - convierte de decimal a binario<br />
```oct()``` - convierte de decimal a Octal<br />
```hex()``` - convierte de decimal a hexadecimal<br />

## Funciones
### Qué Es
Son rutinas, que pueden o no devolver valores y pueden o no usar parámetros<br />
### Declaración Básica Función Sin Parámetros
```
def funcion():
 Rutina/algoritmo
 ```
    
### Declaración Básica Función Con Parámetros

```
def funcion(parametro):
    print('-'*10)
    print(parametro)
print('-'*10)
```

### Empaquetar Parámetros - Reciba Varios Parámetros
```def contador(*num)``` - recibe varios parámetros<br />



### Ayuda Interactiva
```help(función interna)``` - Devuelve una ayuda sobre una función interna <br />

### Docstrings
#### Qué Es
Cadena de documentación, es decir, Ayuda (Help) para una función creada por ti<br />
#### Cómo Crear
Una línea después de definir la función, crear 3 comillas dobles y cerrar todo lo que está adentro es el 'manual de cómo usar tu función'<br />
#### Ejemplo
```
def funcion(a,b,c):
    """
    -> aquí va una descripción directa
    :param a: Descripción del parámetro a
:param b: Descripción del parámetro b
:param c: Descripción del parámetro c
:return: si la función tiene retorno o no, y si tiene, cuál es el retorno
    """
    Aquí comienza el código de la función
```






### Parámetros Opcionales
#### Qué Es
crea parámetros que pueden o no ser insertados sin influir en la funcionalidad del programa<br />
#### Cómo Crear
colocar un valor para una variable en caso de que no sea insertada<br />
#### Ejemplo
```
def funcion(a,b,c=0(si c no recibe ningún valor, recibirá 0)):
    s = a + b + c
print(s)
```

### Alcance De Variables

#### Definición De Alcance
lugar donde existirá la variable y donde dejará de existir<br />
#### Alcance Local
existe solo en una parte del programa<br />
#### Alcance Global
existe en todas partes del programa<br />
#### Consejo
En Python, al definir una variable global y una local con el mismo nombre, se crearán 2 variables diferentes sin conexión. Para vincularlas, debes usar el comando global<br />

##### Ejemplo
```
def funcion():
    global (nombre de la variable)
    aquí comienza el código de la función
```
    

### Retorno De Resultados
#### Cómo Crear

colocar el comando return en la última línea de la función junto con una variable que contenga el valor que deseas devolver<br />

#### Ejemplo
```
def funcion(a,b,c):
    s = a + b + c
return s
```

## Modularização
### Qué Es
la separación del programa principal de las funciones<br />
### Focos
* Dividir un programa grande
* Aumentar la legibilidad
* Facilitar el mantenimiento

### Cómo Crear
Crear un archivo .py en la misma carpeta que el programa principal con el nombre deseado<br />
dentro poner todas las funciones que necesites, después en el programa principal usar ```import nombre_del_archivo```, o ```from nombre_del_archivo import nombre_de_la_funcion```

### Ventajas
* Organización del código
* Facilidad de mantenimiento
* Ocultamiento del código detallado
* Reutilización en otros proyectos

## Pacotes

### Qué Es
Una carpeta con varios módulos, permitiendo separar los módulos por tema<br />
### Cómo Crear
Solo crear una carpeta; dentro del proyecto ya se reconoce que puede ser potencialmente un paquete<br />
Siempre dentro de un paquete debe haber un archivo llamado: ```__init__.py``` donde estarán las funciones<br />
### Cuándo Utilizar
Cuando los proyectos comienzan a volverse muy grandes<br />

## Manejo De Erroress E Exceções
### Tipos De Errores
#### Sintaxis
Errores de tipeo, el comando digitado no existe<br />
#### Excepción
son errores que ocurren por una asignación incorrecta, recibir un número diferente al esperado, etc.<br />

### Manejo De Errores
#### Qué Es
verificar si es posible ejecutar algo sin que resulte en un error, y en caso de problema, realizar otro comando<br />
#### Cómo Crear
poner ```try:``` saltar línea y escribir el comando que debe intentar, luego de escribir el bloque de comando saltar línea '```except:```' saltar línea y escribir qué hacer en caso de error, y si es necesario ```else:``` y poner lo que funcionó. ```finally:```, escribe de todos modos con o sin error<br />
#### Ejemplo
```
try:
    Bloque de comando
except: / variante / except Exception as error:
    en caso de error / variante / print(error.__class__) muestra cuál fue el error
(opcional) else:
    en caso de que haya dado resultado
(opcional) finally:
    se ejecuta de cualquier manera, de resultado o error
```

#### Except
puedes crear numerosos except y especificar para cada uno de ellos cuál es el error y cómo tratar cada uno:<br />
```
except TypeError:
    Tratamiento para el error TypeError.
except ValueError:
    Tratamiento para el error ValueError
```

## Manipulação De Arquivo Txt
### Preparar Para Leer Guardar Reemplazar

```variable = open('Ruta que deseas crear/Leer', Parámetro)```

### Parámetros Para Crear Leer
```‘r’``` - Transforma en una variable lista para lectura<br />
```‘a’``` - Transforma en una variable lista para agregar texto<br />
```‘w’``` - Transforma en una variable lista para sustituir todo y poner un texto nuevo<br />
después de cada letra se puede poner el ```+``` para que, en caso de que el archivo no exista, lo cree. ejemplo: ```a+```<br />
```encoding=’utf-8’``` - Parámetro Adicional para poder realizar Edición/Lectura y Guardado de archivos con acentos<br />

### Guardar Texto

```variable_lista_para_[agregar/reemplazar]_texto.write(‘texto deseado\n’)``` (el ‘\n’ es opcional porque hace salto de línea, pero es muy recomendable porque si agregas múltiples textos no salta la línea automáticamente)<br />

### Leer Archivo De Texto

```print(variable_lista_para_leer_texto.read())``` - lee el valor del archivo incluyendo saltos de línea<br />

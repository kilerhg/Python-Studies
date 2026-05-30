````markdown
# 
# ### Ler arquivo de texto

```ex = ex1 = ex2 = ex3 = 0```<br />
reverse = True - torna algumas funções invertidas ex: ```L.sort()```<br />
função == Método<br />
toda função abre e fecha parênteses após o nome ex: f()<br />

## Tipos Primitivos
* int - inteiro
* bool - booleano / true , false
* float - números com vírgula
* str - cadeia de texto

## Operações Aritméticas
* Adição: +
* Subtração: -
* Multiplicação: *
* Divisão: /
* Potência: **
* Divisão: //
* Resto da divisão/Módulo : %
* Comparação: ==
* Recebe: =

## Ordem de precedência
1. :()
1. :**
1. :*,/,//,%
1. :+,-
## Anotações Print

dentro de um print com f string ou .format pode se utilizar ```:.3f``` dentro das chaves para definir apenas 3 número após o ponto flutuante<br />
```end=' '``` no rompe la línea<br />
Flag - Ponto de parada<br />
Consegue-se receber o mesmo valor para várias variáveis utilizando:<br />
```ceil(N)``` : redondea hacia arriba<br />
```floor(N)``` : arredonda para baixo<br />
```trunc(N)``` : trunca decimales sin redondear<br />
```pow(N)``` : potência<br />
```sqrt(N)``` : raíz cuadrada<br />
```factorial(N```) : fatorial<br />

### Random

```random()``` : genera un número aleatorio entre 0 y 1<br />
```randint(numero inicial,Numero Final)``` : gera um número aleatório inteiro em que é possível escolher o range<br />
```shuffle(L)``` : mezcla una lista<br />
# 
# ### Time

```sleep(segundos)```: hace que el proceso espere la cantidad de tiempo definida antes de continuar la ejecución<br />
# 
# ### Datetime

```date.today().year``` : año actual<br />
# 
# ### Operator

```itemgetter``` - usado para obtener elementos dentro de diccionarios<br />
# 
# ### Urllib

```urllib.request.urlopen(URL)``` - intenta acceder a un sitio web<br />
```\n``` - quebra a linha
3 aspas duplas para pegar mais de uma linha
f string - ```f'teste : {variável}'```
# 
# ## Bibliotecas
# 
# ### Math

```frase[9:21]``` - devuelve el valor de frase empezando en la posición 9 hasta la 20 (python ignora el índice final)<br />
```len(f)``` - quantidade de caracteres em uma string ou lista<br />
```(T).count()``` - cuenta la cantidad de un carácter dentro de una cadena/lista<br />
```(T).find()``` - mostra a posição de um caracter dentro de uma string / lista. se não existir ele retorna -1<br />
```(T).index(valor, inicio)``` - muestra la posición del valor buscado dentro de una variable compuesta
```in``` - retorna valor booleano<br />
```del(variable)```
 

### Transformaciones
```replace()``` - Substitui uma string/valor de lista por outra string digitada<br />
```upper()``` - convierte una cadena a mayúsculas
```lower()``` - Deixa uma string em minúsculas<br />
```capitalize()``` - convierte una cadena a minúsculas y pone la primera letra en mayúscula
```title()``` - Deixa cada palavra em uma string em maiúscula<br />
```strip()``` - elimina espacios inútiles al inicio y final de una cadena
```rstrip()``` - Remove os espaços da direita<br />
```lstrip()``` - elimina espacios a la izquierda
```variavel_com_url_site.getcode()``` - Retorna um código para a tentativa de acesso sendo 200 bem sucedido.<br />

## Manipulação de texto

### Localização

```split()``` - divide una cadena en una lista<br />
# 
# ### Junção

```'separador'.join(texto)``` - une una cadena // ejemplo '-'.join(texto) une la cadena y separa por '-'<br />
```zfill(número)``` - adiciona uma quantidade de zeros a uma string
# 
# ## Estrutura Condicional simples e composta
# 
# ### Tipos
# 
# #### Sequencial
# 
# roda o programa de forma linear de cima para baixo executando todos os comandos
# 
# #### Pythonizar
# 
Escreva tudo em uma linha exemplo:``` print('1' if var <=3 else '2')```
# 
# #### Simples
# 
# Ele executa apenas um bloco condicional
# 
# #### Composto
# 
executa mais de um bloco condicional ex : else
# 
# #### Ninhadas
# 
# Condições dentro de condições
# 
# ### if

```if``` - condicional
```Elif``` - Precisa sempre de um if<br />
```Else``` - Solo puede usarse una vez dentro del anidamiento con if o elif
# ## Estrutura de Repetição ou laços ou Iterações
# ### Laço com variável de controle
# 
# ### for

```for x in range(Número Inicial, Número Final(Resultado NF-1)```, cuál es la iteración( Ejemplo Sumar(1) o restar(-1)) )<br />
```for x enumerated( Variável Composta )``` retorna o valor e o índice.<br />

### Laço com teste lógico

#### While
```while not``` (Valor Booleano):<br />
```while true```: loop infinito<br />
```break``` - interrumpe el bucle<br />
```continue``` - continua o laço e caso o programa rode alguma parte que não contenha o continue sendo que ele existe dentro do mesmo laço ele para<br />



## Coleções

### Anotações

Você pode interpolar as coleções, por exemplo: Dicionários Dentro de listas<br />

### Tuplas

Caracter - ()

Tuplas são Imutaveis
```sorted(T)``` - ordena la tupla pero no guarda el valor; para conservarlo asignar a una variable
# 
# ### Listas
# 
Caracter - []

```sum(L)``` - suma todos los valores de una lista<br />
```L.append()``` - adiciona um valor na lista<br />
```L[índice]``` - muestra el elemento que está en la posición indicada<br />
```L.insert(Posição,Valor)``` - adiciona um valor em uma posição selecionada <br />
```L.remove()``` - elimina un valor de la lista<br />
```max(L)``` - Mostra maior valor da lista<br />
```min(L)``` - muestra el menor valor de la lista
```(L).sort``` - Ordena a lista<br />
```del L[Índice]``` - eliminar un elemento de una lista por índice seleccionado<br />
```L.pop(Índice)``` - Deletar um item de uma lista pelo Índice escolhido ou se não for entregue argumento ele remove o último valor.<br />
```L.remove(valor)``` - elimina el elemento buscado por su valor(Contenido) definido<br />
```L1 = L2``` - o sinal '=' faz um ligação entre as listas, onde a mudança de um afeta o outro

```L1 = L2[:]``` - copia la lista sin crear vínculo
```L1.append(L2[:])``` - Copia a list L2 para Dentro da lista L1<br />
```L1 = [['Valor1','Valor2'],['Valor1','Valor2']]``` - declara una lista dentro de otra lista
```print(L[0][0])``` - mostra o índice 0 dentro da lista [0]<br />
```L.clear()``` - limpia una lista
```L.choice``` - Escolhe um item aleatoriamente dentro da lista<br />

### Dicionários

Caracter - {}

Principal diferença entre a lista : Tem índices Literais (Letras/Palavras)<br />

```D['ÍndiceLiteral'] = 'Valor'``` - añade un valor a la variable<br />
```del D['Índice Literal']``` - Deleta o valor que está no índice digitado. 

```D.values()``` - devuelve los valores<br />
```D.keys()``` - Retorna os Índices Literais<br />
```D.items()``` - devuelve tanto claves como valores
```D.copy()``` - Copia os valores de um dicionário sem fazer relação, (para utilização em laços e ETC)<br />
```D1 = sorted(D2.items(), key=itemgetter(índice_del_diccionario_donde_0_son_las_claves_y_1_los_valores))``` - ordena ascendentemente un diccionario por sus valores
# 
# ## Cores no Terminal Python
# 
# ### ANSI

`````\033[Style;Text;Back;m`````
```\033[0;33;44m```
### Style
0 - none <br />
1 - bold<br />
4 - underline / sublinhado<br />
7 - negativo<br />
### Text
30 - branco<br />
31 - vermelho<br />
32 - verde<br />
33 - amarelo<br />
34 - azul<br />
35 - violeta<br />
36 - ciano<br />
37 - cinza<br />
### Back
40 - branco<br />
41 - vermelho<br />
42 - verde<br />
43 - amarelo<br />
44 - azul<br />
45 - violeta<br />
46 - ciano<br />
47 - cinza<br />
## Conversão Base de dados

```bin()``` - convertir decimal a binario<br />
```oct()``` - converter de decimal para Octal<br />
```hex()``` - convertir decimal a hexadecimal<br />

## Funções
### O que é
São rotinas, que podem ou não retornar valores e podem ou não usar parâmetros<br />
### Declaração basica função sem parâmetros
```
def funcion():
 Rutina/algoritmo
 ```
    
### Declaración básica función con parámetros


```
def funcion(parámetro):
    print('-'*10)
    print(parámetro)
print('-'*10)
```
 
### Empaquetar parámetros - aceptar varios parámetros
```string.center(Número de caracteres)``` - Centraliza o texto no Números de caracteres definidos<br />

### Divisão

```help(función_interna)``` - devuelve ayuda sobre una función interna <br />
# 
# ### Salvar texto

```
def funcion(a,b,c):
    """
    -> aquí va una descripción directa
    :param a: Descripción del parámetro a
:param b: Descripción del parámetro b
:param c: Descripción del parámetro c
:return: si la función tiene o no retorno y si lo tiene cuál es
    """
    Aquí comienza el código de la función
```




### parámetros opcionales
# 
# ### docstrings
# #### O que é
# String de documentação, ou seja Help para uma função criada por você
# #### Como criar
# Uma linha após definir a função criar 3 aspas duplas e fechar o que estiver dentro é o "manual de como usar sua função" 
# #### exemplo

```
def funcion(a,b,c=0 (si c no recibe ningún valor será 0)):
    s = a + b + c
print(s)
```

### Ámbito de Variables

#### Definição Escopo
local onde a variável vai existir e onde ela não vai mais existir<br />
#### Escopo local
existe apenas em uma parte do programa<br />
#### Escopo global
existe em todo lugar do programa<br />
#### Dica
No python quando definir uma variável global e uma local com o mesmo nome, ele irá criar 2 variáveis diferentes sem ligação, para criar ligação você deverá colocar o comando global<br />

##### Exemplo
```
def funcion():
    global (nombre de la variable)
    aquí comienza el código de la función
```
    

### retorno de resultados
#### O que é
cria Parâmetros que podem ou não serem inseridos sem influenciar na funcionalidade do programa<br />
#### Como criar
colocar um valor para uma variável caso ela não for inserida<br />
#### Exemplo
```
def funcion(a,b,c):
    s = a+b+c
return s
```

## Modularización
# ### O que é
# a separação do programa principal das funções
# ### Focos
* Dividir um programa Grande
* Aumentar a legibilidade
* Facilitar a manutenção
# 
# ### Como Criar
# Criar um arquivo .py na mesma pasta que o programa principal com o nome desejado
dentro colocar todas as funções que precisa, após isso no programa principal utilizar ```import nome_do_arquivo```, ou ```from nome_do_arquivo import nome_da_função```
# 
# ### Vantagens
* Organização do código
* Facilidade na manutenção
* Ocultação de código detalhado
* Reutilização em outros projetos
# 
# ## Pacotes
# 
# ### O que é
# Uma pasta com vários Módulos, podendo separar os módulos por assunto
# ### Como criar
# Apenas criar um pasta, dentro do projeto ele já reconhece que pode potencialmente ser um pacote
Sempre dentro de um pacote deve-se ter um arquivo chamado: ```__init__.py``` onde irá ficar as funções
# ### Quando utilizar
# Quando os projetos começam a ficar muito grandes
# 
# ## Tratamento de Erros e Exceções
# ### Tipos de Erros
# #### Sintaxe
# Erros de digitação, o comando digitado não existe
# #### Exceção
# são erros que acontecem por atribuição errada, receber número diferente do esperado e etc
# 
# ### Tratamento de Erro
# #### O que é
# verificar se algo é possível de executar sem resultar em erro, caso tenha problema realizar outro comando
# #### Como criar
colocar ```try:``` quebrar linha e escrever o comando que ele deve tentar, depois de escrever o bloco de comando quebra linha '```except:```' quebra linha, e escrever o que fazer caso tenha dado erro, e caso necessário ```else:``` e colocar o que deu certo. ```finally:```, escreve de qualquer maneira com ou sem erro
# #### Exemplo

```
try:
    Bloque de comandos
except: / variante / except Exception as error:
    si ocurrió un error / variante / print(error.__class__) muestra qué error ocurrió
(opcional) else:
    si tuvo éxito
(opcional) finally:
    se ejecuta tanto si tuvo éxito como si hubo error
```

#### except
# #### Como criar
# 
colocar o comando return na última linha da função juntamente com uma variável com o valor que deseja retornar
# 
# #### Exemplo

```
except TypeError:
    Manejo para TypeError.
except ValueError:
    Manejo para ValueError
```

## Manipulación de Archivo de texto
você pode criar inúmeros except e especificar para cada um deles qual o erro e como tratar cada um:<br />
```variable = open('Ruta para crear/Leer',Modo)```

### Parámetros para crear/Leer
```def contador(*núm)``` - recebe vários parâmetros
# 
# 
# 
# ### Interactive help

```'a'``` - abre para añadir<br />
```'r'``` - Transforma em uma variável pronta para leitura

```encoding='utf-8'``` - parámetro adicional para poder editar/leer/guardar archivos con acentos<br />
# ### Preparar para Ler Salvar Substituir

```variable_lista_para_[añadir_o_escribir].write('texto deseado\n')``` (el '\n' es opcional porque produce salto de línea, pero recomendado para que múltiples escrituras no queden juntas)<br />
```'w'``` - Transforma em um variável pronta para substituir tudo e colocar um novo texto
após cada letra pode se colocar o ```+``` para se caso o arquivo não exista ele cria, exemplo: ```a+```

```print(variable_lista_para_leer.read())``` - lee el contenido del archivo incluyendo saltos de línea<br />

````

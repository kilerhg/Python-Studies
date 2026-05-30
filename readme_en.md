  

  
  
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
```end=' '``` does not break the line<br />
```\n``` - quebra a linha
3 aspas duplas para pegar mais de uma linha
f string - ```f'teste : {variável}'```
# 
# ## Bibliotecas
# 
# ### Math

```ceil(N)``` : round up<br />
```floor(N)``` : arredonda para baixo<br />
```trunc(N)``` : truncate decimals without rounding<br />
```pow(N)``` : potência<br />
```sqrt(N)``` : square root<br />
```factorial(N```) : fatorial<br />

### Random

```random()``` : generates a random number between 0 and 1<br />
```randint(numero inicial,Numero Final)``` : gera um número aleatório inteiro em que é possível escolher o range<br />
```shuffle(L)``` : shuffles a list<br />
# 
# ### Time

```sleep(seconds)```: causes the process to wait the defined amount of time before continuing execution<br />
# 
# ### Datetime

```date.today().year``` : current year<br />
# 
# ### Operator

```itemgetter``` - used to fetch items inside dictionaries<br />
# 
# ### Urllib

```urllib.request.urlopen(URL)``` - attempts to access a website<br />
```variavel_com_url_site.getcode()``` - Retorna um código para a tentativa de acesso sendo 200 bem sucedido.<br />

## Manipulação de texto

### Localização

```frase[9:21]``` - returns the value of frase starting at position 9 up to 20 (python ignores the last index)<br />
```len(f)``` - quantidade de caracteres em uma string ou lista<br />
```(T).count()``` - counts occurrences of a character inside a string/list<br />
```(T).find()``` - mostra a posição de um caracter dentro de uma string / lista. se não existir ele retorna -1<br />
```(T).index(value, start)``` - shows the position of the searched value inside a composite variable
```in``` - retorna valor booleano<br />
```del(variable)```
 

### Transformations
```replace()``` - Substitui uma string/valor de lista por outra string digitada<br />
```upper()``` - makes a string uppercase
```lower()``` - Deixa uma string em minúsculas<br />
```capitalize()``` - makes a string lowercase and capitalizes the first letter
```title()``` - Deixa cada palavra em uma string em maiúscula<br />
```strip()``` - removes useless spaces at the beginning and end of a string
```rstrip()``` - Remove os espaços da direita<br />
```lstrip()``` - removes left-side spaces
```string.center(Número de caracteres)``` - Centraliza o texto no Números de caracteres definidos<br />

### Divisão

```split()``` - splits a string into a list<br />
# 
# ### Junção

```'separator'.join(text)``` - joins a string // example '-'.join(text) joins the string and separates by '-'<br />
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

```if``` - conditional
```'r'``` - Transforma em uma variável pronta para leitura

```Else``` - can only be used once inside the nesting with if or elif
# ## Estrutura de Repetição ou laços ou Iterações
# ### Laço com variável de controle
# 
# ### for

```for x in range(start, end (result is end-1), step (e.g. +1 or -1))```, what is the iteration (e.g. add(1) or subtract(-1)) )<br />
```for x enumerated( Variável Composta )``` retorna o valor e o índice.<br />

### Laço com teste lógico

#### While
```while not``` (Boolean Value):<br />
```while true```: loop infinito<br />
```break``` - stops the loop<br />
```continue``` - continua o laço e caso o programa rode alguma parte que não contenha o continue sendo que ele existe dentro do mesmo laço ele para<br />



## Coleções

### Anotações

Você pode interpolar as coleções, por exemplo: Dicionários Dentro de listas<br />

### Tuplas

Caracter - ()

Tuplas são Imutaveis
```sorted(T)``` - sorts the tuple but does not store the result; assign to a variable to keep it
# 
# ### Listas
# 
Caracter - []

```sum(L)``` - sums all values in a list<br />
```L.append()``` - adiciona um valor na lista<br />
```L[index]``` - shows the item at the indicated position<br />
```L.insert(Posição,Valor)``` - adiciona um valor em uma posição selecionada <br />
```L.remove()``` - removes a value from the list<br />
Flag - Ponto de parada<br />
Consegue-se receber o mesmo valor para várias variáveis utilizando:<br />
```min(L)``` - shows the smallest value in the list
```(L).sort``` - Ordena a lista<br />
```del L[index]``` - delete an item from a list by index
```L.pop(Índice)``` - Deletar um item de uma lista pelo Índice escolhido ou se não for entregue argumento ele remove o último valor.<br />
```L.remove(value)``` - remove the item searched by its value
```L1 = L2``` - o sinal '=' faz um ligação entre as listas, onde a mudança de um afeta o outro

```L1 = L2[:]``` - copies the list without linking
```L1.append(L2[:])``` - Copia a list L2 para Dentro da lista L1<br />
```L1 = [['Value1','Value2'],['Value1','Value2']]``` - declares a list inside a list
```print(L[0][0])``` - mostra o índice 0 dentro da lista [0]<br />
```L.clear()``` - clears a list
```L.choice``` - Escolhe um item aleatoriamente dentro da lista<br />

### Dicionários

Caracter - {}

Principal diferença entre a lista : Tem índices Literais (Letras/Palavras)<br />

```D['LiteralIndex'] = 'Value'``` - adds a value to the variable<br />
```del D['Índice Literal']``` - Deleta o valor que está no índice digitado. 

```D.values()``` - returns the values<br />
```D.keys()``` - Retorna os Índices Literais<br />
```D.items()``` - returns both keys and values
```D.copy()``` - Copia os valores de um dicionário sem fazer relação, (para utilização em laços e ETC)<br />
```D1 = sorted(D2.items(), key=itemgetter(index_of_dictionary_where_0_is_keys_and_1_is_values))``` - sorts a dictionary in ascending order based on values
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

```bin()``` - convert decimal to binary<br />
```Elif``` - Precisa sempre de um if<br />
```hex()``` - convert decimal to hexadecimal<br />

## Funções
### O que é
São rotinas, que podem ou não retornar valores e podem ou não usar parâmetros<br />
### Declaração basica função sem parâmetros
```
def function():
 Routine/algorithm
 ```
    
### Basic function declaration with parameters


```
def function(parameter):
    print('-'*10)
    print(parameter)
print('-'*10)
```
 
### Packing parameters - accept multiple parameters
```oct()``` - converter de decimal para Octal<br />
```help(built_in_function)``` - returns help about a built-in function <br />
# 
# ### docstrings
# #### O que é
# String de documentação, ou seja Help para uma função criada por você
# #### Como criar
# Uma linha após definir a função criar 3 aspas duplas e fechar o que estiver dentro é o "manual de como usar sua função" 
# #### exemplo

```
def function(a,b,c):
    """
    -> here goes a direct description
    :param a: Description of parameter a
:param b: Description of parameter b
:param c: Description of parameter c
:return: whether the function returns something and if so what it returns
    """
    Here begins the function code
```




### optional parameters
#### O que é
cria Parâmetros que podem ou não serem inseridos sem influenciar na funcionalidade do programa<br />
#### Como criar
colocar um valor para uma variável caso ela não for inserida<br />
#### Exemplo
```
def function(a,b,c=0 (if c receives no value it will be 0)):
    s = a + b + c
print(s)
```

### Variable Scope

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
def function():
    global (variable name)
    here begins the function code
```
    

### return values
```def contador(*núm)``` - recebe vários parâmetros
# 
# 
# 
# ### Interactive help

```
def function(a,b,c):
    s = a+b+c
return s
```

## Modularization
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
    Command block
except: / variant / except Exception as error:
    if an error occurred / variant / print(error.__class__) it shows which error occurred
(optional) else:
    if successful
(optional) finally:
    executes regardless of success or error
```

#### except
# #### Como criar
# 
colocar o comando return na última linha da função juntamente com uma variável com o valor que deseja retornar
# 
# #### Exemplo

```
except TypeError:
    Handling for TypeError.
except ValueError:
    Handling for ValueError
```

## Text File Manipulation
# ### Preparar para Ler Salvar Substituir

```variable = open('Path to create/read', Mode)```

### Parameters to create/read
```max(L)``` - Mostra maior valor da lista<br />
```'a'``` - opens for appending<br />
você pode criar inúmeros except e especificar para cada um deles qual o erro e como tratar cada um:<br />
```encoding='utf-8'``` - additional parameter to allow editing/reading/saving files with accents<br />
# 
# ### Salvar texto

```ready_variable_for_[append_or_write].write('desired text\n')``` (the '\n' is optional because it breaks the line, but recommended so multiple writes don't run together)<br />
```'w'``` - Transforma em um variável pronta para substituir tudo e colocar um novo texto
após cada letra pode se colocar o ```+``` para se caso o arquivo não exista ele cria, exemplo: ```a+```

```print(ready_variable_for_reading.read())``` - reads the file value including line breaks<br />

````

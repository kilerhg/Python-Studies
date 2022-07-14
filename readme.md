# Anotações Python

## Sumário

* [Anotações Python](#anotações-python)
* [Sumário](#sumário)
* [Anotações Gerais](#anotações-gerais)
* [Tipos Primitivos](#tipos-primitivos)
* [Operações Aritméticas](#operações-aritméticas)
* [Ordem De Precedência](#ordem-de-precedência)
* [Anotações Print](#anotações-print)
* [Bibliotecas](#bibliotecas)
  * [Math](#math)
  * [Random](#random)
  * [Time](#time)
  * [Datetime](#datetime)
  * [Operator](#operator)
  * [Urllib](#urllib)
* [Manipulação De Texto](#manipulação-de-texto)
  * [Localização](#localização)
  * [Transformações](#transformações)
  * [Divisão](#divisão)
  * [Junção](#junção)
* [Estrutura Condicional Simples E Composta](#estrutura-condicional-simples-e-composta)
  * [Tipos](#tipos)
  * [Sequencial](#sequencial)
  * [Pythonizar](#pythonizar)
  * [Simples](#simples)
  * [Composto](#composto)
  * [Ninhadas](#ninhadas)
  * [If](#if)
* [Estrutura De Repetição Ou Laços Ou Iterações](#estrutura-de-repetição-ou-laços-ou-iterações)
  * [Laço Com Variável De Controle](#laço-com-variável-de-controle)
    * [For](#for)
  * [Laço Com Teste Lógico](#laço-com-teste-lógico)
    * [While](#while)
* [Coleções](#coleções)
  * [Anotações](#anotações)
  * [Tuplas](#tuplas)
  * [Listas](#listas)
  * [Dicionários](#dicionários)
* [Cores No Terminal Python](#cores-no-terminal-python)
  * [Ansi](#ansi)
  * [Style](#style)
  * [Text](#text)
  * [Back](#back)
* [Conversão Base De Dados](#conversão-base-de-dados)
* [Funções](#funções)
  * [O Que É](#o-que-é)
  * [Declaração Basica Função Sem Parâmetros](#declaração-basica-função-sem-parâmetros)
  * [Declaração Basica Função Com Parâmetros](#declaração-basica-função-com-parâmetros)
  * [Empacotar Parâmetros - Receba Vários Parâmetros](#empacotar-parâmetros---receba-vários-parâmetros)
  * [Interactive Help](#interactive-help)
  * [Docstrings](#docstrings)
    * [O Que É](#o-que-é)
    * [Como Criar](#como-criar)
    * [Exemplo](#exemplo)
  * [Parâmetros Opcionais](#parâmetros-opcionais)
    * [O Que É](#o-que-é)
    * [Como Criar](#como-criar)
    * [Exemplo](#exemplo)
  * [Escopo De Variáveis](#escopo-de-variáveis)
    * [Definição Escopo](#definição-escopo)
    * [Escopo Local](#escopo-local)
    * [Escopo Global](#escopo-global)
    * [Dica](#dica)
    * [Exemplo](#exemplo)
  * [Retorno De Resultados](#retorno-de-resultados)
    * [Como Criar](#como-criar)
    * [Exemplo](#exemplo)
* [Modularização](#modularização)
  * [O Que É](#o-que-é)
  * [Focos](#focos)
  * [Como Criar](#como-criar)
  * [Vantagens](#vantagens)
* [Pacotes](#pacotes)
  * [O Que É](#o-que-é)
  * [Como Criar](#como-criar)
  * [Quando Utilizar](#quando-utilizar)
* [Tratamento De Erros E Exceções](#tratamento-de-erros-e-exceções)
  * [Tipos De Erros](#tipos-de-erros)
    * [Sintaxe](#sintaxe)
    * [Exceção](#exceção)
  * [Tratamento De Erro](#tratamento-de-erro)
    * [O Que É](#o-que-é)
    * [Como Criar](#como-criar)
    * [Exemplo](#exemplo)
    * [Except](#except)
* [Manipulação De Arquivo Txt](#manipulação-de-arquivo-txt)
  * [Preparar Para Ler Salvar Substituir](#preparar-para-ler-salvar-substituir)
    * [Parâmetros Para Criar Ler](#parâmetros-para-criar-ler)
  * [Salvar Texto](#salvar-texto)
  * [Ler Arquivo De Texto](#ler-arquivo-de-texto)


## Anotações gerais
Refinamento sucessivo : particionar um aplicação e realizar testes em quando desenvolve, para por exemplo evitar erros no começo meio, e corrigi los enquanto em fase de desenvolvimento.<br />
Inverter string digitada com : ```var[::-1]```<br />
Flag - Ponto de parada<br />
Consegue-se receber o mesmo valor para várias variáveis utilizando:<br />
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
```end=’ ’``` não quebra a linha<br />
```\n``` - quebra a linha<br />
3 aspas duplas para pegar mais de uma linha<br />
f string - ```f‘teste : {variável}’```

## Bibliotecas

### Math
```ceil(N)``` : arredonda para cima<br />
```floor(N)``` : arredonda para baixo<br />
```trunc(N)``` : reduz casas decimais sem arredondar<br />
```pow(N)``` : potência<br />
```sqrt(N)``` : raiz quadrada<br />
```factorial(N```) : fatorial<br />

### Random

```random()``` : gera número aleatório entre  0 e 1<br />
```randint(numero inicial,Numero Final)``` : gera um número aleatório inteiro em que é possível escolher o range<br />
```shuffle(L)``` : Embaralha uma lista<br />

### Time

```sleep(segundos)```: faz o processo aguardar a quantidade de tempo definido antes de continuar a execução<br />

### Datetime

```date.today().year``` : ano atual<br />

### Operator

```itemgetter``` - usado para buscar itens dentro de dicionários<br />

### Urllib

```urllib.request.urlopen( Url de algum site )``` - tenta acessar algum site<br />
```variavel_com_url_site.getcode()``` - Retorna um código para a tentativa de acesso sendo 200 bem sucedido.<br />

## Manipulação de texto

### Localização

```frase[9:21]``` - Retorna o valor de frase começando na posição 9 e indo até a 20 (o python desconsidera a última)<br />
```len(f)``` - quantidade de caracteres em uma string ou lista<br />
```(T).count()``` - conta a quantidade de um caracter dentro de uma string / list<br />
```(T).find()``` - mostra a posição de um caracter dentro de uma string / lista. se não existir ele retorna -1<br />
```(T).index(Valor procurado, Início)``` - mostra a posição  do valor procurado dentro de uma variável composta<br />
```in``` - retorna valor booleano<br />
```del(Variável)```
 


### Transformações
```replace()``` - Substitui uma string/valor de lista por outra string digitada<br />
```upper()``` - Deixa uma string em maiúsculo<br />
```lower()``` - Deixa uma string em minúsculas<br />
```capitalize()``` - Deixa uma string em minúscula e coloca a primeira letra em maiúscula<br />
```title()``` - Deixa cada palavra em uma string em maiúscula<br />
```strip()``` - Remove os espaços inúteis antes do começo da string e no final<br />
```rstrip()``` - Remove os espaços da direita<br />
```lstrip()``` - Remove os espaços da esquerda<br />
```string.center(Número de caracteres)``` - Centraliza o texto no Números de caracteres definidos<br />

### Divisão

```split()``` - Divide uma string em uma lista<br />

### Junção
```'separador'join(frase)``` - junta um string // exemplo ‘-’.join(frase) junta a string e separa por ‘-’<br />
```zfill(número)``` - adiciona uma quantidade de zeros a uma string<br />

## Estrutura Condicional simples e composta

### Tipos

#### Sequencial

roda o programa de forma linear de cima para baixo executando todos os comandos<br />

#### Pythonizar

Escreva tudo em uma linha exemplo:``` print(‘1’ if var <=3 else ‘2’)```

#### Simples

Ele executa apenas um bloco condicional<br />

#### Composto

executa mais de um bloco condicional ex : else<br />

#### Ninhadas

Condições dentro de condições<br />

### if
```if``` - ```se```
```Elif``` - Precisa sempre de um if<br />
```Else``` - So pode ser utilizado uma vez dentro da Ninhada com if ou elif<br />
## Estrutura de Repetição ou laços ou Iterações
### Laço com variável de controle

### for

```for x in range(Número Inicial, Número Final(Sendo o Resultado NF-1)```, qual é a iteração( Exemplo Somar(1) ou subtrair(-1)) )<br />
```for x enumerated( Variável Composta )``` retorna o valor e o índice.<br />

### Laço com teste lógico

#### While
```while not``` (Valor Booleano):<br />
```while true```: loop infinito<br />
```break``` - interrompe o laço de repetição<br />
```continue``` - continua o laço e caso o programa rode alguma parte que não contenha o continue sendo que ele existe dentro do mesmo laço ele para<br />



## Coleções

### Anotações

Você pode interpolar as coleções, por exemplo: Dicionários Dentro de listas<br />

### Tuplas

Caracter - ()

Tuplas são Imutaveis
```sorted(T```) - ordena a tupla porém não armazena o valor, para guardar usar variável<br />

### Listas

Caracter - []

```sum(L)``` - soma todos os valores de uma lista<br />
```L.append()``` - adiciona um valor na lista<br />
```L[índice]``` - mostra o item que está na posição indicada<br />
```L.insert(Posição,Valor)``` - adiciona um valor em uma posição selecionada <br />
```L.remove()``` - remove um valor da lista<br />
```max(L)``` - Mostra maior valor da lista<br />
```min(L)``` - Mostra o menor valor da lista<br />
```(L).sort``` - Ordena a lista<br />
```del L[Índice]``` - Deletar um item de uma lista pelo Índice escolhido<br />
```L.pop(Índice)``` - Deletar um item de uma lista pelo Índice escolhido ou se não for entregue argumento ele remove o último valor.<br />
```L.remova(valor)``` - Remova o item procurado pelo valor(Conteúdo) definido<br />
```L1 = L2``` - o sinal ‘=’ faz um ligação entre as listas, onde a mudança de um afeta o outro<br />
```L1 = L2[:]``` - copia a lista, não tendo ligação<br />
```L1.append(L2[:])``` - Copia a list L2 para Dentro da lista L1<br />
```L1 = [[‘Valor1’,’Valor2’],[‘Valor1’,’Valor2’]]``` - Declara uma lista dentro de lista<br />
```print(L[0][0])``` - mostra o índice 0 dentro da lista [0]<br />
```L.clear()``` - Limpa uma lista<br />
```L.choice``` - Escolhe um item aleatoriamente dentro da lista<br />

### Dicionários

Caracter - {}

Principal diferença entre a lista : Tem índices Literais (Letras/Palavras)<br />

```D[‘Índice Literal’]``` = ‘Valor’ - Adiciona um valor a variável<br />
```del D[‘Índice Literal’]``` - Deleta o valor que está no índice digitado. <br />
```D.values()``` - Retorna os Valores<br />
```D.keys()``` - Retorna os Índices Literais<br />
```D.items()``` - Retorna tanto os Índices(Keys), como os Valores(values)<br />
```D.copy()``` - Copia os valores de um dicionário sem fazer relação, (para utilização em laços e ETC)<br />
```D1 = sorted(D2.items(), key=itemgetter(índice do dicionário sendo 0 as keys, e 1 os valores) )``` - Ordena em ordem<br /> crescente um dicionário com base nos valores

## Cores no Terminal Python

### ANSI
```\033[Style;Text;Back;m```
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

```bin()``` - converter de decimal para binário<br />
```oct()``` - converter de decimal para Octal<br />
```hex()``` - converter de decimal para hexadecimal<br />

## Funções
### O que é
São rotinas, que podem ou não retornar valores e podem ou não usar parâmetros<br />
### Declaração basica função sem parâmetros
```
def funcao():
 Rotina/algoritmo
 ```
    
### Declaração basica função com parâmetros

```
def funcao(parâmetro):
    print(‘-’*10)
    print(parâmetro)
print(‘-’*10)
```

### Empacotar parâmetros - Receba vários parâmetros
```def contador(*núm)``` - recebe vários parâmetros<br />



### Interactive help
```help(função interna)``` - Retorna uma ajuda sobre uma função interna <br />

### docstrings
#### O que é
String de documentação, ou seja Help para uma função criada por você<br />
#### Como criar
Uma linha após definir a função criar 3 aspas duplas e fechar o que estiver dentro é o ”manual de como usar sua função” <br />
#### exemplo
```
def funcao(a,b,c):
    “””
    -> aqui vai uma descrição direta
    :param a: Descrição do parâmetro a
:param b: Descrição do parâmetro b
:param c: Descrição do parâmetro c
:return: se a função tem ou não retorno se tiver qual o retorno
    “””
    Aqui começa o código da função
```






### parâmetros opcionais
#### O que é
cria Parâmetros que podem ou não serem inseridos sem influenciar na funcionalidade do programa<br />
#### Como criar
colocar um valor para uma variável caso ela não for inserida<br />
#### Exemplo
```
def funcao(a,b,c=0(caso c não receba nenhum valor ele irá receber 0)):
    s = a + b + c
print(s)
```

### Escopo de Variáveis

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
def funcao():
    global (nome da variável)
    aqui começa o código da função
```
    

### retorno de resultados
#### Como criar

colocar o comando return na última linha da função juntamente com uma variável com o valor que deseja retornar<br />

#### Exemplo
```
def funcao(a,b,c):
    s = a+b+c
return s
```

## Modularização
### O que é
a separação do programa principal das funções<br />
### Focos
* Dividir um programa Grande
* Aumentar a legibilidade
* Facilitar a manutenção

### Como Criar
Criar um arquivo .py na mesma pasta que o programa principal com o nome desejado<br />
dentro colocar todas as funções que precisa, após isso no programa principal utilizar ```import nome_do_arquivo```, ou ```from nome_do_arquivo import nome_da_função```

### Vantagens
* Organização do código
* Facilidade na manutenção
* Ocultação de código detalhado
* Reutilização em outros projetos

## Pacotes

### O que é
Uma pasta com vários Módulos, podendo separar os módulos por assunto<br />
### Como criar
Apenas criar um pasta, dentro do projeto ele já reconhece que pode potencialmente ser um pacote<br />
Sempre dentro de um pacote deve-se ter um arquivo chamado: ```__init__.py``` onde irá ficar as funções<br />
### Quando utilizar
Quando os projetos começam a ficar muito grandes<br />

## Tratamento de Erros e Exceções
### Tipos de Erros
#### Sintaxe
Erros de digitação, o comando digitado não existe<br />
#### Exceção
são erros que acontecem por atribuição errada, receber número diferente do esperado e etc<br />

### Tratamento de Erro
#### O que é
verificar se algo é possível de executar sem resultar em erro, caso tenha problema realizar outro comando<br />
#### Como criar
colocar ```try:``` quebrar linha e escrever o comando que ele deve tentar, depois de escrever o bloco de comando quebra linha ‘```except:```’ quebra linha, e escrever o que fazer caso tenha dado erro, e caso necessário ```else:``` e colocar o que deu certo. ```finally:```, escreve de qualquer maneira com ou sem erro<br />
#### Exemplo
```
try:
    Bloco de comando
except: / variante / except Exception as erro:
    caso tenha dado erro / variante / print(erro.__class__ ) ele mostra qual erro foi o erro
(opcional) else:
    caso tenha dado certo 
(opcional) finally:
    executa de qualquer maneira dando certo ou errado
```

#### except
você pode criar inúmeros except e especificar para cada um deles qual o erro e como tratar cada um:<br />
```
except TypeError:
    Tratamento para o erro TypeError.
except ValueError:
    Tratamento para o erro ValueError
```

## Manipulação de Arquivo txt
### Preparar para Ler Salvar Substituir

```variável = open(‘Caminho que deseja criar/Ler’,Parâmetro)```

### Parâmetros para criar Ler
```‘r’``` - Transforma em uma variável pronta para leitura<br />
```‘a’``` - Transforma em uma variável pronta para adicionar texto<br />
```‘w’``` - Transforma em um variável pronta para substituir tudo e colocar um novo texto<br />
após cada letra pode se colocar o ```+``` para se caso o arquivo não exista ele cria, exemplo: ```a+```<br />
```encoding=’utf-8’``` - Parâmetro Adicional para poder fazer qualquer Edição/Leitura e Salvamento de arquivos com acentos<br />

### Salvar texto

```variável_pronta_para_[adicionar/substituir]_texto.write(‘texto desejado\n’)``` (o ‘\n’ é opcional pois ele quebra linha, porém é extremamente recomendado pois caso adicione mais de um texto ele não quebra automaticamente a linha)<br />

### Ler arquivo de texto

```print(variável_pronta_para_ler_texto.read())``` - lê o valor do arquivo inclusive com quebra linhas<br />

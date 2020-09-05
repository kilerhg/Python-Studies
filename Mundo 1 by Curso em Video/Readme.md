# Curso python mundo 1 By [Curso em Video](https://cursoemvideo.com)
## Anotações gerais
len() - conta número de itens dentro de uma variável
lista se escreve com []
choice : escolhe um item dentro de uma lista
Refinamento sucessivo : particionar um aplicação e realizar testes em quando desenvolve, para por exemplo evitar erros no começo meio, e corrigi los enquanto em fase de desenvolvimento.
## Tipos de variáveis / Tipos primitivos
 * int - inteiro
* bool - booleano / true , false
* float - números com vírgula
* str - cadeia de texto
* list - lista
## Operações Aritméticas
* Adição: +
* Subtração: -
* Multiplicação: *
* Divisão: /
* Potência: **
* Divisão Inteira: //
* Resto da divisão/Módulo : %
* Comparação: ==
* Recebe: =


## Ordem de precedência
1. ()
1. **
1. *,/,//,%
1. +,-
## Anotações Print
dentro de um print com f string ou .format pode se utilizar ```:.3f``` dentro das chaves para definir apenas 3 número após o ponto flutuante
```end=’ ’```não quebra a linha
```\n``` - quebra a linha
3 aspas duplas para pegar mais de uma linha

## Bibliotecas
### Math
ceil : arredonda para cima
floor : arredonda para baixo
trunc : reduz casas decimais sem arredondar
pow : potência
sqrt : raiz quadrada
factorial : fatorial
### Random
random : gera número aleatório entre  0 e 1
radint : gera um número aleatório inteiro em que é possível escolher o range
Shuffle : Embaralha uma lista
### Time
timedelta : efetuar cálculos com tempo. exemplo duração.
```sleep(segundos)```: faz o processo aguardar a quantidade de tempo definido antes de continuar a execução
### Datetime
```date.today().year``` : ano atual




## Manipulação de texto
### Localização
```frase[9:21]``` - Retorna do caracter 9 até o 20 (sempre termina um antes do selecionado)
```len(f)``` - quantidade de caracteres em uma string ou lista
```count()``` - conta a quantidade de um caracter dentro de uma string / list
```find()``` - mostra a posição de um caracter dentro de uma string / lista. se não existir ele retorna -1
```in``` - retorna valor booleano
 
### transformações

```replace()``` - Substitui uma string/valor de lista por outra string digitada
```upper()``` - Deixa uma string em maiúsculo
```lower()``` - Deixa uma string em minúsculas
```capitalize()``` - Deixa uma string em minúscula e coloca a primeira letra em maiúscula
```title()``` - Deixa cada palavra em uma string em maiúscula
```strip()``` - Remove os espaços inúteis antes do começo da string e no final
```rstrip()``` - Remove os espaços da direita
```lstrip()``` - Remove os espaços da esquerda
### Divisão
```split()``` - Divide uma string em uma lista
### Junção
```join()``` - junta um string // exemplo ‘-’.join(frase) junta a string e separa por ‘-’
```zfill(número)``` - adiciona uma quantidade de zeros a uma string
## Estrutura Condicional simples e composta
### Sequencial
roda o programa de forma linear de cima para baixo executando todos os comandos
### Pythonizar
Escreva tudo em uma linha exemplo: ```print(‘1’ if var <=3 else ‘2’)```
### Simples
Ele executa apenas um bloco condicional
### Composto
executa mais de um bloco condicional ex : else
## Cores no Terminal Python
### ANSI
```\033[Style;Text;Back;m```
```\033[0;33;44m```
### Style  / Estilo
0 - none
1 - bold
4 - underline / sublinhado
7 - negativo
### Text / Cores
30 - branco
31 - vermelho
32 - verde
33 - amarelo
34 - azul
35 - violeta
36 - ciano
37 - cinza
### Back / Fundo
40 - branco
41 - vermelho
42 - verde
43 - amarelo
44 - azul
45 - violeta
46 - ciano
47 - cinza

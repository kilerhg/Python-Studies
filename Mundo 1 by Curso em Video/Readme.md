# Curso python mundo 1 By [Curso em Video](https://cursoemvideo.com)
## Anotações gerais
len() - conta número de itens dentro de uma variável<br />
lista se escreve com []<br />
choice : escolhe um item dentro de uma lista<br />
Refinamento sucessivo : particionar um aplicação e realizar testes em quando desenvolve, para por exemplo evitar erros no começo meio, e corrigi los enquanto em fase de desenvolvimento.<br />
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
dentro de um print com f string ou .format pode se utilizar ```:.3f``` dentro das chaves para definir apenas 3 número após o ponto flutuante<br />
```end=’ ’```não quebra a linha<br />
```\n``` - quebra a linha<br />
3 aspas duplas para pegar mais de uma linha<br />

## Bibliotecas
### Math
ceil : arredonda para cima<br />
floor : arredonda para baixo<br />
trunc : reduz casas decimais sem arredondar<br />
pow : potência<br />
sqrt : raiz quadrada<br />
factorial : fatorial<br />
### Random
random : gera número aleatório entre  0 e 1<br />
radint : gera um número aleatório inteiro em que é possível escolher o range<br />
Shuffle : Embaralha uma lista<br />
### Time
timedelta : efetuar cálculos com tempo. exemplo duração.<br />
```sleep(segundos)```: faz o processo aguardar a quantidade de tempo definido antes de continuar a execução<br />
### Datetime
```date.today().year``` : ano atual<br />




## Manipulação de texto
### Localização
```frase[9:21]``` - Retorna do caracter 9 até o 20 (sempre termina um antes do selecionado)<br />
```len(f)``` - quantidade de caracteres em uma string ou lista<br />
```count()``` - conta a quantidade de um caracter dentro de uma string / list<br />
```find()``` - mostra a posição de um caracter dentro de uma string / lista. se não existir ele retorna -1<br />
```in``` - retorna valor booleano<br />
 
### transformações

```replace()``` - Substitui uma string/valor de lista por outra string digitada<br />
```upper()``` - Deixa uma string em maiúsculo<br />
```lower()``` - Deixa uma string em minúsculas<br />
```capitalize()``` - Deixa uma string em minúscula e coloca a primeira letra em maiúscula<br />
```title()``` - Deixa cada palavra em uma string em maiúscula<br />
```strip()``` - Remove os espaços inúteis antes do começo da string e no final<br />
```rstrip()``` - Remove os espaços da direita<br />
```lstrip()``` - Remove os espaços da esquerda<br />
### Divisão
```split()``` - Divide uma string em uma lista<br />
### Junção
```join()``` - junta um string // exemplo ‘-’.join(frase) junta a string e separa por ‘-’<br />
```zfill(número)``` - adiciona uma quantidade de zeros a uma string<br />
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
0 - none<br />
1 - bold<br />
4 - underline / sublinhado<br />
7 - negativo<br />
### Text / Cores
30 - branco<br />
31 - vermelho<br />
32 - verde<br />
33 - amarelo<br />
34 - azul<br />
35 - violeta<br />
36 - ciano<br />
37 - cinza<br />
### Back / Fundo
40 - branco<br />
41 - vermelho<br />
42 - verde<br />
43 - amarelo<br />
44 - azul<br />
45 - violeta<br />
46 - ciano<br />
47 - cinza<br />

'''
Estudos sobre funções: **kwargs

Semelhante ao *args, o **kwargs aceita outro nome, desde que se inicie com **.

ele também funciona semelhante ao aceitar nenhum ou diversos parametros, sendo opcionais e trabalhando junto com parametros tradicionais.

a diferença dele está que se precisa passar 'nome=valor' sempre, assim ao final do dia temos um dicionario com chave:valor,

exemplo:

def sorteio(**kwargs):
    return kwargs


print(sorteio(caio=5,vanessa=10,lucas=2,roberto=1))

Em funções python existe uma ordem de parametros que se deve seguir:

- Parametros obrigatórios
- *args
- parametros opcionais
- **kwargs


def habitos_pessoas(nome,idade,*args,trabalha=False,**kwargs):
    print(f'nome {nome}, idade {idade}')
    if trabalha:
        print('trabalhando')
    else:
        print('nao trabalhando')
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')

habitos_pessoas('carlos',15,1,1,1,1,1,rorto='sim',casaco=2)

Praticando desempacotamento de * & **

def soma_valores(a,b,c):
    print(a+b+c)

lista = [1,2,3]
tupla = (1,2,3)
conjunto = {1,2,3}

soma_valores(*lista)
soma_valores(*tupla)
soma_valores(*conjunto)

dicionario = {'a':1,'b':2,'c':3}

soma_valores(**dicionario)

Utilizado:
    ** você desempacota o dicionario em variavel=valor, em vez do tradicional chave:valor
    * você desempacota a lista em 3 variaveis com nome de variavel qualquer.

!! Atenção, ao utilizar ** ele retorna com o mesmo nome da chave, então a função tem que ter o parametro com nome idêntico. gerando TypeError

'''



'''
Estudos sobre funções: *args

Pode se chamar qualquer nome desde que tenha * como inicio, exemplo: def ola(*teste)

Com o args podemos dar um passo a mais com parametros opcionais, recebendo nenhum ou diversos valores:

def printa_valor(*args):
    for arg in args:
        print(arg)

também pode se receber parametros tradicionais e o *args

def cadastra(nome,telefone,*args):
    dicionario_cadastro = {}
    dicionario_cadastro['nome'] = nome
    dicionario_cadastro['telefone'] = telefone
    dicionario_cadastro['cursos'] = args
    return dicionario_cadastro

Desempacotando

Utilizando *variavel na utilização de uma função, o python desempacota o valor antes de passar para a função:
exemplo:

def soma_valores(*args):
    print(args)
return sum(args)

lista = [1,2,3,4,5]

print(soma_valores(*lista))

'''





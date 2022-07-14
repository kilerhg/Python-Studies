'''
Estudos sobre comprehensions: listas

O que é: Gera uma lista que pode ser tratada e processada até mesmo com funções em tempo de execução a partir de um iterável.

Sintaxe: 

var = [num + 1 for num in iteravel]

teste = [1,2,3,4,5]

var = [num * 1000 for num in teste]

print(var)

def verifica_valor(numero):
    if str(numero).isnumeric():
        numero = int(numero)
    else:
        numero = str(numero)
    return numero


minha_lista = [1,2,3,'cinco','44','a1','10101','teste',10.1,'10.1']
var = [verifica_valor(num) for num in minha_lista]
print(var)
'''

'''
Adicionando validações em compreehensions

sintaxe:

[numero for numero in lista if numero > 10]

Adicionando else

sintaxe:

[numero + 1 if numero == 1 else numero + 2 for numero in lista]



lista = range(20)

# menor_10 = [bool(numero % 2) for numero in lista if numero < 10]
# maior_10 = [bool(numero % 2) for numero in lista if numero > 10]

# calculo = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in lista]
calculo = [numero + 1 if numero == 1 else numero + 2 for numero in lista]
print(calculo)
# print(menor_10)
# print(maior_10)
'''


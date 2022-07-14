# digitar 7 valores numericos e cadastra-los em uma lista unica que mantenha separado os numeros pares e os numeros impares, no final mostre os valores pares e impares de forma crescente
"""

Alternativa

cria = list()
lista = list()
lista.append(cria[:])
lista.append(cria[:])
"""

lista = [[],[]]

for x in range(0,7):
    valor = int(input(f'Digite um valor {x+1}: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print(f'Os Valores pares São: {lista[0]}')
print(f'Os Valores Impares São: {lista[1]}')

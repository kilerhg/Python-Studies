# aprimore o desafio 86 mostrando no final:
# A - A soma de todos os valores pares digitados
# B - A soma dos valores da terceira coluna
# C - O maior valor da segunda linha
"""

    Alternativa

lista = list()
lista0 = list()
lista.append(lista0[:])
lista.append(lista0[:])
lista.append(lista0[:])
lista.append(lista0[:])

"""

lista = [[],[],[],[]]

ct = 0
for x in range(0,3):
    for c in range(0,3):
        valor = int(input(f'Digite o valor [{x}]:[{c}] :'))
        lista[x].append(valor)
        if valor % 2 == 0:
            lista[3].append(valor)
print(f'''
{'+-+'*15}
 {' '*5}[{lista[0][0]: ^5}]{' '*5}[{lista[0][1]: ^5}]{' '*5}[{lista[0][2]: ^5}]
 {' '*5}[{lista[1][0]: ^5}]{' '*5}[{lista[1][1]: ^5}]{' '*5}[{lista[1][2]: ^5}]
 {' '*5}[{lista[2][0]: ^5}]{' '*5}[{lista[2][1]: ^5}]{' '*5}[{lista[2][2]: ^5}]
{'+-+'*15}
''')
print(f'A soma de todos os valores pares é: {sum(lista[3])}')
print(f'A soma de todos os valores da terceira linha é: {lista[0][2] + lista[1][2] + lista[2][2]}')
print(f'O maior valor da segunda linha é: {max(lista[1])}')

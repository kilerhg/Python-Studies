# crie uma matriz de dimensao 3x3 e preencha com valores lidos pelo teclado
"""

    Alternativa

lista = list()
lista0 = list()
lista1 = list()
lista2 = list()
lista.append(lista0)
lista.append(lista1)
lista.append(lista2)
"""

lista = [[],[],[]]

ct = 0
for x in range(0,3):
    for c in range(0,3):
        valor = int(input(f'Digite o valor [{x}]:[{c}] :'))
        lista[x].append(valor)
print(f'''
{'+-+'*15}
 {' '*5}[{lista[0][0]: ^5}]{' '*5}[{lista[0][1]: ^5}]{' '*5}[{lista[0][2]: ^5}]
 {' '*5}[{lista[1][0]: ^5}]{' '*5}[{lista[1][1]: ^5}]{' '*5}[{lista[1][2]: ^5}]
 {' '*5}[{lista[2][0]: ^5}]{' '*5}[{lista[2][1]: ^5}]{' '*5}[{lista[2][2]: ^5}]
{'+-+'*15}
''')

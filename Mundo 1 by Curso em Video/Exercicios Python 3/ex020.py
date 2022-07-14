# leia quatro nomes e mostre em uma ordem

from random import shuffle


n1 = input('Digite um nome:')
n2 = input('Digite um nome:')
n3 = input('Digite um nome:')
n4 = input('Digite um nome:')
lista = [n1,n2,n3,n4]
shuffle(lista)
number = 0
for x in lista:
    number += 1
    print(f' O Nome do aluno {number}: {x}')

'''
resultado = list()
number = 0

for x in range(0,4):
    random = randint(0,len(lista))
   resultado.append(lista[random-1])
   del lista[random-1]


for x in resultado:
    number += 1
    print(f' O Nome do aluno {number}: {x}')
'''







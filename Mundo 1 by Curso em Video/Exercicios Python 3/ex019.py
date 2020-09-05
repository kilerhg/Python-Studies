# leia quatro nomes e escolha um
from random import randint
n1 = input('Digite um nome:')
n2 = input('Digite um nome:')
n3 = input('Digite um nome:')
n4 = input('Digite um nome:')

lista = [n1, n2, n3, n4]
numerorand = randint(0,3)
print(f'Aluno Sorteado: {lista[numerorand]}')
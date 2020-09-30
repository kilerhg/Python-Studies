# crie um modulo chamado moeda.py que tenha as funções incorporadas
# aumentar(),
# diminuir()
# dobro()
# metade()
# faça tambem um programa que importe esse modulo e use algumas dessas funções
# 

from ex107.moeda import *


n1 = int(input('Digite um numero:'))
print(f'O dobro de R${n1} é R${dobro(n1)}')
print(f'A metade de R${n1} é R${metade(n1)}')
print(f'O numero R${n1} com {10}% de aumento fica: R${aumentar(n1,10)}')
print(f'O numero R${n1} com {10}% de redução fica: R${diminuir(n1,10)}')


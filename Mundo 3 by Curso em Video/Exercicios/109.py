# modifique as funcoes que foram criadas no desafio 107, para que elas aceitem um parametro a mais, informando se o valor retornado por elas vai ser
# ou nao formatado pela função moeda(), desenvolvida no desafio 108
# 

from ex109.moeda import *


n1 = float(input('Digite um Valor:'))
n2 = float(input('Digite as Porcentagens:'))
print('-*'*30)
print(f'O dobro  de {moeda(n1)} é   {dobro(n1,True)}')
print(f'A metade de {moeda(n1)} é   {metade(n1,True)}')
print(f'O numero    {moeda(n1)} com {n2}% de aumento fica: {aumentar(n1,n2,True)}')
print(f'O numero    {moeda(n1)} com {n2}% de redução fica: {diminuir(n1,n2,True)}')
print('-*'*30)
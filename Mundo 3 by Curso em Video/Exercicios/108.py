# adapte o codigo do desafio 107, criando uma função adicional chamada moeda(), que consiga mostrar os valores como um valor monetario formatado
# 

from ex108.moeda import *

n1 = float(input('Digite um Valor:'))
n2 = float(input('Digite as Porcentagens:'))
print('-*'*30)
print(f'O dobro  de {moeda(n1)} é {moeda(dobro(n1))}')
print(f'A metade de {moeda(n1)} é {moeda(metade(n1))}')
print(f'O numero {moeda(n1)} com {n2}% de aumento fica: {moeda(aumentar(n1,n2))}')
print(f'O numero {moeda(n1)} com {n2}% de redução fica: {moeda(diminuir(n1,n2))}')
print('-*'*30)
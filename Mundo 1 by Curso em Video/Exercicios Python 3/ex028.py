# gerar numero random entre 0 e 5, pedir um numero ao usuario e verificar se está correto, caso sim venceu senão perdeu.
from random import randint
pc = randint(0,5)
print(f'''
{'_--_'*12}
Vou pensar em um numero entre o e 5... advinhe-o
{'_--_'*12}
''')

usuario = int(input('Tentea advinhar o numero que pensei:'))
if usuario == pc:
    print('Você acertou')
else:
    print(f'Você errou colocando {usuario}, o computador escolheu: {pc}')
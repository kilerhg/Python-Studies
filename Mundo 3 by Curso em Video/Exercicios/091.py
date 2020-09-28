# 4 jogadores joguem um dado (1 a 6) e tenham resultados aleatorios, guarde esses resultados em um dicionario, no final coloque esse dicionario em ordem,
# sabendo que o vencedor tirou o maior numero no dado.

from random import randint
from time import sleep

jogo = {}
jogoord = {}
valores = []
for x in range(0,4):
    jogo[f'Jogador {x}'] = randint(1,6)
for x in jogo.values():
    valores.append(x)
valores.sort(reverse=True)
for pos,x in enumerate(valores):
    for k,v in jogo.items():
        if v == x:
            jogoord[k] = v


#    if v == max(jogo.values()):
#        jogoord[k] = v
print(f'{"Valores Escolhidos":-^40}')
ct = 1
for k,v in jogo.items():
    sleep(.5)
    print(f'O {k} Escolheu: {v}')
    ct += 1
print(f'{"Ranking Dos Jogadores":-^40}')
ct = 1
for k,v in jogoord.items():
    sleep(.5)
    print(f'{ct} Lugar : {k} com Numero: {v}')
    ct += 1




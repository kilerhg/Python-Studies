# Computador pensar em um numero entre 0 e 10, porem o jogador vai tentando advinhar até acertar, e no final mostrar quantos palpiter foram necessarios

from random import randint
vpc = int(randint(0,10))
vus = -1
sm = 0
while not vpc == vus:
    print('= ='*10)
    vus = int(input('Tente Advinhar o Numero Que o computador está pensando:'))
    if vpc != vus:
        if vpc > vus:
            print(f'{vus} não é o numero que pensei, Tente um Maior ;)!!')
        else:
            print(f'{vus} não é o numero que pensei, Tente um Menor!!')

    sm += 1
print(f'Parabens {vus} é o Numero que pensei, Você precisou apenas de {sm} Tentativas')


# jogue par ou impar com o computador, o jogo so sera interrompido quando o jogador perder, mostrando o total de vitorias consecutivas.
from random import randint
vc = 0
while True:
    vus = int(input('Digite um valor inteiro para jogar:'))
    while not vus <= 10:
        vus = int(input('Digite um valor inteiro para jogar:'))
    tus = str(input('Par ou Impar [P/I]')).strip()[0]
    if tus in 'Pp':
        tus = 0
    elif tus in 'Ii':
        tus = 1
    else:
        while tus not in 'PpIi':
            tus = str(input('Par ou Impar [P/I]')).strip()[0]
    print('= =' * 20)
    vpc = int(randint(1,10))
    if tus == 0:
        tpc = 1
    else:
        tpc = 0
    if (vus + vpc) % 2 == 0:
        res = 0
        nres = 'Par'
    else:
        res = 1
        nres = 'Impar'
    if tus == res:
        print(f'Você Venceu escolhendo : {vus}\nEnquando o computador escolheu {vpc}\ndando soma {vus + vpc}\nSendo {nres}')
        vc += 1
    else:
        print(f'Você Perdeu escolhendo : {vus}\nEnquando o computador escolheu {vpc}\ndando soma {vus + vpc}\nSendo {nres}\nCom {vc} Vitorias Seguidas!!')
        break


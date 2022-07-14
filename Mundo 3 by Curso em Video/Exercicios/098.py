# uma funcao  que receba tres parametros, inicio fim e passo e realize a contagem
# seu progama tem que realizar tres contagens atraves da funcao criada
# A- De 1 até 10 de 1 em 1
# B- De 10 até 0 de 2 em 2
# C- uma contagem personalizada com valores rebebidos de input do usuario
from time import sleep


def contador(inicio, fim, passo):
    p = passo
    if p < 0:
        p *= -1
    print('*-'*20)
    if inicio > fim:
        cont = inicio + passo
        if passo > 0:
            passo *= -1
    else:
        cont = inicio - passo
        if passo < 0:
            passo *= -1

    if passo == 0:
        passo = 1

    print(f'Contagem de {inicio} até {fim} indo de {p} em {p}')
    for x in range(inicio,fim+passo,passo):
        if inicio > fim:
            if x < fim:
                break
        else:
            if x > fim:
                break
        sleep(0.2)
        print(f'{x} ', end='', flush=True)

    '''
    
        Alternativa Sem utilizar For
        
    if inicio > fim:
        cont = inicio + passo
        passo *= -1
        while cont > fim:
            cont += passo
            if cont < fim:
                break
            sleep(.1)
            print(f'{cont} ', end='', flush=True)
    else:
        cont = inicio - passo
        while cont < fim:
            cont += passo
            if cont > fim:
                break
            sleep(.1)
            print(f'{cont} ', end='', flush=False)
    '''
    print()


contador(0,10,1)
contador(10,0,2)
n1 = int(input('Digite o valor de inicio:'))
n2 = int(input('Digite o valor de fim:'))
n3 = int(input('Digite de quanto em quanto:'))
contador(n1,n2,n3)

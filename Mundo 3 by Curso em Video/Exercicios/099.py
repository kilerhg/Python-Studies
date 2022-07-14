# uma funcao que receba varios parametros com valores inteiros, seu programa tem que analisar todos os valores e dizer qual deles é o maior
from time import sleep
def maior(*numeros):
    print('*-'*25)
    print('Analizando os valores......')
    print('Os Numero do grupo são: ', end='')
    for x in numeros:
        sleep(.5)
        print(f'{x} ',end='')
    print(f' Ao todo foram informados {len(numeros)} Numeros')
    if len(numeros) != 0:
        print(f'O maior valor do grupo é: {max(numeros)}')
    else:
        print('O maior valor do grupo é: 0')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

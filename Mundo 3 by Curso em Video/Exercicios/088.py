# Cria grupo com 6 numeros aleatorios sem repetir entre 1 e 60. o usuario ira digitar a quantidade de grupos
from time import sleep
from random import randint
qtd = int(input('Digite a quantidade de Jogos: '))
lista = list()
jogo = list()
for x in range(0,qtd):
    for x in range(0,6):
        valor = randint(1,60)
        if x == 0:
            jogo.append(valor)
        else:
            while True:
                valor = randint(1,60)
                if valor not in jogo:
                    break
            jogo.append(valor)
    lista.append(jogo[:])
    jogo.clear()
print(f'{"Gerador Jogos":-^30}')
for num,x in enumerate(lista):
    sleep(1)
    x.sort()
    print(f'Jogo {num+1}: {x}')


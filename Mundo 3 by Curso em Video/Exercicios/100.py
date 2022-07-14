# um programa que tenha uma lista e duas foncoes que sorteia e uma que some par,
# a primeira vai gerar 5 numeros aleatorios e colocalos dentro de uma lista
# a segunda vai somar os valores pares gerador anteriormente
from random import randint


def sortear(lista):
    for x in range(0, 5):
        numeros.append(randint(1, 10))
    # return numeros


def somapar(numeros):
    s = 0
    for x in numeros:
        if (x % 2) == 0:
            s += x




    print(f'A soma dos pares é {s}')

numeros = []
sortear(numeros)

# numeros = sortear()
print(f'Os numeros sorteados Foram: {numeros}')
somapar(numeros)




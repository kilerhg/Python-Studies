# gerar cinco numeros aleatorio e colocar em uma tupla, apos mostrar os numeros sorteados e tambem o menor e o maior


from random import randint
numeros = tuple()
for x in range(0,5):
    rand = randint(1,9)
    numeros += tuple(str(rand))
print(f' Os numeros escolhidos Foram : {numeros}')
print(f' O Maior Numero é : {max(numeros)}')
print(f' O Menor Numero é : {min(numeros)}')

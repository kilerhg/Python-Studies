# leia seis numeros inteiros e mostre a soma apenas dos pares se for impar desconsiderar
sm = 0
for x in range(1,7):
    v = int(input('Digite um Numero Inteiro:'))
    if v % 2 == 0:
        sm += v
print(sm)

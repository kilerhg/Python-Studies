# escreva todos os numeros primos de 1 até 100

for x in range(1,101):
    sm = 0
    for v in range(1,101):
        if x % v == 0:
            sm += 1
    if sm == 2 or x == 1:
        print(x)
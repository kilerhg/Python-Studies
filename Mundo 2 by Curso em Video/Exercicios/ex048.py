# soma de todos os numeros impares que são multiplos de 3 e se encontrar no intervalo de 1 até 500
sm = 0
for x in range(1,501):
    if (x % 2) != 0 and (x % 3) == 0:
        sm += x
print(sm)
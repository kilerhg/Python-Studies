# Leia um numero qualquer e mostre seu fatorial

final = 0
n = int(input('Digite um Numero Inteiro:'))
sm = 0
rn = n
ni = n
while n != 1:
    rn = rn * (n-1)
    n = n-1
    sm += 1
print(f' {ni}! = {rn}')
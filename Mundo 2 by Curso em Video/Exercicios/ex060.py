# Leia um numero qualquer e mostre seu fatorial


'''  Resolução Utilizando While
final = 0
n = int(input('Digite um Numero Inteiro:'))
sm = 0
rn = n
ni = n
while n != 1:
    rn *= (n-1)
    n -= 1
    sm += 1
print(f' {ni}! = {rn}')

'''

# Resolução utilizando for
n = int(input('Digite um Numero Inteiro:'))
sm = 1
for x in range(n,1,-1):
    sm *= x
print(f' {n}! = {sm}')


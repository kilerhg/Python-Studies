# Faça um programa que leia um numero inteiro inteiro e verifique se ele é um numero primo, sendo numero primo divido apenas por 1 e ele mesmo

n1 = int(input('Digite um numero Inteiro:'))
sm = 0
for x in range(1,n1+1):
    if n1 % x == 0:
        sm += 1
if sm == 2:
    print('Numero Primo')
else:
    print('Numero Não Primo')
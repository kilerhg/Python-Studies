# leia o ano de nascimento de sete pessoas mostre quantas são maiores de idade e quantos nao atingiram, maioridade = 21 anos

from datetime import datetime
anoa = int(datetime.today().year)
sm = 0

for x in range(0,7):
    anod = int(input('Digite o ano de nascimento:'))
    idade = anoa - anod
    if idade >= 21:
        sm += 1
print(f'Dos 7, {sm} São Maiores de idade, e {7-sm} Ainda são menor(es)')


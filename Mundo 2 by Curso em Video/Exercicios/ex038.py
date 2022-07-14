# leia dois numeros inteiros e compare os, mostrando na tela qual é maior ou por ordem digitada o primeiro(segundo) valor é maior ou se sao iguais.
n1 = int(input('Digite um Numero inteiro:'))
n2 = int(input('Digite outro Numero Inteiro:'))

if n1 > n2:
    print(f'O primeiro valor {n1} é maior que o segundo {n2}')
elif n2 > n1:
    print(f'O Segundo valor {n2} é maior que o primeiro {n1}')
else:
    print(f'Os Numeros {n1} e {n2} são Iguais')
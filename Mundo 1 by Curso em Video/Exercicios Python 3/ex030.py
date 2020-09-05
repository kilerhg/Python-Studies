# programa que leia um numero inteiro e verifique se é impar ou par
n1 = int(input('Digite um numero inteiro:'))
if n1 % 2 == 0:
    print(f'O numero {n1} é Par')
else:
    print(f'O numero {n1} é Impar')
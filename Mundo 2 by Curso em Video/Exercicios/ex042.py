# leia 3 angulos e mostre se pode mostrar um triangulo e qual tipo do triangulo sendo: Equilátero: todos os lados iguais, Isósceles: dois lados igauis, Escaleno: todos os lados diferentes

n1 = float(input('Digite um Lado do Triangulo:'))
n2 = float(input('Digite um Lado do Triangulo:'))
n3 = float(input('Digite um Lado do Triangulo:'))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Pode se formar Um Triangulo:',end = ' ' )
    if n1 == n2 == n3:
        print('Equilatero')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('Isósceles')
    else:
        print('Escaleno')
print('Não pode se Formar um triangulo')

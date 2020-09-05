# leia 3 numeros e verifique o maior e o menor
n1 = float(input('Digite um numero:'))
n2 = float(input('Digite um numero:'))
n3 = float(input('Digite um numero:'))
p1, p2, p3 = 0, 0, 0

if n1 > (n3 and n2):
    p1 = n1
    if n2 < n3:
        p2 = n2
    else:
        p2 = n3
elif n2 > (n1 and n3):
    p1 = n2
    if n1 < n3:
        p2 = n1
    else:
        p2 = n3
else:
    p1 = n3
    if n1 < n2:
        p2 = n1
    else:
        p2 = n2
print(f'O Maior Valor digitado foi : {p1}\nO Menor valor digitado foi: {p2}')

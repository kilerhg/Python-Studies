# leia duas notas e faça media aritmetica media abaixo de 5 : reprovado, entre 5 e 6.9 recuperação, acima de 7 aprovado

n1 = float(input('Digite sua nota do primeiro Semestre:'))
n2 = float(input('Digite sua nota do segundo Semestre:'))
m = (n1+n2) / 2
if m < 5:
    print('Reprovado')
elif 5 <= m <= 6.9:
    print('Recuperação')
else:
    print('Aprovado')

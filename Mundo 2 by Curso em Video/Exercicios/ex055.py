# leia o peso de 5 pessoa e mostre o maior e menor peso lido
l = []
for x in range(0,5):
    p = float(input('Digite Um Peso:'))
    l.append(p)
l.sort()
print(f'O Menor peso é: {l[0]}\nO Maior peso é: {l[len(l)-1]}')

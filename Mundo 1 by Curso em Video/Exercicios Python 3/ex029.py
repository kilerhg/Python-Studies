# escreva um numero em km por hora, se for acima de 80 km/h tem multa de 7 RS por km
n1 = float(input('Digite uma velocidade em Km/h:'))
if n1 > 80:
    mt = (n1 - 80) * 7
    print(f'Você precisa pagar um multa de {mt:.2f} R$')
else:
    print(f'Você é um bom motorista e não precisa pagar multa ;)')

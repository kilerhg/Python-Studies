# receba distancia em km se for menor que 200km pague 0,5 por km rodado caso seja maior pague 0,45
km = float(input('Digite uma distancia em KM:'))
if km <= 200:
    custo = km*0.5
else:
    custo = km*0.45
print(f'Você precisa pagar {custo} R$')
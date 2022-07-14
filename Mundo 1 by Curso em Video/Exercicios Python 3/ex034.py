# receba um salario e caso for maior que 1250 aumento de 10% caso seja menor ou igual 15%
sl = float(input('Digite seu salario:'))
if sl <= 1250:
    slf = sl*1.15
else:
    slf = sl*1.1
print(f'O seu salario com reajuste ficou: {slf:.2f} R$ !')
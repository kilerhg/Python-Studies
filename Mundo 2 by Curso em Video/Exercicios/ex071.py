# simule o programa que simule o funcionamentp de uma caixa eletronico, no inicio o usuario pergunta qual o valor a ser sacado,
# e o programa vai informar quantas cedulas de cada valor serão entregues, considere que o caixa possui cedulas de 50,20,10,e 1.
cont50 = cont20 = cont10 = cont1 = 0
valor = int(input('Digite o valor a ser Sacado:'))
while True:

    if valor >= 50:
        valor -= 50
        cont50 += 1
    elif valor >= 20:
        valor -= 20
        cont20 += 1
    elif valor >= 10:
        valor -= 10
        cont10 += 1
    elif valor >= 1:
        valor -= 1
        cont1 += 1

    if valor == 0:
        break
print(f' {"= ="*15} Banco ABC {"= ="*15}')
if cont50 != 0:
    print(f'{cont50:2} Nota(s) de R$50 Serão Entregue(s) ')
if cont20 != 0:
    print(f'{cont20:2} Nota(s) de R$20 Serão Entregue(s)')
if cont10 != 0:
    print(f'{cont10:2} Nota(s) de R$10 Serão Entregue(s)')
if cont1 != 0:
    print(f'{cont1:2} Nota(s) de R$ 1 Serão Entregue(s)')


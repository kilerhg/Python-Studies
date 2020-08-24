'''


Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

Entrada

O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.
Saída

O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.

'''

linha = input().split(' ')
codigo,qtd = linha
codigo = int(codigo)
qtd = int(qtd)

if codigo == 1:
    preco = 4
if codigo == 2:
    preco = 4.5
if codigo == 3:
    preco = 5
if codigo == 4:
    preco = 2
if codigo == 5:
    preco = 1.5

conta = qtd * preco

print('Total: R$ %.2f'%conta)

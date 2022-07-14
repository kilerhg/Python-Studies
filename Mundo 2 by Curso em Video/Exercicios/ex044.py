# Leia preço normal e condição de pagamento, sendo elas á vista dinhero/cheque: 10% de decsconto, em até 2x no cartão: preço normal. 3x ou mais no cartão 20% de juros
preco = float(input('Digite o preço padrão do produto:'))
print(f'''
{"="*40}
Digite a condição de pagamento sendo:
Á vista: Dinheiro ou cheque
Cartão: 2x ou mais no cartão
{"="*40}
''')
condicao = str(input('Digite o metodo de pagamento:')).strip()


if ('DINHEIRO') in condicao.upper() or ('CHEQUE') in condicao.upper():
    print(f'A Vista no valor de: {preco*0.9}')

elif condicao.upper() == ('CARTÃO') or condicao.upper() == ('CARTAO') or condicao.upper() == ('1X CARTAO') or condicao.upper() == ('1X CARTÃO'):
    print(f'\nÁ Vista No cartão com valor: {preco*0.95}')
elif ('CARTAO') in condicao.upper() or ('CARTÃO') in condicao.upper():
    print('No cartão com valor:', end=' ')
    if ('2x') in condicao.lower():
        print(preco)
    else:
        print(preco*1.2)
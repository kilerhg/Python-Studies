# leia um ano e verifique se é ano bissexto
ano = int(input('Digite um ano:'))
if (ano % 4) == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano Bissexto')
else:
    print('Ano Não Bissexto')
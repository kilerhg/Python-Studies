# Receba o valor da casa, salario e em quantos anos e verifique se a prestação mensal excede 30%, caso sim o emprestimo sera negado

vcasa = float(input('Digite o valor da casa:'))
salario = float(input('Digite o seu salario:'))
anos = int(input('Digite em quantos anos deseja pagar:'))

prestacao = (vcasa / anos)

if ((salario * 0.3)*12) >= prestacao:
    print('Emprestimo Aceito')
else:
    print('Emprestimo Negado')
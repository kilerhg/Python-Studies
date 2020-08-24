'''


A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:

Salário 	Percentual de Reajuste

0 - 400.00
400.01 - 800.00
800.01 - 1200.00
1200.01 - 2000.00
Acima de 2000.00
	

15%
12%
10%
7%
4%

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.
Entrada

A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.
Saída

Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste e o percentual de reajuste ganho, conforme exemplo abaixo.

'''

salariobase = float(input())

if 0 < salariobase < 400.01 :
    salariofinal = salariobase * 1.15
    aumento = 15
elif 400 < salariobase < 800.01 :
    salariofinal = salariobase * 1.12
    aumento = 12
elif 800 < salariobase < 1200.01 :
    salariofinal = salariobase * 1.10
    aumento = 10
elif 1200 < salariobase < 2000.01 :
    salariofinal = salariobase * 1.07
    aumento = 7
elif 2000 < salariobase :
    salariofinal = salariobase * 1.04
    aumento = 4

print('Novo salario: %.2f' % salariofinal)
print('Reajuste ganho: %.2f' %float(salariofinal - salariobase))
print('Em percentual: {} %'.format(aumento))


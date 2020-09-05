'''

Em um país imaginário denominado Lisarb, todos os habitantes ficam felizes em pagar seus impostos,
pois sabem que nele não existem políticos corruptos e os recursos arrecadados são utilizados em benefício da população,
sem qualquer desvio. A moeda deste país é o Rombus, cujo símbolo é o R$.

Leia um valor com duas casas decimais, equivalente ao salário de uma pessoa de Lisarb. Em seguida,
calcule e mostre o valor que esta pessoa deve pagar de Imposto de Renda, segundo a tabela abaixo.

Lembre que, se o salário for R$ 3002.00, a taxa que incide é de 8% apenas sobre R$ 1000.00, pois a faixa de salário que fica de R$ 0.00 até R$ 2000.00 é isenta de Imposto de Renda.
No exemplo fornecido (abaixo), a taxa é de 8% sobre R$ 1000.00 + 18% sobre R$ 2.00, o que resulta em R$ 80.36 no total. O valor deve ser impresso com duas casas decimais.
Entrada

A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.
Saída

Imprima o texto "R$" seguido de um espaço e do valor total devido de Imposto de Renda, com duas casas após o ponto. Se o valor de entrada for menor ou igual a 2000,
deverá ser impressa a mensagem "Isento".

'''

salariobruto = float(input())

if salariobruto > 2000 :
    if salariobruto > 4500 :
        imposto = 350 + ((salariobruto - 4500 )* 0.28)
    elif 3000 < salariobruto <= 4500 :
        imposto = 80 + ((salariobruto - 3000 )* 0.18)
    elif 2000 < salariobruto <= 3000 :
        imposto = ((salariobruto - 2000 )* 0.08)
    print('R$ %.2f' %imposto)
else :
    print('Isento')
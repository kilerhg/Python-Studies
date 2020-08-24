'''


Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias.
Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364.
Este é apenas um exercício com objetivo de testar raciocínio matemático simples.
Entrada

O arquivo de entrada contém um valor inteiro.
Saída

Imprima a saída conforme exemplo fornecido.

'''

dias = (int(input()))
meses = 0
anos = 0

while (dias>364) :
    anos = anos + 1
    dias = dias - 365

while (dias>29) :
    meses = meses + 1
    dias = dias - 30

print('%s ano(s)\n%s mes(es)\n%s dia(s)' % (anos,meses,dias))
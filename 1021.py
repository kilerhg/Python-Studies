'''


Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir,
 calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2.
  As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.
Entrada

O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).
Saída

Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.

'''

valor = (float(input()))

if 0 <= valor <= 1000000 :
    exit

n100 = 0
n50 = 0
n20 = 0
n10 = 0
n5 = 0
n2 = 0
m100 = 0
m50 = 0
m25 = 0
m10 = 0
m5 = 0
m1 = 0

while(valor>=100):
    valor = float("%.2f" % valor)
    n100 = n100 + 1
    valor = valor - 100

valor = float("%.2f" % valor)


valor = float("%.2f" % valor)
while(valor >=50):
    valor = float("%.2f" % valor)
    n50 = n50 + 1
    valor = valor - 50

valor = float("%.2f" % valor)



while(valor>=20):
    valor = float("%.2f" % valor)
    n20 = n20 + 1
    valor = valor - 20

valor = float("%.2f" % valor)


while(valor>=10):
    valor = float("%.2f" % valor)
    n10 = n10 + 1
    valor = valor - 10

valor = float("%.2f" % valor)


while(valor>=5):
    valor = float("%.2f" % valor)
    n5 = n5 + 1
    valor = valor - 5

valor = float("%.2f" % valor)


while(valor>=2):
    valor = float("%.2f" % valor)
    n2 = n2 + 1
    valor = valor - 2

valor = float("%.2f" % valor)


while(valor>=1):
    valor = float("%.2f" % valor)
    m100 = m100 + 1
    valor = valor - 1

valor = float("%.2f" % valor)


while(valor>=.50):
    valor = float("%.2f" % valor)
    m50 = m50 + 1
    valor = valor - .50

valor = float("%.2f" % valor)


while(valor>=.25):
    valor = float("%.2f" % valor)
    m25 = m25 + 1
    valor = valor - .25

valor = float("%.2f" % valor)


while(valor>=.10):
    valor = float("%.2f" % valor)
    m10 = m10 + 1
    valor = valor - .10

valor = float("%.2f" % valor)


while(valor>=.5):
    valor = float("%.2f" % valor)
    m5 = m5 + 1
    valor = valor - .05

valor = float("%.2f" % valor)


while(valor>.00):
    valor = float("%.2f" % valor)
    m1 = m1 + 1
    valor = valor - .01


valor = float("%.2f" % valor)

print('NOTAS:')
print('%d nota(s) de R$ 100.00' % n100 )
print('%d nota(s) de R$ 50.00' % n50 )
print('%d nota(s) de R$ 20.00' % n20 )
print('%d nota(s) de R$ 10.00' % n10 )
print('%d nota(s) de R$ 5.00' % n5 )
print('%d nota(s) de R$ 2.00' % n2 )

print('MOEDAS:')
print('%d moeda(s) de R$ 1.00' % m100 )
print('%d moeda(s) de R$ 0.50' % m50 )
print('%d moeda(s) de R$ 0.25' % m25 )
print('%d moeda(s) de R$ 0.10' % m10 )
print('%d moeda(s) de R$ 0.05' % m5 )
print('%d moeda(s) de R$ 0.01' % m1 )


'''

print('NOTAS:')
print(n100,' nota(s) de R$ 100.00')
print(n50,' nota(s) de R$ 50.00')
print(n20,' nota(s) de R$ 20.00')
print(n10,' nota(s) de R$ 10.00')
print(n5,' nota(s) de R$ 5.00')
print(n2,' nota(s) de R$ 2.00')

print('MOEDAS:')
print(m100,' moeda(s) de R$ 1.00')
print(m50,' moeda(s) de R$ 0.50')
print(m25,' moeda(s) de R$ 0.25')
print(m10,' moeda(s) de R$ 0.10')
print(m5,' moeda(s) de R$ 0.05')
print(m1,' moeda(s) de R$ 0.01')

'''


'''
print(('NOTAS:\n%s nota(s) de R$ 100.00\n%s nota(s) de R$ 50.00\n%s nota(s) de R$ 20.00\n%s nota(s) de R$ 10.00\n%s nota(s) de R$ 5.00\n%s nota(s) de R$ 2.00\nMOEDAS:\n%s moeda(s) de R$ 1.00\n%s moeda(s) de R$ 0.50\n%s moeda(s) de R$ 0.25\n%s moeda(s) de R$ 0.10\n%s moeda(s) de R$ 0.05\n%s moeda(s) de R$ 0.01') % (n100,n50,n20,n10,n5,n2,m100,m50,m25,m10,m5,m1))
'''
'''
NOTAS:
5 nota(s) de R$ 100.00
1 nota(s) de R$ 50.00
1 nota(s) de R$ 20.00
0 nota(s) de R$ 10.00
1 nota(s) de R$ 5.00
0 nota(s) de R$ 2.00
MOEDAS:
1 moeda(s) de R$ 1.00
1 moeda(s) de R$ 0.50
0 moeda(s) de R$ 0.25
2 moeda(s) de R$ 0.10
0 moeda(s) de R$ 0.05
3 moeda(s) de R$ 0.01
'''

'''
NOTAS:
5 nota(s) de R$ 100.00
1 nota(s) de R$ 50.00
1 nota(s) de R$ 20.00
0 nota(s) de R$ 10.00
1 nota(s) de R$ 5.00
0 nota(s) de R$ 2.00
MOEDAS:
1 moeda(s) de R$ 1.00
1 moeda(s) de R$ 0.50
0 moeda(s) de R$ 0.25
2 moeda(s) de R$ 0.10
0 moeda(s) de R$ 0.05
3 moeda(s) de R$ 0.01
'''
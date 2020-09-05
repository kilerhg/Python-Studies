'''

Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto.
As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.
Entrada

O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).
Saída

Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias,
conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha,
caso contrário seu programa apresentará a mensagem: “Presentation Error”.



'''


valor = int(input())
valorbase = valor
notas100 = 0
notas50 = 0
notas20 = 0
notas10 = 0
notas5 = 0
notas2 = 0
notas1 = 0

while ((valor > 99)) :
    valor = valor - 100
    notas100 = notas100 + 1
    

while ((valor > 49)) :
    valor = valor - 50
    notas50 = notas50 + 1
    

while ((valor > 19)) :
    valor = valor - 20
    notas20 = notas20 + 1

while ((valor > 9)) :
    valor = valor - 10
    notas10 = notas10 + 1

while ((valor > 4)) :
    valor = valor - 5
    notas5 = notas5 + 1

while ((valor > 1)) :
    valor = valor - 2
    notas2 = notas2 + 1

while ((valor > 0)) :
    valor = valor - 1
    notas1 = notas1 + 1


print(valorbase)
print('%.0f nota(s) de R$ 100,00'%notas100)
print('%.0f nota(s) de R$ 50,00'%notas50)
print('%.0f nota(s) de R$ 20,00'%notas20)
print('%.0f nota(s) de R$ 10,00'%notas10)
print('%.0f nota(s) de R$ 5,00'%notas5)
print('%.0f nota(s) de R$ 2,00'%notas2)
print('%.0f nota(s) de R$ 1,00'%notas1)
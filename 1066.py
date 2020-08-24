'''

Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares,
 quantos valores digitados foram positivos e quantos valores digitados foram negativos.
Entrada

O arquivo de entrada contém 5 valores inteiros quaisquer.
Saída

Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final de linha após cada uma.

'''

pares = 0
impares = 0
positivos = 0
negativos = 0
n1 = input()
n2 = input()
n3 = input()
n4 = input()
n5 = input()

lista = [n1,n2,n3,n4,n5]
lista1 = list(map(int,lista))
for x in lista1:
    if x % 2 == 0:
        pares += 1
    elif x % 2 != 0:
        impares += 1
    if x > 0 :
        positivos += 1
    elif x < 0:
        negativos += 1
print('%.0f valores par(es)' %pares)
print('%.0f valores impar(es)' %impares)
print('%.0f valores positivo(s)' %positivos)
print('%.0f valores negativo(s)' %negativos)
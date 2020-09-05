'''

Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos).
A seguir, mostre a quantidade de valores positivos digitados.
Entrada

Seis valores, negativos e/ou positivos.
Saída

Imprima uma mensagem dizendo quantos valores positivos foram lidos.

'''

postivos = 0
n1 = input()
n2 = input()
n3 = input()
n4 = input()
n5 = input()
n6 = input()

lista = [n1,n2,n3,n4,n5,n6]
lista1 = list(map(float,lista))
for x in lista1:
    if x > 0 :
        postivos += 1
print('%.0f valores positivos' %postivos)
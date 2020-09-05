'''

Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.
Entrada

O arquivo de entrada contém 5 valores inteiros quaisquer.
Saída

Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.

'''

pares = 0
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
print('%.0f valores pares' %pares)
# leia 5 valores numeros e guarde em uma lista, no final mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista = []
posmax = []
posmin = []
for x in range(0,5):
    lista.append(int(input(f'Digite um valor na pos{x}:')))
print(f'A Lista digitada foi: {lista}')

if lista.count(max(lista)) > 1:
    for pos, x in enumerate(lista):
        if x == max(lista):
            posmax.append(pos)
    print(f'O Maior valor Digitado foi: {max(lista)}, Na posição : ', end = ' ')
    for x in posmax:
        print(f'...{x}', end='')
    print('\n')
else:
    print(f'O Maior valor Digitado foi: {max(lista)}, Na posição {lista.index(max(lista))}')

if lista.count(min(lista)) > 1:
    for pos, x in enumerate(lista):
        if x == min(lista):
            posmin.append(pos)
    print(f'O Menor valor Digitado foi: {min(lista)}, Na posição : ', end = ' ')
    for x in posmin:
        print(f'...{x}',end='')
    print('\n')
else:
    print(f'O Menor valor Digitado foi: {min(lista)}, Na posição {lista.index(min(lista))}')



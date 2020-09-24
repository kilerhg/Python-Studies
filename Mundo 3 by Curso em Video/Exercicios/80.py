# digitar 5 valores numericos e cadastre os em uma lista, ja na posição correta, SEM USAR SORT, no final mostre a lista ordenada na tela.
lista = []
for x in range(0,5):
    valor = int(input('Digite um valor:'))
    if valor in lista:
        lista.insert(lista.index(valor), valor)
    n1 = len(lista)
    if n1 > 0:
        for c in range(0,n1):
            if valor > max(lista):
                lista.insert(n1,valor)
                print('Adicionado na ultima posição da lista')
            elif valor < min(lista):
                lista.insert(0,valor)
                print('Adicionado na posição 0')
            else:
                for v in range(0,3):
                    if lista[v] < valor < lista[v+1]:
                        lista.insert(v+1,valor)
    else:
        lista.append(valor)
        print('Adicionado na ultima posição da lista')
print('A lista ordenada Ficou: ', end='')
for x in lista:
    print(f'...{x}',end='')
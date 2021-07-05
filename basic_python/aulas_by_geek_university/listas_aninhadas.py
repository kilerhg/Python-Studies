'''
List comprehension,Listas aninhadas (Nested Lists)

em outras linguagem conhece-se as 'listas' do python pelos seguintes nomenclatura:
    Unidimensional - Arrays/vetores
    Multidimensional - Matrizes 

Exemplo com for e com comprehension

tradicional 

lista_aninhada = [[1,2,3],[4,5,6],[7,8,9]]

# for lista in lista_aninhada:
#     for valor in lista:
#         print(valor)

comprehension

[[print(valor) for valor in lista] for lista in lista_aninhada]

gerando tabuleiro 3x3
tabuleiro = [[linha for linha in range(1,4)]for coluna in range(3)]
print(tabuleiro)

[[print(valor) for valor in lista] for lista in tabuleiro ]

gerando jogadas velha

Com comprehensions

velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1,4)] for colunas in range(3)]
print(velha)

Com for

lista_explica = []
for colunas in range(3):
    lista_dentro = []
    for numero in range(1,4):
        if numero % 2 == 0:
            lista_dentro.append('X')
        else:
            lista_dentro.append('O')
    lista_explica.append(lista_dentro[:])
print(lista_explica)
'''

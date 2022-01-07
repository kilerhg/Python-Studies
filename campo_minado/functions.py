# B - Bomba
# V - Vazio


def gera_matriz(colunas : int, linhas : int):
    lista_matriz = []
    for coluna in range(0, colunas):
        lista_matriz.append(list('V'* linhas))
    return lista_matriz


def gera_pos_bomba(max_colunas, max_linhas):
    from random import randint
    x, y = randint(0, max_linhas-1), randint(0, max_colunas-1)
    return x, y


colunas, linhas = 3, 3
lista_matriz = gera_matriz(colunas=colunas, linhas=linhas)

x, y = gera_pos_bomba(max_colunas=colunas, max_linhas=linhas)
lista_matriz[x][y] = 'B'
print(lista_matriz)
print(x+1, y+1)

# Varrendo


# m : minus 1
# p : plus 1
# n : not change

for c in range(0, colunas):
    for l in range(0, linhas):
        atual = lista_matriz[c][l]
        atual_x_n_y_n = ''
        atual_x_n_y_n = ''
        
# produtos = ['000001','Pipoca','01','2,59','000002','Manteiga','01','4,20']
# produtos = list(produtos)
# pesquisar = '1'
# if len(pesquisar) < 6:
#     pesquisar = ('0' * (6 - len(pesquisar))) + pesquisar
# codigo_indice = produtos.index(f'{pesquisar}')
# codigo = produtos[codigo_indice]
# produto = produtos[codigo_indice+1]
# quantidade = produtos[codigo_indice+2]
# preco = produtos[codigo_indice+3]
# print(f'Codigo {codigo}')
# print(f'Produto {produto}')
# print(f'Quantidade {quantidade}')
# print(f'Preco {preco}')
#
# print('CODIGO ------- NOME PRODUTO  ---- QTD --- PREÇO')
# print(f'{codigo:0<6} {"-"*7} {produto:^13} {"-"*4} {quantidade:^3} {"-"*3} {preco:^7}')
# 6 7 13 4 3 7
# XXXXXX ------- XXXXXXXXXXXXX ---- XXX ---- XXXXXXX
#
#
# print(produtos)
#
# deletar
#
# del produtos[codigo_indice+3]
# del produtos[codigo_indice+2]
# del produtos[codigo_indice+1]
# del produtos[codigo_indice]
# print(produtos)
#
# criar nota
#
# for x in range(1,(len(produtos)//4)+1):
#     if len(str(x)) < 6:
#         pesquisar = ('0' * (6 - len(str(x)))) + str(x)
#     codigo_indice = produtos.index(f'{pesquisar}')
#     codigo = produtos[codigo_indice]
#     produto = produtos[codigo_indice + 1]
#     quantidade = produtos[codigo_indice + 2]
#     preco = produtos[codigo_indice + 3]
#     # print(f'Codigo {codigo}')
#     # print(f'Produto {produto}')
#     # print(f'Quantidade {quantidade}')
#     # print(f'Preco {preco}')
#     #
#     # print('CODIGO ------- NOME PRODUTO  ---- QTD --- PREÇO')
#     print(f'{codigo:0<6} {"-"*7} {produto:^13} {"-"*4} {quantidade:^3} {"-"*3} {preco:^7}')
#     # 6 7 13 4 3 7
#     # XXXXXX ------- XXXXXXXXXXXXX ---- XXX ---- XXXXXXX
# from builtins import range
# from datetime import datetime
#
# def data_agora():
#     data = str(datetime.today())
#     data = data[:-7]
#     return data
#
# print(data_agora())
# datetime.date()

# def teste():
#     a = 5
#     b = 5
#     c = a+b
#     print('TESTE')
#
# def somar(num1,num2):
#     num1 = int(num1)
#     num2 = int(num2)
#     soma = num1 + num2
#     return soma
#
# print(somar(10,6))
# print(somar(10,1))
# print(somar(10,5))
# print(somar(10,3))
# d = 10
# a = 2
# b = 3
#
# # c = funcao(a,b)
# # print(c)
# print(funcao(a,b))
# teste()
# print(d)


def funcao(a, b):
    print('a')
    d = 10000
    lista=[]
    for i in range(1, a + 1):
      print(i)
      lista.append(b * i)
    return lista
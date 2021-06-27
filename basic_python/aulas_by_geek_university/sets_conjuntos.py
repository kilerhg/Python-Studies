"""
Testando Tamanho Conjunto

import sys

letters = ['a','b','c','d','e','f']

# for letter in letters:
dados = range(100000)

tupla = tuple(dados)
lista = list(dados)
conjunto = set(dados)

print(f'''
-=-=-= conjunto

Tipo    : {type(conjunto)}
Len     : {len(conjunto)}
Tamanho : {sys.getsizeof(conjunto)}

-=-=-= lista

Tipo    : {type(lista)}
Len     : {len(lista)}
Tamanho : {sys.getsizeof(lista)}

-=-=-= tupla

Tipo    : {type(tupla)}
Len     : {len(tupla)}
Tamanho : {sys.getsizeof(tupla)}

''')

Utilidades interessantes

Ter apenas dados unicos, aplicando um set em uma lista ou tupla. exemplo:
lista = [1,2,3,1]
conjunto = list(set(lista))

conjunto = {'a','B',True,True,False,12,4.2}

Inserir dados em um conjunto com .add
a.add(4)

# Removendo dados de um conjunto com .remove ou .discard

a.remove(11)

# Utilizando o remove, ele remove o valor normalmente, porém se o valor não existir retorna KeyError
a.discard(2)

# Utilizando o Discard, remove igual o remove, porem se o valor não existir ele continua normalmente


# Copiando Sets

# Metodo 1 - Deep Copy (cria uma outra variavel independente)

a = s.copy()
a.add(4)

# Metodo 2 - Shallow Copy (cria um vinculo entre duas variaveis)

a = s
a.add(4)

# Metódos Mátematicos de conjuntos

# União de conjuntos 

# Método 1 com .union()


c = a.union(b)

# Método 2 com pipi |

c = a | b

# Metódos Mátematicos de conjuntos

# Interseção de conjuntos

# Método 1 .intersection()

c = a.intersection(b)

# Método 2 & (E comercial)

c = a & b

# Metódos Mátematicos de conjuntos

# Interseção de conjuntos

# Método 1 .intersection()

c = a.intersection(b)

# Método 2 & (E comercial)

c = a & b 

# Metódos Mátematicos de conjuntos

# Diferença de conjuntos

# Gera apenas o que não está no duplicado entre os dois .difference()

c = a.difference(b)
d = b.difference(a)

"""





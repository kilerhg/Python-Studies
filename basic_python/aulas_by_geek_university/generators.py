'''
-> Generators

O que são:
    Iterável Performatico que armazena em disco até ser utilizado

Utilizando:
    Utilização semelhante aos Comprehensions de set,list. porém com a diferença de definição com '(' colchetes 

from sys import getsizeof

# Pratica

# Gerando um iteravel com range entre 0 e 10**5 multiplicado por 2

# Com list
list_comp = [valor*2 for valor in range(10**3)]

# Com set
set_comp = {valor*2 for valor in range(10**3)}

# Com dict

dict_comp = {valor:valor*2 for valor in range(10**3)}

# Com gerenator

gen = (valor*2 for valor in range(10**3))

# Verficando se são idênticos

# print(list(list_comp) == list(set_comp) == list(gen)) # Convertendo todos para lista e validando se são iguais

## Verificando espaço em memoria para a mesma tarefa

print(f"""
Lista       : {getsizeof(list_comp)}
Conjunto    : {getsizeof(set_comp)}
Generator   : {getsizeof(gen)}
Dicionario  : {getsizeof(dict_comp)}
""")
'''


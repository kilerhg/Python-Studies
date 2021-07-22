'''
zip() - Cria um iterável zip object, que concatena em tupla os iteraveis passados como parametro e a retorna

zip(iteravel, iteravel, ...)


# Semelhantemente aos objetos filter e map, o objeto gerado morre após a primeira Conversão


# Exemplo Básico


from random import randint

lista1 = [randint(1,10) for valor in range(10)]
lista2 = [randint(1,10) for valor in range(10)]
lista3 = [randint(1,10) for valor in range(10)]


print(f"""
Lista 1: {lista1}
Lista 2: {lista2}
Lista 3: {lista3}
""")

b = zip(lista1, lista2, lista3) # Junta o item de outro iterável pelo mesmo indice

for item in b: # É iterável
    print(item)

print(b) # tipo zip object

b = zip(lista1, lista2, lista3) # Junta o item de outro iterável pelo mesmo indice

print(tuple(b))

b = zip(lista1, lista2, lista3) # Junta o item de outro iterável pelo mesmo indice

print(list(b))

b = zip(lista1, lista2, lista3) # Junta o item de outro iterável pelo mesmo indice
b = [list(item) for item in b] # Tranforma a tupla em lista dentro de cada indice
print(b)

b = zip(lista1, lista2, lista3) # Junta o item de outro iterável pelo mesmo indice

print(set(b))

# TAMANHO do zip object

b = zip(lista1, lista2, lista3) # Junta o item de outro iterável pelo mesmo indice

# print(len(lista1)) # 10 
# print(len(lista2)) # 9
# print(len(lista3)) # 8


print(len(list(b))) # 8
# Vale ressaltar que a quantidade de itens é limitada pelo menor iterável,
# neste caso lista3 com 8 elementos, Indiferentemente da ordem.

# ITERANDO Diferentes tipos de Iteráveis

lista = [randint(1,10) for valor in range(9)]
conjunto = {randint(1,10) for valor in range(50)} # Pode se ter variação de quantidade de itens pois o set tira repetição
gerador = (randint(1,10) for valor in range(12))
tupla = tuple(lista)
dicionario = {valor:randint(1,10) for valor in range(20)}


print(f"""
-=-= Elementos
lista: {lista}
conjunto: {conjunto}
gerador: {gerador} # Mostra que é objeto pois ainda não foi convertido ou iterádo
tupla: {tupla}
dicionario: {dicionario}
-=-= Elementos
""")

zipado = list(zip(lista, conjunto, gerador, tupla, dicionario.values()))

print(zipado)
print(len(zipado))

# Desempacotando

from random import randint

valor = [(randint(0,10), randint(0, 10)) for value in range(10)]

print(list(zip(*valor)))

'''


# Exercicio, recebendo notas de 3 alunos em 2 provas
#  e fazer um dicionario com todas as notas e com a maior nota

alunos = ['carlos', 'maria', 'eduarda']
prova1 = [57, 89, 60]
prova2 = [82, 96, 99]


notas = list(zip(alunos, prova1, prova2))

dicionario_todos = {nota[0]:list(nota[1:]) for nota in notas}


dicionario_maior = {nota[0]:max(list(nota[1:])) for nota in notas}

# Utilizando map
dicionario_maior_map = dict(zip(alunos, map(lambda nota: max(nota), zip(prova1,prova2)))) 
# Zip com 2 parametros(iteráveis) pode ser convertido para dicionario sem problema,
# Sendo elemento 0 como chave e 1 como valor


print(dicionario_todos)

print(dicionario_maior)

print(dicionario_maior_map)
























'''
Map

Mapeando valores para função

Sintaxe:

map(funcao,iteravel) # ele retorna um map.object() # desejavel converter para lista e depois printar

def ao_quadrado(numero):
    return numero ** 2

lista = list(range(1,11)) # [1,..,10]
# Exemplo 01 for
lista_final = []
for valor in lista:
    lista_final.append(ao_quadrado(valor))

print(lista_final)

# Exemplo 02 comprehensions

lista_final = []
lista_final = [valor ** 2 for valor in lista]
print(lista_final)

# Exemplo 03 map

lista_final = []
lista_final = map(ao_quadrado, lista)
print(list(lista_final))

# forma 4 map + lambda

lista_final = []
lista_final = list(map(lambda x: x ** 2, lista))
print(lista_final)

# OBS: ele zera o cache do map após a primeira vez que converter o objeto: exemplo
lista_final_mapa_original = map(lambda x: x ** 2, lista)
lista_final_mapa = list(lista_final_mapa_original) # Retorna o valor, pois é a primeira vez que converte
print(lista_final_mapa) 
lista_final_mapa = list(lista_final_mapa_original) # Retorna o vazio, pois é a segunda vez que converte
print(lista_final_mapa)

# Convertendo apenas um valor de uma tupla

cidades = (['osasco',20],['são paulo',5],['rio de janeiro',50])
func = lambda dado: (dado[0],(9/5) * dado[1] + 32)
print(list(map(func,cidades)))

# Obs map aceita somente funções com 1 parametro
'''




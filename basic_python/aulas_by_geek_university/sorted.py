'''
-> Sorted

OBS: Cuidado para não confundir com o [].sort(), o mesmo é um função de listas, o sorted é uma função separada.

Como funciona:
    sorted(iterável) - retorna uma LISTA com valores ordenados

from random import randint
# Na pratica

dados_list = [randint(1,10) for valor in range(10)]
dados_gen = (randint(1,10) for valor in range(10))
dados_set =  {randint(1,10) for valor in range(10)}


print(f"""
Listas:
    Dados: {dados_list}
    Ordem: {sorted(dados_list)}

Generator:
    Dados: {dados_gen}
    Ordem: {sorted(dados_gen)}

Set:
    Dados: {dados_set}
    Ordem: {sorted(dados_set)}
"""
)

# Parametros Do sorted


## reverse | Inverte a ordenação para decrescente

print(f"""
Listas:
    Dados: {dados_list}
    Ordem: {sorted(dados_list)}
    Rever: {sorted(dados_list, reverse=True)}


Generator:
    Dados: {dados_gen}
    Ordem: {sorted(dados_gen)}
    Rever: {sorted(dados_gen, reverse=True)} # Não apresenta valor pois o generator se auto-remove da memoria a partir da primeira conversão


Set:
    Dados: {dados_set}
    Ordem: {sorted(dados_set)}
    Rever: {sorted(dados_set, reverse=True)}

"""
)

# key | Utilizado para ordenar dicionarios, passando uma função

users = [
    {'username':'lucas','password':'123'},
    {'username':'carlos','password':'ASADASD56A4SD65AS45D6SA'},
    {'username':'roberta','password':'ASADASD56A4SD65AS45D6SA'},
    {'username':'gilberto','password':'321'},
    {'username':'rodolfo','password':'familia'},
    {'username':'rogerio','password':'teste'},
]

print(users)

# Ordena o dicionario users pelo chave username
print(sorted(users, key=lambda x:x['username'])) 

musicas = [
    {'title':'music1','times':1},
    {'title':'music2','times':2},
    {'title':'music3','times':3},
    {'title':'music4','times':4},
]

# Sem ordenação
print(musicas)

# Ordenada Por titulo ascendente
print(sorted(musicas, key=lambda musica:musica['title']))

# Ordenada por vezes ascendente
print(sorted(musicas, key=lambda musica:musica['times']))

# Ordenada por vezes descendente
print(sorted(musicas, key=lambda musica:musica['times'], reverse=True))

'''











'''
Filter

filter() -> Serve para filtrar uma determinada coleção


Sintaxe:
filter(funcao,iteravel) - Retorna objeto filter

import statistics

dados = [0.8,4.2,1.1,2.3,4.8,9.5]

media = statistics.mean(dados)

print(media)

resultado = filter(lambda x: x > media, dados)
print(list(resultado))

# De modo semelhante o map(), após o objeto ser convertido a primeira vez ele é deletado da memoria

# Funcionalidade -> ele retorna booleano, se ele for true entra no filter.

# Exemplo 01 - removendo dados vazio de uma lista
print(paises)

resultado = filter(None,paises)

paises = ['Brasil','chile','','','Uruguai']
print(paises)
resultado = filter(lambda x: len(str(x).strip()) > 0,paises)
print(list(resultado))

# Diferença map e filter

map -> aplica uma função com parametro do iterado, retornando o resultado da função

filter -> aplica uma função com parametro do iterado, retornando booleano, se for True inclue no valor filtrado


# Exemplos mais complexos

# Separando valor dentro de lista de dicionarios

users = [
    {'username':'kil','password':'123'},
    {'username':'kil','password':'ASADASD56A4SD65AS45D6SA'},
    {'username':'kil','password':'ASADASD56A4SD65AS45D6SA'},
    {'username':'kil','password':'321'},
    {'username':'kil','password':'familia'},
    {'username':'kil','password':'teste'},
]

senhas_fracas = filter(lambda x: len(x['password']) < 5, users)

print(list(senhas_fracas))

'''

# Desafio 01, combinando filter e map(), criar uma lista contendo 'sua intrutora é :' + nome desde que tenha menos de 5 caracteres
lista = ['Vanessa', 'Ana', 'Maria']

menor_cinco = filter(lambda x: len(x) < 5, lista)
lista_menor = list(menor_cinco)

lista_introducao = list(map(lambda x: f'Sua intrutora é {x}', lista_menor))

print(lista_introducao)
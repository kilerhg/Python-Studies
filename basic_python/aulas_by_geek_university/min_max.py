'''
> Min e Max

max() -> Retorna o MAIOR valor de um iterável, ou maior de dois ou mais elementos
min() -> Retorna o MENOR valor de um iterável, ou menor de dois ou mais elementos

from random import randint

dados_lista = [item*randint(1, 50) for item in range(1, 20)]
dados_conjunto = {item*randint(1, 50) for item in range(1, 20)}
dados_dicionario = {item:item*randint(1, 50) for item in range(1, 20)}
dados_generator = (item*randint(1, 50) for item in range(1, 20))

print(f"""
{'lista':-^20}
Valor: {dados_lista}
Maior: {max(dados_lista)}
Menor: {min(dados_lista)}

{'Conjunto':-^20}
Valor: {dados_conjunto}
Maior: {max(dados_conjunto)}
Menor: {min(dados_conjunto)}

{'Dicionario':-^20}
Valor: {dados_dicionario}
Maior: {max(dados_dicionario.values())}
Menor: {min(dados_dicionario.values())}

{'Generator':-^20}
Valor: {dados_generator}
Maior: {max(dados_generator)}
Menor: 'min(dados_generator)' # Não Retorna nada pois o gerador já foi convertido

""")

## Utilizando Com Strings

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

print(max(nomes)) # Em Ordem alfabética o ultimo elemento
print(min(nomes)) # Em Ordem alfabética o primeiro elemento

## Utilizando key com min e max

### OBS: após passar o iterável passe o opcional key explicitamente se não a sintaxe reconhece como outro argumento de *args

print(max(nomes, key=lambda x: len(x))) # Retorna o com iterável com mais caracteres 
print(min(nomes, key=lambda x: len(x))) # Retorna o com iterável com menos caracteres 


print(max(musicas, key=lambda musica: musica['times'])) # Mais Tocada Retorna Dicionario Inteiro
print(min(musicas, key=lambda musica: musica['times'])) # Menor Tocada Retorna Dicionario Inteiro

print(max(musicas, key=lambda musica: musica['times'])['title']) # Mais Tocada Retorna Titulo
print(min(musicas, key=lambda musica: musica['times'])['title']) # Menor Tocada Retorna Titulo

musicas = [
    {'title':'music1','times':1},
    {'title':'music2','times':2},
    {'title':'music3','times':3},
    {'title':'music4','times':4},
    {'title':'music5','times':0},
]

mais_tocada = menos_tocada = {'times':-1}
for musica in musicas:
    vezes = int(musica['times'])
    if vezes > mais_tocada['times']:
        mais_tocada = musica
    if vezes < menos_tocada['times'] or menos_tocada['times'] == -1:
        menos_tocada = musica

print(mais_tocada)
print(menos_tocada)
'''








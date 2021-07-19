'''
-> Reversed

OBS: não confundir com reverse pois é uma função das listas:
    lista.reverse() # Retorna a lista invertida

O Reversed funciona para quaisquer iterável, invertendo o mesmo.

-> Retorna um iterável propio, de nome: List Reversed Iterator

# Exemplos:

## Iteraveis

dados = list(range(10))
print(dados) # Iterável
print(reversed(dados)) # Objeto Propio que também é iterável
print(type(reversed(dados))) # list_reverseiterator
print(list(reversed(dados))) # Convertido em lista

## Strings

### Invertendo Nome

nome = 'LUCAS NUNES DE ASSIS'

print(nome)
print(nome[::-1]) # Método mais fácil

[print(letra, end='') for letra in reversed(nome)] # Utilizando For e Reversed
print()

print(''.join(list(reversed(nome)))) # Utilizando join e Reversed


## Range

### Invertendo range

dados_reversed = reversed(range(10)) # Utilizando Reversed
dados_range = list(range(9, -1, -1)) # Utilizando Parametros do range

print(list(dados_reversed))
print(dados_range)


'''






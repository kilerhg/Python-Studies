"""
Modulo Collections (Modulo conhecido por alta performance) - Default Dict


> Ao utilizar o Default dict se passa um valor padrão, que quando não for atribuído valor, ele puxara automaticamente o padrão, e quando ele for
referenciado antes de criado ele cria e passa o valor como default
"""

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['teste'] = 'algum'
print(dicionario)
print(dicionario['ola'])
print(dicionario)
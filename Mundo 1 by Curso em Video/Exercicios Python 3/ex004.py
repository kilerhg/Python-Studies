algo = input('Escreva algo:')
print(type(algo))
print('Algo é Numero? ', algo.isnumeric())
print('Algo é Texto? ', algo.isalpha())
print('Algo é Texto e Numerico? ', algo.isalnum())
print('Algo é Todo em maiusculo? ', algo.isupper())
print('Algo é Todo em minusculo? ', algo.islower())
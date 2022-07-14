'''
-> Reduce

Importando 'import functools'


Entendendo

imagine uma coleção de dados(iterável):

dados [a1, a2, a3, ...an]

se tem uma função com dois parametros:

def função(x, y):
    return x *  y

semelhantemente ao map, filter, recebe dois parametros : Uma função e um iterável,
Porem diferente de map e filter, a função passada como parametro recebe dentro dela dois parametros

reduce(função, dados)

funcionamento:
    1. res1 = f(a1, a2) # Aplica a função nos dois primeiros iterados e armazena
    2. res2 = f(res1, a3) # Aplica a função no resultado anterior e o próximo iterado
    3. res3 = f(res2, a4) # Continua o ciclo
    .. res. = f(res., a.)

Resultado final:
    O que será retornado pela reduce é o resultado do ultimo passo do funcionamento.

Também podendo ser visualizado da seguinte forma:
    função(função(função(função(função(a1, a2), a3), a4), ...), an)

from functools import reduce

# Obs: reduce em geral pode ser substituido por for, usar somente quando for estritamente necessário 

# Praticando:

# Desafio Multiplicar um iterável por outro passando na lista

## Utilizando Reduce:

dados = [1, 2, 3, 4, 5, 6, 7, 8, 9]

resultado_reduce = reduce(lambda x,y:x*y,dados)

# Utilizando For:
resultado_for = 1
for item in dados:
    resultado_for *= item

print(resultado_reduce)
print(resultado_for)
'''


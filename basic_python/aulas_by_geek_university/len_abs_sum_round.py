'''
Len, Abs, Sum, Round

# Len


len() -> Recebe um iterável e Retorna a quantidade de itens do iterável

## Recaptulando

print(len(range(0,10))) # 10

## Por baixo dos Panos, 

# ele roda Dunder Len
print(range(0, 10).__len__()) # 10

# Abs

abs() -> Recebe um valor inteiro ou Real e retorna seu valor positivo

print(abs(-5)) # 5
print(abs(5)) # 5 
print(abs(-3.14)) # 5
print(abs(3.14)) # 5

# Sum

sum() -> Recebe um iterável com valores numericos(inteiros ou reais), e pode opcionalmente receber valor inicial(start=), retornando a soma dos iteraveis numericamente

dados = range(50)
print(sum(dados))
print(sum(dados, start=-1)) # Soma o iterável começando com -1

# Round

round() -> Recebe um numero real e arredonda para a quantidade de casas definidas, o padrão é 0, ou seja retornando um iteiro

# OBS: ao numero terminar com .5 ele arrendonda para o numero base 10(par) mais proximo

exemplo:

print(round(10.5)) # 10
print(round(9.5)) # 10
'''


print(round(10.123,2)) # 10.12
print(round(10.129,2)) # 10.13














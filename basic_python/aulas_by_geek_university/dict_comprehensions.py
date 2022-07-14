'''
Dict Comprehensions

Sintaxe:

{chave:valor for item in iterável}

Exemplos:

Exemplo 01 Verificando se valor é numero se sim converte

dicionario = {'a':1, 'b':'2', 'c':3, 'd':4, 'e':'1.0'}
dicionario_gerado =  {chave: int(valor) if str(valor).isnumeric() else str(valor) for chave,valor in dicionario.items()}

Exemplo 02 gerando dict de uma lista

lista = range(5)

dicionario_gerado = {valor: valor ** 2 for valor in lista}

OBS: Dicionario não aceita repetição de chaves

Exemplo 03 Misturando 2 iteraveis

Utilizando Comprehensions

iteravel_string = 'abcde'
iteravel_lista = [1,2,3,4,5]

dicionario_resultante = {iteravel_string[indice]: iteravel_lista[indice] for indice in range(len(iteravel_string))}

Utilizando For

dicionario_resultante = {}
for indice in range(len(iteravel_string)):
    dicionario_resultante[iteravel_string[indice]]=iteravel_lista[indice]

'''



iteravel_lista = [1,2,3,4,5]

dicionario_par_impar = {numero: ('par' if numero % 2 == 0 else 'impar') for numero in iteravel_lista}

print(dicionario_par_impar)

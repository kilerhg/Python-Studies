'''
O que são Lambda: Funções sem nome, Anonimas

sintaxe: 

# Função normal

def quadrado(x):
    return x**2

print(quadrado(2))

# Declarando Lambda



# Utilizando

calc = lambda x:x**2

print(calc(2))


# Lambdas aceitam multiplas entradas

nome_completo = lambda nome, sobrenome: str(nome).strip().title() + ' ' + str(sobrenome).strip().title()


print(nome_completo('lucas  ','  nunes'))

# Ao passar mais parametros do que a lambda espera retorna TypeError


nomes = ['lucas nunes', 'nunes lucas', 'carlos roberto', 'agnaldo faria',' faria agnaldo']

nomes.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].strip().lower())

print(nomes)

# Utilizando Lambda dentro de uma função

def soma_quadrado(a,b):
    return lambda x: (a+b) ** x


soma = soma_quadrado(1,2)

print(soma_quadrado(1,2)(3)) # o segundo parenteses (3) entra no lambda x

'''


# leia Sexo (M,F) caso esteja errado para digitar certo ate ter um valor correto
sexo = 'a'
while sexo not in 'MmFf':
    sexo = str(input('Digite O sexo [M/F]:')).strip()[0]

# programa que leia nome,sexo e idade de varias pessoas, guardando em um dicionario e todos os dicionarios em uma lista, no final mostre:
# A - Quantas pessoas foram cadastradas
# B - A media de idade do grupo
# C - Uma lista com todas as mulheres
# D - Uma lista com todas as pessoas com idade acima da media
flag = 'a'
pessoa = {}
pessoas = []
idades = []
mulheres = []
maiores = []
while True:
    pessoa['nome'] = str(input('Digite o Nome:')).strip().capitalize()
    while True:
        pessoa['sexo'] = str(input('Digite o Sexo [M/F]:')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Por favor Digite O sexo corretamente M/F')
    '''
        
        Alternativa
        
    pessoa['sexo'] = str(input('Digite o Sexo:')).strip().upper()[0]
    if pessoa['sexo'] not in 'MF':
        while True:
            print('Por favor Digite O sexo corretamente')
            pessoa['sexo'] = str(input('Digite o Sexo:')).strip().upper()[0]
            if pessoa['sexo'] in 'MF':
                break
    '''
    pessoa['idade'] = int(input('Digite a Idade:'))
    print('*-'*30)
    pessoas.append(pessoa.copy())
    idades.append(pessoa['idade'])
    while True:
        flag = str(input('Deseja Cadastrar mais pessoas [S/N]:')).strip().upper()[0]
        if flag in 'SN':
            break
        print('Digite S Ou N')
    '''
    
        Alternativa 
        
    if flag not in 'SN':
        while True:
            print('Por favor digite S ou N')
            flag = str(input('Deseja Cadastrar mais pessoas [S/N]:')).strip().upper()[0]
            if flag in 'SN':
                break
    '''
    if flag in 'N':
        break

print()
for x in pessoas:
    if x['sexo'] == 'F':
        mulheres.append(x)
    if x['idade'] > sum(idades)/len(pessoas):
        maiores.append(x)
print(f'Foram cadastradas {len(pessoas)} Pessoas')
print(f'A media de idade do grupo é: {sum(idades)/len(pessoas):.2f}')
print(f'Lista das Mulheres cadastradas:', end=' ')
for x in mulheres:
    print(x["nome"],end=', ')
print()
print(f'Lista com os Maiores da Media: ')
for x in maiores:
    for k,v in x.items():
        print()
        print(f'{k.capitalize()} = {v}.', end=' ')
    print()
print()


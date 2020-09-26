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
    pessoa['sexo'] = str(input('Digite o Sexo:')).strip().upper()[0]
    pessoa['idade'] = int(input('Digite a Idade:'))
    print('*-'*30)
    pessoas.append(pessoa.copy())
    idades.append(pessoa['idade'])
    flag = str(input('Deseja Cadastrar mais pessoas [S/N]:')).strip().upper()[0]
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


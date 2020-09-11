# desenvolva que leia nome idade e sexo de 4 pessoas no final mostre a media de idade destas pessoas, o nome do homem mais velho, quantas mulheres tem menos de 20 anos

si = 0
sf = 0
dc = {}
ls = []
for x in range(0,4):
    print('-'*10)
    nome = str(input('Digite o Nome:')).strip().capitalize()
    idade = int(input('Digite a idade:'))
    s = str(input('Digite o Sexo M/F:')).strip().upper()
    si += idade
    if s == 'M':
        ls.append(idade)
        dc[idade] = nome
    elif idade < 20:
        sf += 1
    ls.sort()
if ls == []:
    ls = [0]
print(f'\nMedia Idades : {si/4}\nNome homem mais velho: {dc[ls[len(ls)-1]]}\nMulheres com menos de 20 anos: {sf}')
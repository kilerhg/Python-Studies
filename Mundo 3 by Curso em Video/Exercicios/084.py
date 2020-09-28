# leia o nome e peso de varias pessoas e armazenar em uma lista, no final mostrar:
# A - Quantas pessoas forma cadastradas
# B - Uma listagem com as pessoas mais pesadas
# C - Uma listagem com as pessoas mais leves
ma = me = 0

lista = list()
dados = list()
nma = list()
nme = list()
while True:
    dados.append(str(input('Digite seu Nome: ')))
    dados.append(float(input('Digite seu Peso: ')))
    lista.append(dados[:])
    dados.clear()
    flag = str(input('Deseja Continuar [S/N]:')).strip().upper()[0]
    if flag in 'N':
        break

for x in range(0,len(lista)):
    if x == 0:
        ma = lista[x][1]
        me = lista[x][1]
        nma.append(lista[x][0])
        nme.append(lista[x][0])
    elif lista[x][1] > ma:
        ma = lista[x][1]
        nma.clear()
        nma.append(lista[x][0])
    elif lista[x][1] < me:
        me = lista[x][1]
        nme.clear()
        nme.append(lista[x][0])
    elif lista[x][1] == ma:
        nma.append(lista[x][0])
    elif lista[x][1] == me:
        nme.append(lista[x][0])
print(f'Foram Cadastradas {len(lista)} Pessoas')
print(f'As pessoas mais pesadas com: {ma} Kilos são :',end=' ')
for x in nma:
    print(x,end='...')
print(end='\n')
print(f'As Pessoas mais leves com: {me} Kilos são :',end=' ')
for x in nme:
    print(x,end='...')
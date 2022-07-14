# ler varios numeros e colocar em uma lista, criar duas listas extras que vão conter apenas os valores pares e os valores impares, ao final mostre o conteudo das tres lista
lista = []
flag = 'B'
listapar = []
listaimpar = []
while True:
    lista.append(int(input('Digite um valor:')))
    flag = str(input('Você deseja continuar [S/N]:')).strip().upper()[0]
    if flag not in 'SN':
        while True:
            flag = str(input('Você deseja continuar [S/N]:')).strip().upper()[0]
            if flag in 'SN':
                break
    if flag == 'N':
        break
for x in lista:
    if x % 2 == 0:
        listapar.append(x)
    else:
        listaimpar.append(x)
print(f'Os valores Digitados Foram: {lista}')
print(f'Os valores Pares Digitados Foram: {listapar}')
print(f'Os valores Impares Digitados Foram: {listaimpar}')
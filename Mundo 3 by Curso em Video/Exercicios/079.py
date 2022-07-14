# digitar varios valores numericos, caso o numero ja esteja na lista ele não adicionara, ao fim mostrar todos os numeros escritos de forma crescente
lista = []
flag = ''
while True:
    valor = int(input('Digite um valor:'))
    if len(lista) > 0:
        if valor not in lista:
            lista.append(valor)
            print(f'O valor {valor} foi adicionado com sucesso!!')
        else:
            print(f'O valor {valor} Não foi adicionado, Valor Repetido!!!')
    else:
        lista.append(valor)
        print(f'O valor {valor} foi adicionado com sucesso!!')
    if flag in 'SN':
        while True:
            flag = str(input('Deseja Continuar [S/N]:')).strip().upper()[0]
            if flag in 'SN':
                break
    if flag in 'N':
        break
lista.sort()
print(f'O valor da lista: {lista}')
# ler varios numeros e colocar em uma lista depois disso, mostrar:
# A- Quantos numeros foram digitados
# B- A lista de valores ordenada de forma decrescente
# C- Se o valor 5 foi digitado e está ou não na lista
lista = []
while True:
    lista.append(int(input('Digite um valor:')))
    flag = str(input('Você deseja continuar? [S/N]:')).strip().upper()[0]
    if flag not in 'SN':
        while True:
            flag = str(input('Você deseja continuar? [S/N]:')).strip().upper()[0]
            if flag in 'SN':
                break
    if flag == 'N':
        break
print(f'{len(lista)} Numeros foram Digitados')
lista.sort()
print(f'A lista de forma decrescente: {lista[::-1]}')
if lista.count(5) > 0:
    print(f'O valor 5 está na lista')
else:
    print('O valor 5 Não está na lista')
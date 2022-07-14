# a tabuada de varios numeros, ume de cada vez para cada valor que o usuario digitar, o programa sera interrompido quando o flag for negativo.
while True:
    print('= ='*20)
    n = int(input('Digite um Valor Inteiro:'))
    if n < 0:
        print(f'Valor negativo digitado: {n}, Parando...')
        break
    for x in range(1,11):
        print(f' {n} * {x} = {n*x}')
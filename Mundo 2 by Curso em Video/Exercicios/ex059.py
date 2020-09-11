# Leia dois valores e mostre um menu: 1-somar, 2-multiplicar, 3-maior, 4-novos Numeros, 5-Sair do programa. realizar cada operação
n1 = float(input('Digite Um Numero:'))
n2 = float(input('Digite Um Numero:'))
f = 0
while f != 5:

    print(f'''
    {'= ='*15}
     Menu Contas

    1 - Somar

    2 - Multiplicar

    3 - Maior

    4 - Novos Numeros

    5 - Sair do Programa
    
    {'= ='*15}    
    ''')
    f = int(input('Digite um dos Valores:'))

    if f == 1:
        print(f' A soma {n1} + {n2} = {n1+n2}')
    elif f == 2:
        print(f' A multiplicação {n1} x {n2} = {n1*n2}')
    elif f == 3:
        if n1 == n2:
            print(f' Os Valores {n1} e {n2} São Iguais')
        elif n1 > n2:
            print(f' O valor {n1} é maior que o valor {n2}')
        else:
            print(f' O valor {n2} é maior que o valor {n1}')
    elif f == 4:
        n1 = float(input('Digite Um Numero:'))
        n2 = float(input('Digite Um Numero:'))
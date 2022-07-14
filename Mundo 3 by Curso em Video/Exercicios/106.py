# faça um mini-sistema que utilize o interactive help do python, o usuario vai digitar o comando e
# e o manual vai aparecer. quando o usuario digitar a palavra fim, o programa se encerrara.
# use cores

def persohelp():
    m1 = '  Sistema de Ajuda do Python  '
    m3 = '  Obrigado ;), Volte sempre  '
    while True:
        print('\033[0;33;44m*' * len(m1))
        print(m1)
        print('*' * len(m1))
        flag = str(input('\033[mDigite uma Função ou Biblioteca que deseja visualizar ajuda para sair digite [fim] :')).strip().lower()
        m2 = f'  Acessando a ajuda do comando {flag} ...  '
        if flag == 'fim':
            print('\033[0;33;41m*' * len(m3))
            print(m3)
            print('*' * len(m3))
            break
        print('\033[0;37;40m*' * len(m2))
        print(m2)
        print('*' * len(m2))
        print('\033[0;30;45m ')
        help(flag)


persohelp()


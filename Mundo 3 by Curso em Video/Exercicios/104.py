# crie um programa que tenha a função leiaint() que vai funcionar de
# forma semelhante a funcao input do python, so que fazendo a validacao para aceitar apenas um valor numerico inteiro.
def leianint():
    while True:
        n1 = input('Digite um numero Inteiro:')
        if n1.isnumeric():
            n1 = int(n1)
            break
        else:
            print('Erro, Por favor Digite um numero Inteiro')
    return n1


# Programa Principal
leianint()

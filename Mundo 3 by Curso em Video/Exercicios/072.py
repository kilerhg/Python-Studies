# tenha uma tupla totalmente preenchida de 0 a 20 escrita# crie um programa que vai gerar 5 numeros aleatorios e colocar em uma tupla, depois disso mostre a listagem de numeros gerados e tambem indique o menor e o maior valor que esta na tupla por extenso ler um numero pelo teclado entre 0 e 20 e mostrar na tela por extenso
extenso = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
flag = ''
while not flag == 'N':
    n1 = -1
    while not 0 <= n1 <= 20:
        n1 = int(input('Digite um numero entre zero e vinte: '))
    print(f'O valor {n1} por extenso É : {extenso[n1]}')
    flag = str(input('Você deseja continuar?: [S/N]:')).strip().upper()[0]
    if flag not in 'SN':
        while flag not in 'SN':
            flag = str(input('Você deseja continuar?: [S/N]:')).strip().upper()[0]


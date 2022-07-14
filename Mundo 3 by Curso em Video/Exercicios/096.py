# Faça uma função que receba as dimensoes de um terreno retangular(largura e altura) e mostre a area do terreno
def area(largura,altura):
    area = largura * altura
    print(f'O terreno tem dimensões de {largura}x{altura} com Área: {area}')


n1 = float(input('Digite a Largura:'))
n2 = float(input('Digite a Altura:'))
area(n1,n2)
'''

Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.
Entrada

O arquivo de entrada contém três valores com um dígito após o ponto decimal.
Saída

O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima,
 sempre com mensagem correspondente e um espaço entre os dois pontos e o valor. O valor calculado deve ser apresentado com 3 dígitos após o ponto decimal.

'''
line = input().split(" ")
a,b,c = line

a=float(a)
b=float(b)
c=float(c)
pi = 3.14159

triangulo = (a * c) / 2 
circulo = ((c ** 2)*pi)
trapezio = (((a + b)*c)/2)
quadrado = (b ** 2)
retangulo = (a * b)

print('TRIANGULO: %.3f'%triangulo)
print('CIRCULO: %.3f'%circulo)
print('TRAPEZIO: %.3f'%trapezio)
print('QUADRADO: %.3f'%quadrado)
print('RETANGULO: %.3f'%retangulo)

'''
print('TRIANGULO: %.3f'%triangulo,'\nCIRCULO: %.3f'%circulo,'\nTRAPEZIO: %.3f'%trapezio,'\nQUADRADO: %.3f'%quadrado,'\nRETANGULO: %.3f'%retangulo)
'''

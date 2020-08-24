'''

Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:


Perimetro = XX.X


Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem


Area = XX.X
Entrada

A entrada contém três valores reais.
Saída

O resultado deve ser apresentado com uma casa decimal.

'''

linha = input().split(' ')
A,B,C = linha
A = float(A)
B = float(B)
C = float(C)


if A < ( B + C ) and B < ( A + C ) and C < ( A + B )  :
    print('Perimetro = %.1f'%(A+B+C))
else:
    print('Area = %.1f' % (((A+B)/2)*C))



'''
if A > B and A > C :
    if A < (B + C) :
        print('Perimetro = %.1f'%(A+B+C))
    else :
        print('Area = %.1f' % (((A+B)/2)*C))

if B > A and B > C :
    if B < (A + C) :
        print('Perimetro = %.1f'%(A+B+C))
    else :
        print('Area = %.1f' % (((A+B)/2)*C))

if C > A and C > B :
    if C < (A + B) :
        print('Perimetro = %.1f'%(A+B+C))
    else :
        print('Area = %.1f' % (((A+B)/2)*C))
'''
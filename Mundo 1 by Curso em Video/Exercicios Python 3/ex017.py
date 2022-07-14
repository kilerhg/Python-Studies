# calcular o valor da hipotenusa
from math import hypot
n1 = float(input('Digite o primeiro cateto:'))
n2 = float(input('Digite o segundo cateto:'))
print(f'O valor da hipotenusa é: {hypot(n1,n2):.3f}')
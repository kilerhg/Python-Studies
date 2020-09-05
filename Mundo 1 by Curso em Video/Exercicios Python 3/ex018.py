# leia um angulo e mostre seno coseno tangente
from math import cos,tan,sin,radians
n1 = int(input('Digite um angulo:'))
print(f'O valor do seno: é {sin(radians(n1)):.2f}\nO valor do coseno: {cos(radians(n1)):.2f}\nO valor da tangente: {tan(radians(n1)):.2f}')
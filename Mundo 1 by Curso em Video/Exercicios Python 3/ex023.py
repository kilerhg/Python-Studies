# leia um numero de 0 a 9999 e mostre na tela cada digito separado, por unidade dezena centena milhar
n1 = int(input('Digite um numero de 0 a 9999:'))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10

print(f' O numero digitado tem {m} Milhare(s)')
print(f' O numero digitado tem {c} Centena(s)')
print(f' O numero digitado tem {d} Dezena(s)')
print(f' O numero digitado tem {u} Unidade(s)')
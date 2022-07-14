# Leia varios numeros inteiros pelo teclado, no final da execução, mostre a media e qual foi o maior e o menor. o programa deve perguntar ao usuario se ele quer continuar ou não a digitar valores
flag = 'a'
sm = 0
ct = 0
ls = []
while flag not in 'Ss':
    print('= ='*15)
    n = int(input('Digite um numero:'))
    flag = str(input('Deseja parar? [S/N]:'))
    sm += n
    ct += 1
    ls.append(n)
print(f'A media dos Numeros Digitados é: {sm/ct}\nO maior numero digitado é: {max(ls)}\nO menor Numero Digitado: {min(ls)}')
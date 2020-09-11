# receba uma quantidade n de numeros inteiros e mostre na tela os n primeiros elementos de uma sequencia de fibonaci

nf = int(input('Digite a quantidade de numeros da Sequencia Fibonnaci desejado:'))
cf = 0
n1 = 1
n2 = 1
n3 = n1+n2
while cf != nf:
    if cf+1 != nf:
        print(n1,end=' -> ')
    else:
        print(n1,end='')
    n1 = n2
    n2 = n3
    n3 = n1+n2
    cf += 1



#print(f'Teste : {n1} {n2} {n3}')


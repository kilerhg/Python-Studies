# leia o comprimento de 3 retas e verifique se podem formar um triangulo ou não
r1 = float(input('Digite uma reta do triangulo:'))
r2 = float(input('Digite uma reta do triangulo:'))
r3 = float(input('Digite uma reta do triangulo:'))
lista = [r1,r2,r3]
lista.sort()
n1,n2,n3 = lista
if (((n2-n3) < n1 < (n2 + n3)) and ((n1-n3) < n2 < (n1+n3)) and ((n1-n2) < n3 < (n1+n2))):
    print('Pode se formar um triangulo com essas medidas')
else:
    print('Não é possivel formar um triangulo com essas medidas')
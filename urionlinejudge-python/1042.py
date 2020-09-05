'''

Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.
Entrada

A entrada contem três números inteiros.
Saída

Imprima a saída conforme foi especificado.

'''

linha = input().split(' ')
num1,num2,num3 = linha
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

if num1 < num2 and num1 < num3 :
    print(num1)
    if num2 < num3 :
        print(num2)
        print(num3)
    else: 
        print(num3)
        print(num2)

if num2 < num1 and num2 < num3 :
    print(num2)
    if num1 < num3 :
        print(num1)
        print(num3)
    else: 
        print(num3)
        print(num1) 

if num3 < num1 and num3 < num2 :
    print(num3)
    if num1 < num2 :
        print(num1)
        print(num2)
    else: 
        print(num2)
        print(num1)

print('')
print(num1)
print(num2)
print(num3)








'''
if num1 > num2 or num3 : 
    if num1 > num2 and num3 :
        if num2 > num3 :
            ord1 = num1
            ord2 = num2
            ord3 = num3
        else :
            ord1 = num1
            ord2 = num3
            ord3 = num2
    if num2 > num1 and num3 :
        ord1 = num2
        ord2 = num1
        ord3 = num3
    if num3 > num1 and num2 :
        ord1 = num3
        ord2 = num1
        ord3 = num2
'''
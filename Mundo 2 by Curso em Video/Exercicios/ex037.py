# Leia um numero inteiro qualquer e peça para o usuario qual base de conversão sendo 1 para binario - 2 octal - 3 para hexadecimal

numero = int(input('Digite um numero:'))
choice = int(input('''
Digite A base de conversão que gostaria sendo:
1 - Binario
2 - Octal
3 - Hexadecimal
Digite:'''))

dic = {1:'Binario',2:'Octal',3:'Hexadecimal'}
if choice == 1:
    base = 1
    resultado = bin(numero)[2:]
elif choice == 2:
    base = 2
    resultado = oct(numero)[2:]
elif choice == 3:
    base = 3
    resultado = hex(numero)[2:]
else:
    print('Digite um numero valido')
    exit()
print(f'O seu numero {numero} na base {dic[base]} é: {resultado}')
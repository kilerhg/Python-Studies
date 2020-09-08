# Leia o Peso e altura e calcule o  IMC e mostre seu status abaixo de 18.5: abaixo do peso, entre 18.5 e 25:peso ideal. 30 até 40: obesidade, acima de 40: obesidade morbida
peso = float(input('Digite seu Peso(Em kilos):'))
altura = float(input('Digite sua Altura(Em Metros):'))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc <= 25:
    print('Peso Ideal')
elif 25 < imc <= 29.9:
    print('Sobrepeso')
elif 30 <= imc <= 40:
    print('Obesidade')
else:
    print('Obesidade Morbida')
print(f'Com o imc: {imc:.2f}')

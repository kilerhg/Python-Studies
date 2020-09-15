# leia varios numeros inteiros e quando for digitado 999 parar, no final mostrar quantidade de numeros digitados e a soma deles, descosiderando o flag (999)
sm = 0
ct = 0
while True:
    n = int(input('Digite um valor inteiro:'))
    if n == 999:
        break
    ct += 1
    sm += n
print(f'Você Digitou {ct} Numeros, Com Valor {sm} Somados')
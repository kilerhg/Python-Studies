# leia quatro valores pelo teclado e guardalos em uma tupla, no final mostrar, quantas vezes apareceu o valor 9.
# em que posição foi digitado o primeiro valor 3, quais foram os numeros pares.
valores = pares = tuple()

   # Forma Realizada

for x in range(0,4):
    inpu = input('Digite um valor:')
    valores += tuple(inpu)
    if int(inpu) % 2 == 0:
        pares += tuple(str(inpu))
"""

    # forma alternativa
inpu = (int(input('Digite um valor:')),
        int(input('Digite um valor:')),
        int(input('Digite um valor:')),
        int(input('Digite um valor:')))
for x in range(0,4):
    if int(inpu[x]) % 2 == 0:
        pares += tuple(str(inpu[x]))
valores = inpu
"""


print(f'Os Valores digitados foram: {valores}')
if 9 in valores or '9' in valores:
    print(f'O Numero 9 foi digitado {valores.count("9")} Vezes')
else:
    print('O valor 9 não foi digitado')
if 3 in valores or '3' in valores:
    print(f'A Posição digitada do Numero 3 foi : {valores.index("3")}')
else:
    print('O valor 3 não foi Digitado')
if len(pares) != 0:
    print('Os numeros pares são : ', end = '')
    for x in pares:
        print(x,end = ' ')
else:
    print('Não Foram digitados Numeros pares')
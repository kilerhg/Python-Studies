from random import randint,choice,shuffle

def gerar_caracter(senha='',mai=True,min=True,espe=True,nume=True):
    letras_mai = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letras_min = letras_mai.lower()
    vogais_min = 'áâãéêíîóôõúû'
    vogais_mai = 'ÁÂÃÉÊÍÎÓÔÕÚÛ'
    especiais = '!@#$%&*()-+.,;?{[}]^><:'
    numeros = list(range(0,10))
    rnd = randint(0, 6)
    if rnd == 1 and mai == True:
        caracter = choice(letras_mai)
    elif rnd == 2 and min == True:
        caracter = choice(letras_min)
    elif rnd == 3 and nume == True:
        caracter = choice(numeros)
    elif rnd == 4 and min == True:
        caracter = choice(vogais_min)
    elif rnd == 5 and mai == True:
        caracter = choice(vogais_mai)
    elif rnd == 6 and espe == True:
        caracter = choice(especiais)
    else:
        caracter = ''
    return caracter


def gerar_senha(caracteres=15,mai=True,min=True,espe=True,nume=True):
    senha = ''
    for x in range(0,caracteres):
        caracter = gerar_caracter(senha, mai, min, espe, nume)
        if caracter == '':
            while True:
                caracter = gerar_caracter(senha, mai, min, espe, nume)
                if caracter != '':
                    break
        senha += str(caracter)
    return senha
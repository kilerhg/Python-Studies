# aumentar(),
# diminuir()
# dobro()
# metade()

def aumentar(numero,quanto,formatar=False):
    resultado = numero + numero * (quanto/100)
    if formatar == True:
        resultado = moeda(resultado)
    return resultado


def diminuir(numero,quanto,formatar=False):
    resultado = numero - numero * (quanto/100)
    if formatar == True:
        resultado = moeda(resultado)
    return resultado


def dobro(numero,formatar=False):
    resultado = numero * 2
    if formatar == True:
        resultado = moeda(resultado)
    return resultado


def metade(numero,formatar=False):
    resultado = numero*0.5
    if formatar == True:
        resultado = moeda(resultado)
    return resultado


def moeda(numero):
    numero = str(numero)
    if numero.count(',') > 0:
        numero = numero.replace(',','.')
        numero = float(numero)
    numero = float(numero)
    numero = f'R${numero:.2f}'
    numero = str(numero)
    numero = numero.replace('.',',')
    return numero





# aumentar(),
# diminuir()
# dobro()
# metade()

def aumentar(numero,quanto):
    resultado = numero + numero * (quanto/100)
    return resultado


def diminuir(numero,quanto):
    resultado = numero - numero * (quanto/100)
    return resultado


def dobro(numero):
    return numero*2


def metade(numero):
    return numero*0.5


def moeda(numero,moeda='R$'):
    numero = str(numero)
    if numero.count(',') > 0:
        numero = numero.replace(',','.')
        numero = float(numero)
    numero = float(numero)
    numero = f'{moeda}{numero:.2f}'
    numero = str(numero)
    numero = numero.replace('.',',')
    return numero




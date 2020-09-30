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

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

def resumo(numero,quanto,formatar=False):
    print('-*' * 30)
    print(f'O dobro  de {moeda(numero)} é   {dobro(numero, formatar)}')
    print(f'A metade de {moeda(numero)} é   {metade(numero, formatar)}')
    print(f'O numero    {moeda(numero)} com {quanto}% de aumento fica: {aumentar(numero, quanto, formatar)}')
    print(f'O numero    {moeda(numero)} com {quanto}% de redução fica: {diminuir(numero, quanto, formatar)}')
    print('-*' * 30)






# uma função que receba um texo qualquer como parametro e mostre uma mensagem com tamanho dinamico

def mensagem(texto):
    print('-'*len(texto))
    print(texto)
    print('-'*len(texto))


mensagem(' curso de python by curso em video ')
mensagem(' curso de python ')
mensagem(' curso ')


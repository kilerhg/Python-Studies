'''
Levantando Erros com Raise

raise -> Lança um erro

Utilizado em geral para gerar mensagens de erro personalizadas

ex:

raise TipoDoErro('Mensagem de erro')

'''


def colore(texto : str, cor : str):
    if type(texto) is not str:
        raise TypeError('O texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('A Cor precisa ser uma string')
    print(f'o texto {texto} está com a cor {cor}')

colore('kiler', 7)

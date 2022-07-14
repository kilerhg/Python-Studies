# uma funcao chamada voto que vai receber como parametro o ano de nascimento de uma pessoas, retornando um valor literal indicando se uma pessoa tem voto : NEGADO, OPCIONAL OU OBRIGATORIO
# Sendo voto obrigatorio no campo 17(negado) < obrigatorio < 65(opcional)
from datetime import datetime


def voto(ano):
    """
     -> programa para identificar se a pessoa pode ou não votar
    :param idade: Ano de nascimento
    :return: se pode ou não votar
    """
    global idade
    anoa = datetime.today().year
    idade = anoa - ano
    if idade < 16:
        votar = 'NEGADO'
    elif 18 <= idade <= 65:
        votar = 'OBRIGATORIO'
    elif 65 < idade or 16 <= idade < 18:
        votar = 'OPCIONAL'
    return votar


# Programa Principal
n1 = int(input('Digite seu ano de nascimento:'))
voto(n1)
print(f'Com {idade} Anos de idade é {voto(n1)} Votar!!!')

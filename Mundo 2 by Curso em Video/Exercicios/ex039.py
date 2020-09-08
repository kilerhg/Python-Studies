# informe o ano de nascimento se ele ainda vai se alistar, se é hora, passou do tempo. e mostar quanto tempo falta ou tempo que passou
from datetime import date
anoa = int(date.today().year)
anon = int(input('Digite seu ano de nascimeto:'))

if (anoa - anon) == 18:
    print('Ano de se alistar')
elif (anoa - anon) < 18:
    print(f'Você ainda ira se alistar em {((anoa-anon)-18)*-1} Ano(s)')
else:
    print(f'Voce já passou do ano de alistamento em {(anoa-anon)-18} Ano(s)')


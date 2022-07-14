import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime

# entrar no site dos cinemas : https://www.cinemark.com.br/osasco/cinemas


resposta = requests.get('https://www.cinemark.com.br/osasco/cinemas')

conteudo = resposta.content

site = BeautifulSoup(conteudo,'html.parser')


filmes = site.find('div',attrs={'class':'tabs-content'})

filme = filmes.find_all('div',attrs={'class':'theater'})

# print(filme.prettify())





# salas e horarios : ul- class > theater-times


for i in filme:
    salas = i.find('ul',attrs={'class':'theater-times'}).find_all('li')
    nome = i.find('div',attrs={'class':'title'}).text.strip()
    trailer = i.find('a',attrs={'class':'btn btn-trailer-play'})
    link_trailer = trailer['href']

    print(f'Titulo : {nome}')
    print(f'Link_Trailer : {link_trailer[2:]}')
    for x in salas:
        sala = x.find('span',attrs={'class':'times-auditorium'})
        tipo = i.find('span',attrs={'class':'label-dub'})
        try:
            horario = '-'.join(salas[0].find('ul', attrs={'class': 'times-options'}).text.split())
            print(sala.text,end='  ')
            print(horario)
            print(tipo.text)
            print()
        except:
            pass
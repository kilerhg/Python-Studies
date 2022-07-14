 # Entrar No site ; https://faceitstats.com/player/
 # Buscar ultimas partidas: Resultado,placar,placar player, k/d, hs,mapa, elo, link

import requests
from bs4 import BeautifulSoup
import sqlite3

player = 'gmzfabian'

resposta = requests.get(f'https://faceitstats.com/player/{player}')
conteudo = resposta.content
site = BeautifulSoup(conteudo,'html.parser')
resultados = site.find('table',attrs={'class':'table table-striped table-hover'}).find('tbody')

linha = resultados.find_all('tr')
partidas = []

for i in linha:
    colunas = i.find_all('td')
    colunas_linhas = []
    partida = {}

    for posx, x in enumerate(colunas):
        if str(posx) in '0235679' or posx == 10:
            try:
                a = x.find('a')
                colunas_linhas.append(f'https://faceitstats.com' + a['href'])
            except:
                colunas_linhas.append(f'{x.text.strip()}')
    partida['resultado'] = colunas_linhas[0]
    pontos = [eval(colunas_linhas[1][:2]),eval(colunas_linhas[1][-2:])]
    pontos.sort()
    if partida['resultado'] == 'LOSS':
        partida['pontos_feitos'] = pontos[0]
        partida['pontos_tomados'] = pontos[1]
    else:
        partida['pontos_feitos'] = pontos[1]
        partida['pontos_tomados'] = pontos[0]
    partida['kills'] = eval(colunas_linhas[2][:2])
    partida['death'] = eval(colunas_linhas[2][-2:])
    partida['kd'] = eval(colunas_linhas[3])
    try:
        partida['hs'] = eval(colunas_linhas[4][:2])
    except:
        partida['hs'] = eval(colunas_linhas[4][0])
    partida['mapa'] = colunas_linhas[5][3:]
    try:
        partida['elo'] = eval(colunas_linhas[6][:4])
    except:
        partida['elo'] = 'n/a'
    partida['link'] = colunas_linhas[7]
    partidas.append(partida.copy())
    partida.clear()


try:
    banco = sqlite3.connect('banco_dados_partidas.db')
    cursor = banco.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS partidas (
    id integer PRIMARY KEY AUTOINCREMENT,
    resultado text,
    rounds_ganhados integer,
    rounds_perdidos integer,
    kills integer,
    deaths integer,
    kd text,
    hs integer,
    mapa text,
    elo integer,
    link text
    )''')
    banco.commit()
    banco.close()
except sqlite3.Error as erro:
    print(erro)

for x in partidas:
    try:
        banco = sqlite3.connect('banco_dados_partidas.db')
        cursor = banco.cursor()
        cursor.execute(f'''INSERT INTO partidas VALUES (NULL,'{x["resultado"]}','{x["pontos_feitos"]}','{x["pontos_tomados"]}','{x["kills"]}','{x["death"]}','{x["kd"]}','{x["hs"]}','{x["mapa"]}','{x["elo"]}','{x["link"]}')''')
        banco.commit()
        banco.close()
    except sqlite3.Error as erro:
        print(f'Erro: {erro}')
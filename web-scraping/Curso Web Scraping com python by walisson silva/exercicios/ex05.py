import requests
from bs4 import BeautifulSoup
import sqlite3

# Entrar no site G1 e procurar as ultimas noticas
# Separar Titulo / descrição / link / Local / tema

resposta = requests.get('https://g1.globo.com/ultimas-noticias/')

conteudo = resposta.content

site = BeautifulSoup(conteudo,'html.parser')

# Manchetes : div class="bstn-fd bstn-fd-csr"

manchetes = site.find('div',attrs={'id':'bstn-launcher'})

noticia = manchetes.find('div',attrs={'class':'bastian-page'})

noticias = noticia.find_all('div',attrs={'class':'bastian-feed-item'})


for x in noticias:
    # Titulo : <div class="_ee">
    titulo = x.find('div',attrs={'class':'_ee'}).find('a')
    link = titulo['href']

    # Descrição (opc) : <div class="feed-post-body-resumo">
    try:
        descricao = x.find('div',attrs={'class':'feed-post-body-resumo'}).text
    except:
        descricao = 'N/A'

    # Tema/local : <span class="feed-post-metadata-section">

    local_tema = x.find('span',attrs={'class','feed-post-metadata-section'}).text

    print(f'''
    Titulo    : {titulo.text.strip()}
    Descrição : {descricao.strip()}
    Tema      : {local_tema.strip()}
    link      : {link.strip()}
    ''')
    print()


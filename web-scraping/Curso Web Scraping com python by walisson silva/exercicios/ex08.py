import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime

#Entrar no site neshastore: http://www.neshastore.com/cs-go/skins-cs-go?limit=100&page=1
# buscar informações sobre skin, link, preço

resposta = requests.get('http://www.neshastore.com/cs-go/skins-cs-go?limit=100&page=1')

conteudo = resposta.content

site = BeautifulSoup(conteudo,'html.parser')


# skins fora estoque : div class="product-list-item xs-100 sm-100 md-100 lg-100 xl-100 outofstock"
# skins normal       : div class="product-list-item xs-100 sm-100 md-100 lg-100 xl-100"
# skins              : div class="main-products product-list"

skin = site.find('div',attrs={'class':'main-products product-list'}).find('div',attrs={'div',''})

# print(skin.prettify())

nome_skin = skin.find('div',attrs={'class':'name'})
descricao = skin.find('div',attrs={'class':'description'})
precos = skin.find('div',attrs={'class':'price'})

print(nome_skin)
print(descricao)
print(precos)
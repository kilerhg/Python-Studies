import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime


data = datetime.now().date()
resposta = requests.get('https://www.infomoney.com.br/ferramentas/cambio/')

conteudo = resposta.content

site = BeautifulSoup(conteudo,'html.parser')

# print(site.prettify())

# bloco ? div class="row mt-5"

bloco = site.find('div',attrs={'class':'row mt-5'})

# print(bloco.prettify())
moeda = bloco.find_all('tr')

cotacoes = []
dic = {}

for x in moeda[1:]:

    # print(moeda[2].prettify())

    objetos = x.find_all('td')

    # print(objetos[2].prettify())

    dic['nome_moeda'] = objetos[0].text
    dic['compra_moeda'] = objetos[2].text
    dic['venda_moeda'] = objetos[3].text
    dic['var_moeda'] = objetos[4].text
    cotacoes.append(dic.copy())
    dic.clear()

for x in cotacoes:
    print(f'Moeda  : {x["nome_moeda"]}')
    print(f'Compra : {x["compra_moeda"]}')
    print(f'Venda  : {x["venda_moeda"]}')
    print(f'Var    : {x["var_moeda"]}')
    print()


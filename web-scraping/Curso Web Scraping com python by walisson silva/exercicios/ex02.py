import requests
from bs4 import BeautifulSoup

# Objetivo Entrar na DRAFT5 e buscar os TOP 30 times br hoje
# Achar nome do time / pontos / Posição



# Entrando no ranking


resposta = requests.get('https://draft5.gg/ranking')

conteudo = resposta.content

site = BeautifulSoup(conteudo,'html.parser')

time = site.find_all('a',attrs={'class':'ranking__Team-sc-4i0u5j-0 kNpyLG'})


# print(time[1].prettify())



# class="ranking__Position-sc-4i0u5j-2 btxPKz"
# class="ranking__Position-sc-4i0u5j-2 btxPLO"

# class="ranking__TeamName-sc-4i0u5j-4 gMuPWC"
# class="ranking__TeamName-sc-4i0u5j-4 bDnmFP"

# <span class="ranking__Points-sc-4i0u5j-5 jPqvFH">
# <span class="ranking__Points-sc-4i0u5j-5 jPqvDf">

# posição : <span class="ranking__Position-sc-4i0u5j-2 btxPKz">

times = []
dic = {}
for x in time:

    posicao = x.find('span',attrs={'class':'ranking__Position-sc-4i0u5j-2'})

    # Nome : <h2 class="ranking__TeamName-sc-4i0u5j-4 bDnmFP">
    nome = x.find('h2',attrs={'class':'ranking__TeamName-sc-4i0u5j-4'})

    # Pontos : <span class="ranking__Points-sc-4i0u5j-5 jPqvFH">
    pontos = x.find('span',attrs={'class':'ranking__Points-sc-4i0u5j-5'})


    dic['posicao'] = f'{posicao.text[1:]:0>2}'
    dic['nome'] = nome.text
    dic['pontos'] = pontos.text[:-4]
    times.append(dic.copy())
    dic.clear()

# for x in times:
#     print(x['posicao'])
#     print(x['nome'])
#     print(x['pontos'])
#     print()

for x in times:
    print(x)
import requests
from bs4 import BeautifulSoup

# Buscando as principais noticias do g1 e salvando em lista

resposta = requests.get('https://g1.globo.com/')

conteudo = resposta.content

site = BeautifulSoup(conteudo, 'html.parser')

teste = site.find('div',attrs={'class':'feed-post-body'})


# bstn-hl-wrapper
teste = site.find_all('div',attrs={'class':'feed-post-body'})
# Html da noticia


# noticia = site.find('div',attrs={'class':'feed-post-body'})

# Titulo da noticia : a class="feed-post-link
noticias = []
noticia = {}
for x in teste:
    titulo = x.find('a',attrs={'class':'feed-post-link'})
    link_titulo = titulo['href']
    conteudo = x.find('div',attrs={'class':'feed-post-body-resumo'})
    noticia['titulo'] = titulo.text
    try:
        noticia['conteudo'] = conteudo.text
    except:
        noticia['conteudo'] = 'Vazio'
    noticia['link'] = link_titulo
    noticias.append(noticia.copy())
    noticia.clear()

for x in noticias:
    print(f'Titulo   : {x["titulo"]}')
    print(f'Conteúdo : {x["conteudo"]}')
    print(f'Link     : {x["link"]}')
    print()
# print(titulo.text)






# Subtitulo : div class="feed-post-body-resumo">

# subtitulo = noticia.find('div',attrs={'class':'feed-post-body-resumo'})
# print(subtitulo.text)



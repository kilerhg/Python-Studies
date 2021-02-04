import requests
from bs4 import BeautifulSoup

resposta = requests.get('https://g1.globo.com/')

conteudo = resposta.content

site = BeautifulSoup(conteudo, 'html.parser')


# Html da noticia
noticia = site.find('div',attrs={'class':'feed-post-body'})


# Titulo da noticia : a class="feed-post-link
titulo = noticia.find('a',attrs={'class':'feed-post-link'})

print(titulo.text)


# Subtitulo : div class="feed-post-body-resumo">

subtitulo = noticia.find('div',attrs={'class':'feed-post-body-resumo'})
print(subtitulo.text)



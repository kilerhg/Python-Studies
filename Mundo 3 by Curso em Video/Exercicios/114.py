# crie um codigo em python que teste se o site pudim.com.br está acessivel pelo computador usado

import urllib.request
site = 'http://pudim.com.br/'

try:
    teste = urllib.request.urlopen(site)
except:
    print('Site Pudim Não está disponivel ;(')
else:
    print('Site pudim Está disponivel ;)')
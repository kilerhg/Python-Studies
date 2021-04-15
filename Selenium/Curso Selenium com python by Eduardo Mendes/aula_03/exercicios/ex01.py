'''
Crie um programa em selenium que: Gere um dicionario onde a chave é a tag h1
O valor deve ser um novo dicionario, cada chave do valor devera ser o valor de atributo, cada valor deve ser o texto contido no elemento
url : https://curso-python-selenium.netlify.app/exercicio_01.html

Estrutura = {'H1':{'texto1':'Essa página é top de mais','texto2':'texto','texto3':'texto'}}


'''

# p.get_attribute('atributo')

from selenium.webdriver import Firefox
from time import sleep

navegador = Firefox()

url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'

navegador.get(url)

sleep(3)

dicionario = {}
dicionario['H1'] = {}

elementos = navegador.find_elements_by_tag_name('p')
for elemento in elementos:
    chave = elemento.get_attribute('atributo')
    valor = elemento.text
    dicionario['H1'][chave] = valor

print(dicionario)


navegador.quit()





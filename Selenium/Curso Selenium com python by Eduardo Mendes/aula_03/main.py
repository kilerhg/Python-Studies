from selenium.webdriver import Firefox
from time import sleep

url = 'https://curso-python-selenium.netlify.app/aula_03.html'

navegador = Firefox()

navegador.get(url)

# navegador.implicitly_wait(10) # forma do selenium para fazer o programa esperar
sleep(3) # forma nativa python para esperar

a = navegador.find_element_by_tag_name('a') # busca o primeiro elemento com a tag A
p = navegador.find_element_by_tag_name('p')
# navegador.find_elements_by_tag_name('p') # Busca todos os elementos com a tag p neste nivel DOM

for click in range(10):
    ps = navegador.find_elements_by_tag_name('p')
    a.click()
    print(f'Valor de p: {ps[-1].text} e valor do click(): {click}')

    print(f'Os valores sao iguais: {eval(ps[-1].text) == click}')


navegador.quit()
""" 
print(f'Texto de a: {a.text}')
print(f'Texto de p: {p.text}')

navegador.quit() """

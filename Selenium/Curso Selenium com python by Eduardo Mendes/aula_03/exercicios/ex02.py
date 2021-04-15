'''
Crie um programa em selenium que: jogue o jogo, quando voce ganha o script deve parar de ser executado
url : https://curso-python-selenium.netlify.app/exercicio_02.html
'''



from selenium.webdriver import Firefox
from time import sleep

navegador = Firefox()

url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'

navegador.get(url)

sleep(3)

geral = navegador.find_elements_by_tag_name('p')[1:]
botao = navegador.find_element_by_tag_name('a')
num_esperado = eval(geral[0].text[-1:])

a = 'asdasd'

cont = 0
while True:
    cont += 1
    botao.click()
    num_atual = navegador.find_elements_by_tag_name('p')[-1].text
    print(f'Numero Atual: {num_atual}, Numero Esperado: {num_esperado}')
    #if len(num_atual) > 2: Forma N1
    if eval(num_atual[-1]) == num_esperado:
        break

print(f'Você Ganhou !! : Esperado {num_esperado}, você {num_atual[-1]}')




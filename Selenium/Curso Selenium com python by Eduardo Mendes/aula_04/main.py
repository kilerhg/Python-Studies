from selenium.webdriver import Firefox

browser = Firefox()

url = 'https://selenium.dunossauro.live/aula_04_a.html'

browser.get(url)

lista_n_ordenada = browser.find_elements_by_tag_name('lu')
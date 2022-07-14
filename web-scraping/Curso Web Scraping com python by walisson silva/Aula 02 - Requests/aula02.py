import requests

resposta = requests.get('https://lucasnunes.me/')

print(f'Codigo de status: {resposta.status_code}')

print(f'Cabeçalho: {resposta.headers}')

print(f'Conteúdo: {resposta.content}')
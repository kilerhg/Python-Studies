import requests
from bs4 import BeautifulSoup

# Entrar no site da Draft5
# olhar as Tranferencias recentes do cenario
# Obter Data / Nome player / Como entava / onde foi

# RESULTADO Crawler entra no site Draft 5 e pega todas as tranferencias da pagina

# nome função e data: <div class="PlayerTransferCard__PlayerName-a6cth5-2 lkGCkk">
# Local   :   <a class="PlayerTransferCard__PlayerTeam-a6cth5-3 hFqQYb">
# Destino : <a class="PlayerTransferCard__PlayerTeam-a6cth5-3 hFqQYb">
# Fonte : <div class="PlayerTransferCard__RelatedNewsUrl-a6cth5-7 dxuOOi">
# Status Transferencia : <div class="PlayerTransferCard__TransferStatus-a6cth5-8 cCtQeS">

players = []
dic = {}

resposta = requests.get(f'https://draft5.gg/transferencias-e-rumores?p=1')

conteudo = resposta.content

site = BeautifulSoup(conteudo,'html.parser')
# class="Card__CardContainer-sc-122kzjp-0 ezXhSC PlayerTransferCard__PlayerTransfersCardContainer-a6cth5-0 lnAjkM"

transferencia = site.find_all('div',attrs={'class':'Card__CardContainer-sc-122kzjp-0 ezXhSC PlayerTransferCard__PlayerTransfersCardContainer-a6cth5-0 lnAjkM'})


# print(transferencia[1].prettify())


for x in transferencia:

    dados_player = x.find('div',attrs={'class':'PlayerTransferCard__PlayerName-a6cth5-2 lkGCkk'})
    nome_player = dados_player.find('h3')
    funcao_data = dados_player.find('small').text[-5:]
    local_destino = x.find_all('a',attrs={'class':'PlayerTransferCard__PlayerTeam-a6cth5-3 hFqQYb'})
    status = x.find('div', attrs={'class': 'PlayerTransferCard__TransferStatus-a6cth5-8 cCtQeS'})
    fonte = x.find('div', attrs={'class': 'PlayerTransferCard__RelatedNewsUrl-a6cth5-7 dxuOOi'}).find('a')

    local = local_destino[0].text
    destino = local_destino[1].text

    dic['Nick'] = nome_player.text.strip()
    dic['Data'] = funcao_data
    dic['Local'] = local.strip()
    dic['Destino'] = destino.strip()
    dic['status'] = status.text
    dic['fonte'] = fonte['href']
    players.append(dic.copy())
    dic.clear()

for x in players:
    print(x)


# for x in players:
#     print(f'''
#     Nickname : {x['Nick']}
#     Data     : {x['Data'] + '/2021'}
#     Local    : {x['Local']}
#     Destino  : {x['Destino']}
#     Status   : {x['status']}
#     Fonte    : {x['fonte']}
#     ''')




import requests
from bs4 import BeautifulSoup
import sqlite3

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

banco = sqlite3.connect('banco_dados.db')
cursor = banco.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS transferecias (
id integer PRIMARY KEY AUTOINCREMENT,
nick text,
data text,
local text,
destino text,
status text,
fonte text)""")
banco.commit()
banco.close()


ano = 2021
# cont = 0

for x in range(1,133):
    resposta = requests.get(f'https://draft5.gg/transferencias-e-rumores?p={x}')

    conteudo = resposta.content

    site = BeautifulSoup(conteudo,'html.parser')
    # class="Card__CardContainer-sc-122kzjp-0 ezXhSC PlayerTransferCard__PlayerTransfersCardContainer-a6cth5-0 lnAjkM"

    transferencia = site.find_all('div',attrs={'class':'Card__CardContainer-sc-122kzjp-0 ezXhSC PlayerTransferCard__PlayerTransfersCardContainer-a6cth5-0 lnAjkM'})


    # print(transferencia[1].prettify())


    for x in transferencia:
        # cont += 1
        dados_player = x.find('div',attrs={'class':'PlayerTransferCard__PlayerName-a6cth5-2 lkGCkk'})
        nome_player = dados_player.find('h3')
        funcao_data = dados_player.find('small').text[-5:]
        local_destino = x.find_all('a',attrs={'class':'PlayerTransferCard__PlayerTeam-a6cth5-3 hFqQYb'})
        status = x.find('div', attrs={'class': 'PlayerTransferCard__TransferStatus-a6cth5-8 cCtQeS'})
        fonte = x.find('div', attrs={'class': 'PlayerTransferCard__RelatedNewsUrl-a6cth5-7 dxuOOi'}).find('a')

        local = local_destino[0].text
        destino = local_destino[1].text



        try:
            mes_antigo = mes_atual
        except:
            pass

        dic['Data'] = funcao_data
        mes_atual = int(dic['Data'][-2:])

        try:
            if mes_antigo == 1 and mes_atual == 12:
                ano -= 1
        except:
            pass

        # if len(str(mes_old)) > 0:
        #     if mes_old == 12 and mes_atual == 1:
        #         ano -= 1
        # print(mes_old)
        dic['Nick'] = nome_player.text.strip()
        dic['Data'] = dic['Data'] + f'/{ano}'
        dic['Local'] = local.strip()
        dic['Destino'] = destino.strip()
        dic['status'] = status.text
        try:
            dic['fonte'] = fonte['href']
        except:
            dic['fonte'] = 'N/A'
        players.append(dic.copy())
        dic.clear()



# for x in players:
#     print(x)


for x in players:

    banco = sqlite3.connect('banco_dados.db')
    cursor = banco.cursor()
    cursor.execute(f"INSERT INTO transferecias VALUES (NULL,'{x['Nick'].lower()}','{x['Data']}','{x['Local']}','{x['Destino']}','{x['status']}','{x['fonte']}')")
    banco.commit()
    banco.close()

    # print(f'''
    # Nickname : {x['Nick']}
    # Data     : {x['Data'] + '/2021'}
    # Local    : {x['Local']}
    # Destino  : {x['Destino']}
    # Status   : {x['status']}
    # Fonte    : {x['fonte']}
    # ''')

# for x in players:
#     print(f'''
#     Nickname : {x['Nick']}
#     Data     : {x['Data'] + '/2021'}
#     Local    : {x['Local']}
#     Destino  : {x['Destino']}
#     Status   : {x['status']}
#     Fonte    : {x['fonte']}
#     ''')




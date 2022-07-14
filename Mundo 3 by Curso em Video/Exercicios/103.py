# uma função chamada ficha que receba dois parametros opcionais, o nome de um jogador e quantos gols ele marcou
# o programa devera ser capaz de mostrar a ficha do jogador, mesmo que algum dado não
# tenha sido informado corretamente

def ficha(nome='<Desconhecido>',gols=0):
    if str(nome).isnumeric():
        gols = nome
        nome = '<Desconhecido>'
    if len(nome) == 0:
        nome = '<Desconhecido>'
    if len(gols) == 0:
        gols = 0
    if gols.isnumeric():
        pass
    else:
        gols = 0

    print(f'O jogador {nome} marcou {gols} Gols!!')


# Programa Principal
nome = str(input('Digite o nome do jogador:')).strip().capitalize()
gols = input('Digite a quantidade de gols:')
ficha(nome,gols)

# aprimore o desafio 093 para que ele funcione com varios jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
jogadores = []
jogador = {}
gols = []
flag = 'a'
while True:
    jogador['nome'] = str(input('Digite o Nome do jogador:')).strip().capitalize()
    jogador['partidas'] = int(input('Digite quantas partidas foram jogadas:'))
    for x in range(0,jogador['partidas']):
        gols.append(int(input(f'Partida {x}: Digite quantos Gols:')))
        jogador['gols'] = gols[:]
    jogador['total'] = sum(jogador['gols'])
    jogadores.append(jogador.copy())
    gols.clear()
    flag = str(input('Deseja cadastrar mais algum jogador? [S/N]:')).strip().upper()[0]
    if flag in 'N':
        break
    print('*-'*20)

print(f'{"-="*10} Relatorio {"=-"*10}\n')
print(f'{"Numero": ^5}{"Nome": ^10}{"Gols": ^5}')
for pos, x in enumerate(jogadores):
    print(f'{pos:^5}{x["nome"]: ^12}{x["total"]: ^3}')
print()
print(f'{"-="*10} Relatorio {"=-"*10}\n')
flag = 0
while True:
    flag = int(input('Digite um jogador para Detalhamento [999 para sair]:'))
    print()
    if flag == 999:
        break
    elif flag > len(jogadores)-1:
        print('Tente Novamente:')
    else:
        print(f'{"*-"*5}Levantamento Jogador {jogadores[flag]["nome"]}{"*-"*5}')
        print()
        for pos, x in enumerate(jogadores[flag]['gols']):
            print(f'        Na partida {pos} Foram : {x} Gols!!')
        print()

'''
print(f'{"-="*10} Relatorio {"=-"*10}\n')
print(f' O jogador {jogador["nome"]} Jogou {jogador["partidas"]} Partidas \n')
for pos,x in enumerate(gols):
    print(f'        Na partida {pos} Foram : {x} Gols!!')
print()
print(f' Sendo no total {jogador["total"]} Gols')
print()
print(f'{"-="*10} Relatorio {"=-"*10}\n')
'''
# gerencia o aproveitamento de um jogador de futebol, o programa vai ler o nome do jogador e quantas partidas ele jogou,
# depois vai ler a quantidade de gols feitos em cada partida armazena em uma lista.
# no final, tudo isso sera guardado em um dicionario, incluindo o total de gols geitos durante o campeonato

jogador = {}
gols = []
jogador['nome'] = str(input('Digite o Nome do jogador:')).strip().capitalize()
partidas = int(input('Digite quantas partidas foram jogadas:'))


for x in range(0,partidas):
    gols.append(int(input(f'Partida {x}: Digite quantos Gols:')))
    jogador['gols'] = gols[:]
jogador['total'] = sum(jogador['gols'])
print()
print(f'{"-="*10} Relatorio {"=-"*10}\n')
print(f' O jogador {jogador["nome"]} Jogou {partidas} Partidas \n')
for pos,x in enumerate(gols):
    print(f'        Na partida {pos} Foram : {x} Gols!!')
print()
print(f' Sendo no total {jogador["total"]} Gols')
print()
print(f'{"-="*10} Relatorio {"=-"*10}\n')

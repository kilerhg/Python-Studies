# uma tupla com os 20 primeiros times da tabela do campeonato brasileiro de futebol, na ordem colocação. por fim mostrar,
# apenas os 5 primeiros colocados, os ultimos 4 colocados,
# um lista com os times em ordem alfabetica,
# em que posição na tabela esta o time do Grêmio

times = ('Atlético-MG','Internacional','São Paulo','Palmeiras','Vasco','Flamengo','Santos','Fortaleza','Fluminense','Sport','Ceará','Grêmio','Corinthians','Atlético-GO','Athletico','Coritiba','Bragantino','Botafogo','Bahia','Goiás')
print(f'Os times Participando são: {times}')
print(f'Os Primeiros 5 colocados Foram: {times[:5]}')
print(f'Os Ultimos 4 colocados foram: {times[-4:]}')
print(f'Os Times em ordem alfabetica fica: {sorted(times)}')
print(f'O Time do Grêmio esta na posição {times.index("Grêmio")+1}')
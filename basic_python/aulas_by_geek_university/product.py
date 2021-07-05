# from itertools import product

# anos = range(2020,2025)
# meses = range(1,13)
# for ano in anos:
#     for mes in meses:
#         print(f'{ano}-{str(mes).zfill(2)}')

from itertools import product

anos = range(2020,2025)
meses = range(1,13)
dias = range(1,31)
for ano, mes, dia in product(anos, meses, dias):
    print(f'{ano}-{str(mes).zfill(2)}-{str(dia).zfill(2)}')


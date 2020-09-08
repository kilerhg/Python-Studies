# leia o ano de nascimento até 9, Mirim até 14 infantil, até 19 junior, até 20: senior acima master
from datetime import date
anoh = date.today().year
anon = int(input('Digite seu ano de nascimento:'))
idade = anoh - anon
print(f'Idade : {idade}')
if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 25:
    print('Senior')
else:
    print('Master')
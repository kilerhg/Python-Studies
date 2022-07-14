# Crie um programa que faça o computador jogar Jokenpo com Você.
'''
1-pedra
2-papel
3-tesoura

3<1<2<3
'''


dc = {1:'Pedra',2:'Papel',3:'Tesoura'}

from random import randint
vpc = randint(1,3)

print(f'''
{"="*37}
Escolha Entre Pedra, Papel e tesoura
{"="*37}
''')
user = str(input('Escreva sua escolha:')).strip()
userp = str(user.upper())
if 'PEDRA' in userp:
    vuser = 1
elif 'PAPEL' in userp:
    vuser = 2
elif 'TESOURA' in userp:
    vuser = 3
else:
    print('Digite sua escolha corretamente!!')
    exit()

if vuser == vpc:
    print('\nEmpate')
elif (vpc == 3 and vuser == 1) or (vpc == 1 and vuser == 2) or (vpc == 2 and vuser == 3):
    print('\nParabenss, Você Ganhouu')
else:
    print('\nInfelizmente nesta você perdeu ;/')

print(f'\nVocê escolheu: {dc[vuser]}\nO Computador : {dc[vpc]}')

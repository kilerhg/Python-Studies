# crie um pequeno sistema modularizado que
# permita cadastrar pessoas pelo seu nome e idade em um arquivo de txt simples
# o sistema so vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas

from ex115 import *
from time import sleep

''' 
1 - Ver pessoas Que estão cadastradas
2 - Cadastrar novas Pessoas
3 - Sair do Programa
'''


while True:
    escolha = menu()
    if escolha == 1:
        lerDados()
        sleep(3)
    elif escolha == 2:
        nome = lerNome()
        idade = lerIdade()
        salvarDados(formatarTexto(nome,idade))
        print(f'O registro da pessoa {nome} foi salvo!!!')
        sleep(3)
    else:
        titulo('Obrigado, Volte Sempre!!!')
        break

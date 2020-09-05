'''


Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo,
sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.
Entrada

A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.
Saída

Apresente a duração do jogo conforme exemplo abaixo.

'''

linha = input().split(' ')
linha = list(map(int,linha))
HI,HF = linha

if HF <= HI :
    HF = HF + 24
duracao = HF - HI
print('O JOGO DUROU %.0f HORA(S)' %duracao)
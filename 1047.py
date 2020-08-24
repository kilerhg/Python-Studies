'''
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.
Entrada

Quatro números inteiros representando a hora de início e fim do jogo.
Saída

Mostre a seguinte mensagem: “O JOGO DUROU XX HORA(S) E YYY MINUTO(S)” .
'''

linha = input().split(' ')
linha = list(map(int,linha))
HI,MI,HF,MF = linha

MIT = HI * 60 + MI
MFT = HF * 60 + MF
HT = 24
MT = 0

if HI != HF and MI != MF :
    MIFT = MFT - MIT
    MT = int(MIFT % 60)
    HT = int((MIFT - MT) / 60)
print('O JOGO DUROU %d HORA(S) E %d MINUTO(S)' % (HT,MT))

'''
Tentativa 1


hi = hi * 60 + mi
hf = hf * 60 + mf
md = hf - hi
hd = 0


if hf == hi and mf == mi :
    hd = 24

while md > 60 :
    md = md - 60
    hd = hd + 1

print('O JOGO DUROU %.0f HORA(S) E %.0f MINUTO(S)' % (hd,md))
'''

'''
Tentativa 2

from datetime import timedelta

linha = input().split(' ')
linha = list(map(int,linha))
hi,mi,hf,mf = linha
md = 0
hd = 24
if (hf != hi) and (mf != mi)  :
    hmi = timedelta(hours=hi, minutes=mi)
    hmf = timedelta(hours=hf, minutes=mf)
    diferenca = hmf - hmi
    diferencaseparada = str(diferenca).split(':')
    diferencatratada = list(map(int,diferencaseparada))
    hd,md,sd = diferencatratada

print('O JOGO DUROU %.0f HORA(S) E %.0f MINUTO(S)' % (hd,md))

'''
'''
linha = input().split(' ')
linha = list(map(int,linha))
HI,MI,HF,MF = linha

MIT = HI * 60 + MI
MFT = HF * 60 + MF
HT = 24
MT = 0
if HI != HF and MI != MF :
    MIFT = MFT - MIT
    MT = int(MIFT % 60)
    HT = int((MIFT - MT) / 60)
    print('O JOGO DUROU %d HORA(S) E %d MINUTO(S)' % (HT,MT))
else:
    print('O JOGO DUROU %d HORA(S) E 0 MINUTO(S)')
'''
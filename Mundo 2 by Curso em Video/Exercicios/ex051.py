# leia o primeiro termo e a razão de uma progressão aritmetica, no final mostre os 10 primeiros termos

pt = int(input('Digite o Primeiro termo da PA:'))
ra = int(input('Digite a Razão da PA:'))
c = 0
ct = ((pt+1)*(ra+1)*100)

if pt < 0 and ra > 0:
    ra = ra *-1
if ct == 0:
    ct = 100*-1
for x in range(pt,ct,ra):
    if c < 10:
        print(x)
    c += 1

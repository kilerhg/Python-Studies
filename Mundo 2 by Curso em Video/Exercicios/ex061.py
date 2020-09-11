# Leia o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos usando while

pt = int(input('Digite um Valor Inteiro para o primeiro Termo:'))
ra = int(input('Digite um Valor Inteiro para a Razão:'))
nt = 1
rt = pt
while nt != 11:
    print(f' O {nt:2} Termo é: {rt:3}  !!!')
    rt += ra
    nt += 1

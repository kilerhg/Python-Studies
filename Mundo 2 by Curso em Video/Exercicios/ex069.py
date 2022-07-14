# leia a idade e o sexo de varias pessoas, a cada pessoa cadastrada o programa pergunta se quer continuar ou não, no final mostre:
# quantas pessoas tem mais de 18 anos, quantos homens foram cadastrados, quantas mulheres tem menos de 20 anos.
cont18 = contm = conth = 0
while True:
    print('= ='*20)
    id = int(input('Digite a idade:'))
    sx = str(input('Digite seu Sexo [F/M]:')).strip().upper()[0]
    while sx not in 'FM':
        sx = str(input('Digite seu Sexo [F/M]:')).strip().upper()[0]
    if id > 18:
        cont18 += 1
    if id < 20 and sx == 'F':
        contm += 1
    if sx == 'M':
        conth += 1
    flag = str(input('Quer Continuar [S/N]:')).strip().upper()[0]
    while flag not in 'SN':
        flag = str(input('Quer Continuar [S/N]:')).strip().upper()[0]
    if flag == 'S':
        pass
    elif flag == 'N':
        break
print(f'{cont18} Tem mais de 18 anos\n{conth} Homen(s) foram cadastrados\n{contm} Mulher(es) tem menos de 20 anos. ')
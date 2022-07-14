# o nome e preço de varios produtos, perguntar se quer ou nao continuar, no final mostre: total gasto na compra, quantos produtos custam mais de 1000, nome do produto mais barato.
contb = contm = ctt = 0
while True:
    np = str(input('Digite o nome do produto:')).strip().capitalize()
    vp = int(input('Digite o valor do produto:'))
    ctt += vp
    if vp > 1000:
        contm += 1
    if contb == 0:
        npb = np
        vpb = vp
    contb += 1
    if vp < vpb and contb != 0:
        npb = np
        vpb = vp
    flag = str(input('Deseja continuar? [S/N]:')).strip().upper()[0]
    while flag not in 'SN':
        flag = str(input('Deseja continuar? [S/N]:')).strip().upper()[0]
    if flag == 'N':
        break

print(f'Na compra foi gasto R${ctt:.2f}\nCom {contm} Produtos custando mais de R$1.000,00\nO Produto mais barato comprado Foi : {npb}, Custando R${vpb:.2f}')
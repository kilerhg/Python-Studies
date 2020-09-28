# tenha um tupla unica com nomes de produtos e seus preços na sequencia, no final mostre uma listagem de preços organizando de forma tabular

produtos = ('Caneta',5.9,'Caderno',12,'Lapis',1,'Apostila',20,'Lapiseira',9,'Quadro',25,'Porta Retrato',30)
print(f'Produto{" "*16}Valor')
for x in range(0,int(len(produtos)),2):
    print(f"{produtos[x]:.<20} R${produtos[x+1]:>6.2f}")

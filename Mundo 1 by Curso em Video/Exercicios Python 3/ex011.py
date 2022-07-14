# leia largura e altura e verifique quanto de tinta precisa para pintar a parece considerando 1 litro de tinta pinta 2m2

altura = float(input('Digite a altura da parede:'))
largura = float(input('Digite a largura da parede:'))

print('você ira precisar de {:.1f} litros de tinta'.format((altura*largura)/2))


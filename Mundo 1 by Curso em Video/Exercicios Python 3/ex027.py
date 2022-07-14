# leia um nome completo e mostre o primeiro e ultimo nome
nome = str(input('Digite seu nome completo:')).strip()
linha = nome.split()
print(f' Primero Nome: {linha[0]}\n Segundo Nome: {linha[len(linha)-1]}')
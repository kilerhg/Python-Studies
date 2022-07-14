# leia um nome completo e mostre : letra maiusculas, letras miusculas, quantas letras sem espaços, letras tem o primero nome.
nome = input('Digite seu nome completo:')
print(f' O seu nome completo em maiusculo é : {nome.upper()}')
print(f' O seu nome completo em minusculo é : {nome.lower()}')
print(f' O seu nome tem {len(nome.replace(" ",""))} letras sem espaços')
linha = nome.split()
print(f' O seu nome tem {len(linha[0])} Letras no primeiro nome')

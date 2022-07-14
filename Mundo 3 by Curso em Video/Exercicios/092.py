# leia o ano de nascimento e carteira de trabalho e armazene todos e idade em um dicionario
# se por acabo a ctps for diferente de zero tambem recebera o ano de contratação e o salario,
# calcule e acrescente alem da idade, com quantos anos a pessoa vai se aposentar sendo 35 anos de contribuição para se aposentar

from datetime import datetime
anoa = datetime.today().year


pessoa = {}
pessoa['nome'] = str(input('Digite seu nome:')).strip().capitalize()
anon = int(input('Digite o ano de nascimento:'))
pessoa['idade'] = anoa - anon
pessoa['ctps'] = int(input('Digite a sua carteira de trabalho (0 caso não tenha):'))

if pessoa['ctps'] != 0:
    anoc = int(input('Digite o ano de contratação:'))
    pessoa['Tempo Servico'] = anoa - anoc
    pessoa['Salario'] = float(input('Digite seu Salario:'))
    pessoa['idade Aposentar'] = pessoa['idade'] + (35 - pessoa['Tempo Servico'])
print(f'{"Perfil Pessoal":-^35}')
for k,v in pessoa.items():
    print(f'{k.capitalize(): >15} : {v: <3}')



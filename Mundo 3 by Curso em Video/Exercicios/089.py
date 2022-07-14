# leia nome e duas notas de varios alunos e guardar tudo em uma lista composta com nomes e uma lista notas dentro de cada estudante contendo a nota 1 e 2,
# no final mostre um boletim contendo a media de cada um, e permita que o usuario possa mostrar as notas de cada aluno individualmente

lista = list()
aluno = list()
notas = list()
while True:
    aluno.append(str(input('Digite seu nome:')))
    notas.append(float(input('Digite a Nota 1:')))
    notas.append(float(input('Digite a Nota 2:')))
    aluno.append(notas[:])
    lista.append(aluno[:])
    notas.clear()
    aluno.clear()
    flag = str(input('Você deseja continuar? [S/N]: ')).strip().upper()[0]
    if flag in 'N':
        break
print(f'{"BOLETIM ESCOLAR":-^32}')
print(f'Numero{" "*5}Nome{" "*10}Media')
flag = 0
for pos, x in enumerate(lista):
    print(f'{" "*2}{pos+1}{" "*8}{lista[pos][0]: <10}{" "*5}{(lista[pos][1][0] + lista[pos][1][1])/2:.1f}')
while True:
    flag = int(input('Digite o Numero do aluno [999 para sair]:'))
    if flag == 999:
        break
    print(f'As notas de {lista[flag-1][0]} são : {lista[flag-1][1]}')
print('Obrigado, Volte sempre')


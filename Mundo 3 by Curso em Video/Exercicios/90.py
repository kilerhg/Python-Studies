# leia o nome e media de um aluno, guardando tambem a situação em um dicionario, no final mostrar o conteudo da estrutura na tela.
aluno = {}
aluno['Nome'] = str(input('Digite seu Nome:'))
aluno['Media'] = float(input('Digite A Media:'))
if aluno['Media'] < 5:
    aluno['situacao'] = 'Reprovado'
elif 5 <= aluno['Media'] < 7:
    aluno['situacao'] = 'Recuperação'
elif 7 < aluno['Media']:
    aluno['situacao'] = 'Aprovado'
print(f'Aluno: {aluno["Nome"]}\nSituação: {aluno["situacao"]}')

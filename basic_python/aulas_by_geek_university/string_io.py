'''
StringIO


OBS: para ler ou escrever no os, precisa de permissão para tal


StringIO -> Utilizado para ler e criar arquivos em memória
'''


from io import StringIO

text = 'normal text'


file = StringIO(text)

print(file.read())

file.write('teste')



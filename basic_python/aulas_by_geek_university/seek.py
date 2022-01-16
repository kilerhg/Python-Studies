'''
Seek e cursores


seek() -> é utilizada para manipular o ponteiro de leitura/escrita

'''


value = open('./texto.txt', 'r')


print(value.read())
value.seek(0)
print(value.read())

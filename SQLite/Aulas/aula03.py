import sqlite3

try:
    banco = sqlite3.connect('primeiro_banco.db')

    cursor = banco.cursor()

    cursor.execute("DELETE from pessoas WHERE idade = as")

    banco.commit()
    banco.close()
    print('Dados Removidos com Sucesso')
except sqlite3.Error as erro:
    print(f'Erro ao Remover Dados, Nome : {erro}')

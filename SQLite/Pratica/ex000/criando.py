import sqlite3

nome = 'Felipe'
nascimento = '2010'
email = f'{nome}@gmail.com'


banco = sqlite3.connect('primeiro_banco.db')

cursor = banco.cursor()

# cursor.execute("""CREATE TABLE pessoas (
#     id integer PRIMARY KEY AUTOINCREMENT,
#     nome text,
#     ano_nascimento integer,
#     email text)""")

#cursor.execute(f"INSERT INTO pessoas VALUES (NULL,'{nome}','{nascimento}','{email}')")

# cursor.execute(f'DELETE from pessoas where nome = "Roberto"')

# cursor.execute(f'DELETE from pessoas where nome = "Carlos"')


banco.commit()

pesquisa_nome = 'Roberta'
cursor.execute(f"SELECT ano_nascimento FROM pessoas WHERE nome = '{pesquisa_nome}'")
variavel = cursor.fetchall()
print(variavel[0][0])
import sqlite3

banco = sqlite3.connect('banco_dados.db')

cursor = banco.cursor()

login = input('Digite Um Nome de Login:')
senha = input('Digite uma senha:')

cursor.execute(f"INSERT INTO conta VALUES (NULL,'{login}','{senha}')")

# cursor.execute(f'DELETE from pessoas where nome = "Roberto"')

# cursor.execute(f'DELETE from pessoas where nome = "Carlos"')


banco.commit()
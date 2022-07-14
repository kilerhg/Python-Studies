import sqlite3

nome = 'Roberto'
nascimento = '2001'
email = 'roberto@gmail.com'


banco = sqlite3.connect('primeiro_banco.db')

cursor = banco.cursor()

cursor.execute(f"INSERT INTO pessoas VALUES (NULL,'{nome}','{nascimento}','{email}')")

banco.commit()


cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())
import sqlite3

banco = sqlite3.connect('primeiro_banco.db')

cursor = banco.cursor()

#cursor.execute("CREATE TABLE pessoazinhas (ID integer PRIMARY KEY AUTOINCREMENT,nome text, idade integer, email text)")

cursor.execute("INSERT INTO pessoazinhas VALUES (NULL,'Joao',20,'joao_123@gmail.com')")

banco.commit()


cursor.execute("SELECT * FROM pessoazinhas")
print(cursor.fetchall())
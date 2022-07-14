import sqlite3

nome = 'Lucas'
idade = '18'
email = 'lucasgmail.com'


banco = sqlite3.connect('primeiro_banco.db')

cursor = banco.cursor()

cursor.execute(f"INSERT INTO pessoas VALUES ('{nome}','{idade}','{email}')")

banco.commit()


cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())
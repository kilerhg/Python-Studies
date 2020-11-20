import sqlite3

nome = 'Lucas'
idade = '18'
email = 'lucasgmail.com'


banco = sqlite3.connect('primeiro_banco.db')

cursor = banco.cursor()

cursor.execute(f"UPDATE pessoas SET nome = 'Fabio' WHERE idade = 40")

banco.commit()
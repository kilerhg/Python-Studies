import sqlite3

banco = sqlite3.connect('banco_dados.db')

cursor = banco.cursor()

cursor.execute("""CREATE TABLE conta (
id integer PRIMARY KEY AUTOINCREMENT,
login text,
    senha text)""")
banco.commit()


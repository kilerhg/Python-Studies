import sqlite3

banco = sqlite3.connect('banco_dados.db')
cursor = banco.cursor()

cursor.execute(f"INSERT INTO conta VALUES (NULL,'{login}','{senha}')")
banco.commit()
banco.close()

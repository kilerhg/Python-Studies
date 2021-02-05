import sqlite3


banco = sqlite3.connect('banco_dados.db')
cursor = banco.cursor()


for x in range(11,20):

    cursor.execute(f'SELECT data FROM transferecias WHERE id = {x}')
    resultado = cursor.fetchall()[0][0][:-5]
    banco.commit()

    cursor.execute(f"UPDATE transferecias SET data = '{resultado}' WHERE id = '{x}'")
    banco.commit()
banco.close()


import sqlite3

banco = sqlite3.connect('banco_dados.db')

cursor = banco.cursor()


login = input('Digite Um Nome de Login:')
senha = input('Digite uma senha:')

try:
    cursor.execute(f"SELECT * from conta WHERE login = '{login}' AND senha = '{senha}'")
except sqlite3.Error as erro:
    print(f'Digite a senha ou login Corretamente {erro}')

banco.commit()
resultado = cursor.fetchall()
if len(resultado) != 0:
    print(f'Olá {login}, Bem Vindo')
else:
    print('Digite a senha ou login corretamente')
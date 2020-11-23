from interface import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QClipboard
from PyQt5.QtWidgets import QApplication, QMessageBox
import sqlite3

def main(ui):

    try:
        banco = sqlite3.connect('banco_dados.db')
        cursor = banco.cursor()
        cursor.execute("""CREATE TABLE conta (
        id integer PRIMARY KEY AUTOINCREMENT,
        login text,
        senha text)""")
        banco.commit()
        banco.close()
    except:
        pass

    def limpar_campos_login():
        ui.txt_usuario.setText('')
        ui.txt_senha.setText('')

    def limpar_campos_cadastrar():
        ui.txt_cadastrar_usuario.setText('')
        ui.txt_cadastrar_senha.setText('')

    def mostrar_msg(titulo,texto):
        titulo = str(titulo)
        texto = str(texto)
        win = MainWindow
        msg = QMessageBox(win)
        msg.setWindowTitle(f"{titulo}")
        msg.setText(f"{texto}")
        x = msg.exec_()

    def func_login(self):
        usuario = ui.txt_usuario.text()
        senha = ui.txt_senha.text()

        banco = sqlite3.connect('banco_dados.db')
        cursor = banco.cursor()
        try:
            cursor.execute(f"SELECT * from conta WHERE login = '{usuario}' AND senha = '{senha}'")
        except sqlite3.Error as erro:
            mostrar_msg('Login Empresa XYZ',f'Algo deu errado!! Digite a senha ou usuario Corretamente: {erro}')
            # print(f'{erro}')
        banco.commit()
        resultado = cursor.fetchall()
        limpar_campos_login()
        if len(resultado) != 0:
           mostrar_msg('Login Empresa XYZ',f'Olá {usuario}, Bem Vindo')
           #  print(f'Olá {usuario}, Bem Vindo')
        else:
            mostrar_msg('Login Empresa XYZ','Algo deu errado!! Digite a senha ou usuario Corretamente')
            # print('Algo deu errado!! Digite a senha ou usuario Corretamente')
        banco.close()

    def func_cadastrar():
        usuario_cadastrar = str(ui.txt_cadastrar_usuario.text()).strip()
        senha_cadastrar = str(ui.txt_cadastrar_senha.text()).strip()

        banco = sqlite3.connect('banco_dados.db')
        cursor = banco.cursor()
        cursor.execute(f"SELECT * from conta WHERE login = '{usuario_cadastrar}'")
        resultado = cursor.fetchall()
        if len(resultado) != 0:
            mostrar_msg('Cadastro Empresa XYZ','Usuario Já Cadastrado')
            print(resultado)
        elif not usuario_cadastrar.islower():
            mostrar_msg('Cadastro Empresa XYZ','Digite Apenas Letras Minusculas no Usuario')
        else:
            try:
                cursor.execute(f"INSERT INTO conta VALUES (NULL,'{usuario_cadastrar.lower()}','{senha_cadastrar}')")
                banco.commit()
                print('Dados Cadastrados Com Sucesso!!!')
            except sqlite3.Error as erro:
                print(f'Erro ao cadastrar: {erro}')
        banco.close()
        limpar_campos_cadastrar()

    ui.btn_enviar.clicked.connect(func_login)
    ui.btn_enviar_4.clicked.connect(func_cadastrar)
    ui.txt_senha.setEchoMode(QtWidgets.QLineEdit.Password)
    ui.txt_cadastrar_senha.setEchoMode(QtWidgets.QLineEdit.Password)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    main(ui)
    sys.exit(app.exec_())
from interface import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QClipboard
from PyQt5.QtWidgets import QApplication, QMessageBox
import sys
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

    def nivel_acesso(usuario):
        usuario = str(usuario)
        if usuario == 'adm':
            nivel = 2
        elif usuario == 'visitante':
            nivel = 0
        else:
            nivel = 1
        return nivel
    def limpar_campos_login():
        ui.txt_usuario.setText('')
        ui.txt_senha.setText('')

    def limpar_campos_cadastrar():
        ui.txt_cadastrar_usuario.setText('')
        ui.txt_cadastrar_senha.setText('')

    def limpar_campos_novasenha():
        ui.txt_novasenha_usuario.setText('')
        ui.txt_novasenha_senha.setText('')

    def limpar_campos_removerconta():
        ui.txt_removerconta_usuario.setText('')

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
           ui.frame.lower()
           ui.frame_3.lower()
           ui.frame_4.lower()
           ui.lb_nomeusuario.setText(f'{usuario}')
           acesso = nivel_acesso(usuario)
           ui.lb_nivel_acesso.setText(f'{acesso}')
           if acesso == 0:
               ui.formFrame_4.enabled = False
               ui.formFrame_4.hide()
               ui.lb_nomeusuario_2.hide()
               ui.btn_enviar_removerconta.enabled = False
               ui.btn_enviar_removerconta.hide()
           elif acesso == 1:
               ui.formFrame_4.enabled = False
               ui.formFrame_4.hide()
               ui.lb_nomeusuario_2.hide()
               ui.btn_enviar_removerconta.enabled = False
               ui.btn_enviar_removerconta.hide()
           else:
               ui.formFrame_4.enabled = True
               ui.formFrame_4.show()
               ui.lb_nomeusuario_2.show()
               ui.btn_enviar_removerconta.enabled = True
               ui.btn_enviar_removerconta.show()

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

    def func_novasenha():

        usuario_novasenha = str(ui.txt_novasenha_usuario.text()).strip()
        senha_novasenha = str(ui.txt_novasenha_senha.text()).strip()

        banco = sqlite3.connect('banco_dados.db')
        cursor = banco.cursor()

        try:
            cursor.execute(f"SELECT * FROM conta WHERE login = '{usuario_novasenha}'")
            resultado = cursor.fetchall()
            banco.commit()
            if len(resultado) != 0:
                cursor.execute(f"UPDATE conta SET senha = '{senha_novasenha}' WHERE login = '{usuario_novasenha}'")
                banco.commit()
                mostrar_msg('Redefinição de Senha Empresa XYZ','Senha redefinida com sucesso')
            else:
                mostrar_msg('Redefinição de Senha Empresa XYZ','Usuario Não Encontrado no banco de dados')
        except sqlite3.Error as erro:
            print(f'Algo deu errado!! Erro de nome : {erro}')
        banco.close()
        limpar_campos_novasenha()

    def func_remover_conta():
        #     cursor.execute("DELETE from pessoas WHERE idade = as")
        usuario_remover = str(ui.txt_removerconta_usuario.text()).strip()

        banco = sqlite3.connect('banco_dados.db')
        cursor = banco.cursor()
        try:
            cursor.execute(f"SELECT * from conta WHERE login = '{usuario_remover}'")
            resultado = cursor.fetchall()
            banco.commit()
            if len(resultado) != 0:
                if usuario_remover != 'adm':
                    cursor.execute(f"DELETE from conta WHERE login = '{usuario_remover}'")
                    banco.commit()
                    mostrar_msg('Removendo Contas Empresa XYZ',f'Conta {usuario_remover} Removida Com Sucesso!!!')
                else:
                    mostrar_msg('Removendo Contas Empresa XYZ','Você Não Pode Remover a Conta de Administrador')
            else:
                mostrar_msg('Removendo Contas Empresa XYZ','Usuario Não Encontrado em Nossa base de dados')
        except sqlite3.Error as erro:
            mostrar_msg('Removendo Contas Empresa XYZ',f'Algo deu errado!! Erro de nome : {erro}')
        banco.close()
        limpar_campos_removerconta()
    ui.btn_enviar.clicked.connect(func_login)
    ui.btn_enviar_4.clicked.connect(func_cadastrar)
    ui.btn_enviar_novasenha.clicked.connect(func_novasenha)
    ui.btn_enviar_removerconta.clicked.connect(func_remover_conta)
    ui.txt_senha.setEchoMode(QtWidgets.QLineEdit.Password)
    ui.txt_cadastrar_senha.setEchoMode(QtWidgets.QLineEdit.Password)
    ui.txt_novasenha_senha.setEchoMode(QtWidgets.QLineEdit.Password)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    main(ui)
    sys.exit(app.exec_())
from interface import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QClipboard
from PyQt5.QtWidgets import QApplication, QMessageBox
import sys
import sqlite3
from PyQt5.QtGui import *
from datetime import datetime


def main(ui):
    try:
        banco = sqlite3.connect('banco_dados.db')
        cursor = banco.cursor()
        cursor.execute("""CREATE TABLE produto (
        id integer PRIMARY KEY AUTOINCREMENT,
        nome_produto text,
        marca text,
        descricao text,
        custo REAL,
        codigo integer,
        fornecedor text,
        preco REAL,
        data text)""")
        banco.commit()
        banco.close()
    except:
        pass

    def func_enviar():
        nome_produto = str(ui.txt_produto.text()).strip()
        marca = str(ui.txt_marca.text()).strip()
        descricao = str(ui.txt_descricao.text()).strip()
        custo = str(ui.txt_custo.text()).strip()
        codigo = str(ui.txt_codigo.text()).strip()
        fornecedor = str(ui.txt_fornecedor.text()).strip()
        preco = str(ui.txt_preco.text()).strip()

        try:
            # hoje = str(datetime.today().time()).replace(":","-")
            data = str(datetime.today())
            data = str(data[:-7])
            # data = "A"
            print(data)
            banco = sqlite3.connect('banco_dados.db')
            cursor = banco.cursor()
            cursor.execute(f"""INSERT INTO produto values (NULL,'{nome_produto}','{marca}','{descricao}','{custo}','{codigo}','{fornecedor}','{preco}','{data}')""")
            # cursor.execute(f"""INSERT INTO produto values ('','{nome_produto}','{marca}','{descricao}','{custo}','{codigo}','{fornecedor}','{preco}')""")
            banco.commit()
        except sqlite3.Error as erro:
            print(f'Erro de nome {erro}')
        banco.close()
        func_limpar_campos()


    def func_pesquisar():

        codigo_pesquisar = ui.txt_pesquisar.text()
        try:
            banco = sqlite3.connect('banco_dados.db')
            cursor = banco.cursor()
            cursor.execute(f"""SELECT * from produto WHERE codigo = '{codigo_pesquisar}'""")
            # cursor.execute(f"""INSERT INTO produto values ('','{nome_produto}','{marca}','{descricao}','{custo}','{codigo}','{fornecedor}','{preco}')""")
            banco.commit()
            resultado = cursor.fetchall()
            if len(resultado) != 0:
                resultado = resultado[0][1:]
                func_limpar_campos()
                ui.txt_produto.setText(f'{resultado[0]}')
                ui.txt_marca.setText(f'{resultado[1]}')
                ui.txt_descricao.setText(f'{resultado[2]}')
                ui.txt_custo.setText(f'{resultado[3]}')
                ui.txt_codigo.setText(f'{resultado[4]}')
                ui.txt_fornecedor.setText(f'{resultado[5]}')
                ui.txt_preco.setText(f'{resultado[6]}')
            else:
                print('Erro de Busca')
        except sqlite3.Error as erro:
            print(f'Erro de nome {erro}')
        banco.close()


        # print(f'produto: {nome_produto}')
        # print(f'marca: {marca}')
        # print(f'descricao: {descricao}')
        # print(f'custo: {custo}')
        # print(f'codigo: {codigo}')
        # print(f'fornecedor: {fornecedor}')
        # print(f'preco: {preco}')


    def func_limpar_campos():
        
        ui.txt_produto.setText('')
        ui.txt_marca.setText('')
        ui.txt_descricao.setText('')
        ui.txt_custo.setText('')
        ui.txt_codigo.setText('')
        ui.txt_fornecedor.setText('')
        ui.txt_preco.setText('')


    ui.btn_pesquisar.clicked.connect(func_pesquisar)
    ui.btn_enviar.clicked.connect(func_enviar)
    ui.txt_custo.setValidator(QDoubleValidator(0.99, 99.99, 2))
    # ui.txt_codigo.setValidator(QDoubleValidator(000, 999, 2))
    ui.txt_codigo.setInputMask("0000")
    # ui.txt_codigo.setText('')
    # ui.txt_preco.setInputMask("0000")
    ui.txt_preco.setValidator(QDoubleValidator(0.99, 99.99, 2))
    # ui.txt_preco.setInputMask("0000")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    main(ui)
    sys.exit(app.exec_())
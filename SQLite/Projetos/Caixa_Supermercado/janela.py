from interface import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QClipboard
from PyQt5.QtWidgets import QApplication, QMessageBox
import sys
import sqlite3
from PyQt5.QtGui import *
from datetime import datetime


def main(ui):
    produtos = ['000001', 'PIPOCA', '2.59', '000002', 'MANTEIGA', '4.20']


    def definir_preco_total(preco,quantidade,opcao=0):
        if opcao == 1:
            pass
        else:
            preco = float(preco)
            quantidade = int(quantidade)
            valor_adicionar = preco * quantidade
            valor_atual = ui.txt_preco.text()
            if len(valor_atual) == 0:
                valor_atual = 0
            else:
                valor_atual = float(valor_atual)
            ui.txt_preco.setText(str(valor_atual+valor_adicionar))
    def procurar():
        global codigo,produto,preco
        try:
            pesquisar = str(ui.txt_codigo.text()).strip()
            if len(pesquisar) != 0:
                if len(str(pesquisar)) < 6:
                    pesquisar = ('0' * (6 - len(str(pesquisar)))) + str(pesquisar)
                codigo_indice = produtos.index(f'{pesquisar}')
                codigo = produtos[codigo_indice]
                produto = produtos[codigo_indice + 1]
                # quantidade = produtos[codigo_indice + 2]
                preco = produtos[codigo_indice + 2]
                ui.txt_codigo_produto.setText(f'{codigo}')
                ui.txt_produto.setText(f'{produto}')
                ui.txt_preco_unitario.setText(f'{preco}')
            else:
                print('teste')
        except:
            print('erro')
    def adicionar_linha_nota(codigo_produto,produto,quantidade,preco):
        ui.txt_nota.append(f'{codigo_produto:0<6} {"":-<4} {produto: <10} {"":-<4} {quantidade:0>3} {"-" * 3} {preco: >7}')

    def adicionar_nota():
        #
        #   VERSÃO 00
        # if len(pesquisar) != 0:
        #     for x in range(1, (len(produtos) // 4) + 1):
        #         if len(str(x)) < 6:
        #             pesquisar = ('0' * (6 - len(str(x)))) + str(x)
        #         codigo_indice = produtos.index(f'{pesquisar}')
        #         codigo = produtos[codigo_indice]
        #         produto = produtos[codigo_indice + 1]
        #         quantidade = produtos[codigo_indice + 2]
        #         preco = produtos[codigo_indice + 3]
        #         adicionar_linha_nota(codigo,produto,quantidade,preco)
        global codigo, produto, preco, lista_nota


        quantidade = str(ui.txt_quantidade.text()).strip()
        try:
            adicionar_linha_nota(codigo,produto,quantidade,preco)
            definir_preco_total(preco,quantidade)
        except:
            print('erro')


    ui.btn_adicionar_produto.clicked.connect(adicionar_nota)
    ui.btn_procurar.clicked.connect(procurar)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    main(ui)
    sys.exit(app.exec_())
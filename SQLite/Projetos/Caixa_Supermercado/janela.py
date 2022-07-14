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
        # Criando Banco de dados e Tabelas
        banco = sqlite3.connect('banco_dados.db')
        cursor = banco.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS produtos (
        id integer PRIMARY KEY AUTOINCREMENT,
        codigo integer,
        produto text,
        preco REAL)""")
        banco.commit()
        cursor.execute("""CREATE TABLE IF NOT EXISTS notas (
        id integer PRIMARY KEY AUTOINCREMENT,
        caixa integer,
        nota text,
        valor real,
        data text)""")
        banco.commit()
        cursor.execute("""CREATE TABLE IF NOT EXISTS gestao (
        id integer PRIMARY KEY AUTOINCREMENT,
        caixa integer,
        codigo integer,
        quantidade integer,
        data text)""")
        banco.commit()
        banco.close()
    except sqlite3.Error as erro:
        print(f'Erro de nome: {erro}')

    def data_agora():
        data = str(datetime.today())
        data = str(data[:-7])
        data.replace(' ','-')
        return data

    def mostrar_msg(titulo, texto):
        titulo = str(titulo)
        texto = str(texto)
        win = MainWindow
        msg = QMessageBox(win)
        msg.setWindowTitle(f"{titulo}")
        msg.setText(f"{texto}")
        x = msg.exec_()

    def definir_metodo_pagamento():
        if ui.rd_cartao.isChecked() == False and ui.rd_dinheiro.isChecked() == False:
            retorno = 'nao selecionado'
        elif ui.rd_dinheiro.isChecked():
            retorno = 'DINHEIRO'
        else:
            retorno = 'CARTAO'
        return retorno

    def enviar_banco_notas():
        caixa = ui.lb_caixa.text()
        nota = ui.txt_nota.toPlainText()
        valor = ui.txt_preco.text()
        banco = sqlite3.connect('banco_dados.db')
        data = str(data_agora())
        cursor = banco.cursor()
        # cursor.execute(f"INSERT INTO notas values (NULL,'{caixa}','{nota}','{valor},'{data}')")
        cursor.execute(f"INSERT INTO notas values (NULL,'{caixa}','{nota}','{valor}','{data}')")
        banco.commit()

    def enviar_banco_gestao():
        global lista_compra
        caixa = ui.lb_caixa.text()
        banco = sqlite3.connect('banco_dados.db')
        data = str(data_agora())
        cursor = banco.cursor()
        for x in range(0,len(lista_compra)//2):
            print(lista_compra)
            print(x)
            codigo = lista_compra[x]
            quantidade = lista_compra[x+1]
            cursor.execute(f"INSERT INTO gestao values (NULL,'{caixa}','{codigo}','{quantidade}','{data}')")
            banco.commit()
        banco.close()
        lista_compra.clear()

    def definir_troco():
        total_compra = float(ui.txt_preco.text())
        dinheiro_recebido = float(ui.txt_dinheiro_recebido.text())
        troco = dinheiro_recebido - total_compra
        ui.txt_troco.setText(f'{troco:.2f}')

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
            calculo = valor_atual+valor_adicionar
            ui.txt_preco.setText(f'{calculo:.2f}')

    def procurar():
        global codigo,produto,preco
        try:
            pesquisar = str(ui.txt_codigo.text()).strip()
            if len(pesquisar) != 0:
                if len(str(pesquisar)) < 6:
                    pesquisar = ('0' * (6 - len(str(pesquisar)))) + str(pesquisar)

                banco = sqlite3.connect('banco_dados.db')
                cursor = banco.cursor()
                cursor.execute(f"""SELECT codigo,produto,preco from produtos WHERE codigo == '{pesquisar}'""")
                produtos = cursor.fetchall()
                if len(produtos) != 0:
                    produtos = produtos[0]
                    banco.commit()
                    codigo = produtos[0]
                    produto = produtos[1]
                    preco = produtos[2]
                    ui.txt_codigo_produto.setText(f'{codigo}')
                    ui.txt_produto.setText(f'{produto}')
                    ui.txt_preco_unitario.setText(f'{preco}')
                    banco.close()
                else:
                    mostrar_msg('Caixa EMPRESA XYZ','Digite o codigo do produto')
            else:
                mostrar_msg('Caixa EMPRESA XYZ','Digite o codigo do produto')
        except ValueError as erro:
            mostrar_msg('Caixa EMPRESA XYZ',f'Erro nome: {erro}')
        ui.txt_troco.setText('')

    def adicionar_linha_nota(codigo_produto,produto,quantidade,preco):
        ui.txt_nota.append(f'{codigo_produto:0<6} {"":-<4} {produto: <10} {"":-<4} {quantidade:0>3} {"-" * 4} {preco: >5}')

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
        global codigo, produto, preco, lista_nota, lista_compra
        quantidade = str(ui.txt_quantidade.text()).strip()
        try:
            print(lista_compra)
        except:
            lista_compra = []
        if len(ui.txt_codigo_produto.text()) != 0:
            try:
                lista_compra.append(f'{codigo}')
                lista_compra.append(f'{quantidade}')
                print(lista_compra)
                adicionar_linha_nota(codigo,produto,quantidade,preco)
                definir_preco_total(preco,quantidade)
            except ValueError as erro:
                mostrar_msg('Caixa EMPRESA XYZ',f'Erro nome: {erro}')
        else:
            mostrar_msg('Caixa EMPRESA XYZ','Digite um produto antes de inserir')

    def limpar_campos():
        ui.txt_preco.clear()
        ui.txt_codigo_produto.clear()
        ui.txt_produto.clear()
        ui.txt_preco_unitario.clear()
        ui.txt_quantidade.clear()
        ui.txt_codigo.clear()
        ui.txt_remover_produto.clear()
        ui.txt_dinheiro_recebido.clear()
        ui.txt_nota.clear()

    def enviar_dados():
            if ui.rd_dinheiro.isChecked():
                definir_troco()
                dinheiro_recebido = float(ui.txt_dinheiro_recebido.text())
                troco = float(ui.txt_troco.text())
            else:
                dinheiro_recebido = 0
                troco = 0
            valor_total = float(ui.txt_preco.text())
            nota = ui.txt_nota.toPlainText()
            ui.txt_nota.clear()
            ui.txt_nota.append('')
            ui.txt_nota.append('/' * 54)
            ui.txt_nota.append('')
            ui.txt_nota.append('CODIGO ---- NOME PRODU ---- QTD ----  PRECO')
            ui.txt_nota.append(nota)
            ui.txt_nota.append('')
            ui.txt_nota.append('')
            ui.txt_nota.append('-'*54)
            ui.txt_nota.append('')
            ui.txt_nota.append(f'Total: {valor_total:<5.2f} ---- Dinheiro: {dinheiro_recebido:<5.2f} ')
            ui.txt_nota.append(f'Metodo de Pagamento: {definir_metodo_pagamento()}')
            ui.txt_nota.append(f'Troco: {troco:<5.2f}')
            ui.txt_nota.append(f'Data e hora: {data_agora()}')
            ui.txt_nota.append('')
            ui.txt_nota.append('/'*54)



    def verificar_campos():
        botao_cartao = ui.rd_cartao.isChecked()
        botao_dinheiro = ui.rd_dinheiro.isChecked()
        valor_retorno = 1
        if len(ui.txt_nota.toPlainText()) == 0:
            mostrar_msg('CAIXA EMPRESA XYZ','Entre ao Menos Um Item')
            valor_retorno = 0
        if botao_cartao == False and botao_dinheiro == False:
            mostrar_msg('CAIXA EMPRESA XYZ','Selecione o Tipo de Pagamento')
            valor_retorno = 0
        elif ui.rd_dinheiro.isChecked() == True and len(ui.txt_dinheiro_recebido.text()) == 0:
            mostrar_msg('CAIXA EMPRESA XYZ','Digite o Valor Recebido')
            valor_retorno = 0
        if len(ui.txt_dinheiro_recebido.text()) != 0 and len(ui.txt_preco.text()) != 0:
            recebido = float(ui.txt_dinheiro_recebido.text())
            total = float(ui.txt_preco.text())
            troco = recebido - total
            if troco < 0:
                mostrar_msg('CAIXA EMPRESA XYZ', 'O valor Recebido Não pode ser menor que o Valor total')
                valor_retorno = 0
        return valor_retorno



    def finalizar_compra():
        verificar = verificar_campos()
        if verificar == 1:
            # print('a')
            enviar_dados()
            enviar_banco_notas()
            enviar_banco_gestao()
            limpar_campos()

    lista_compra = ['1']
    ui.lb_caixa.setText('01')
    ui.btn_adicionar_produto.clicked.connect(adicionar_nota)
    ui.btn_procurar.clicked.connect(procurar)
    ui.btn_finalizar_compra.clicked.connect(finalizar_compra)
    ui.rd_cartao.clicked.connect(lambda: ui.txt_dinheiro_recebido.setText(''))

#     Mascaras de campos de texto

    # ui.txt_codigo.setValidator(QDoubleValidator(0, 0, 3))
    ui.txt_codigo.setInputMask("0000")
    ui.txt_quantidade.setInputMask("000")

#     Mascaras de campos de texto
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    main(ui)
    sys.exit(app.exec_())
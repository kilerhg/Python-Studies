from interface import *
from funcoes import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QClipboard
from PyQt5.QtWidgets import QApplication


def main(ui):

    def copiar():
        global senha
        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard )
        cb.setText(str(senha), mode=cb.Clipboard)

    ui.ch_especiais.toggle()
    ui.ch_maiusculas.toggle()
    ui.ch_minusculas.toggle()
    ui.ch_numeros.toggle()
    def programa():
        global senha
        especiais = ui.ch_especiais.isChecked()
        maiusculas = ui.ch_maiusculas.isChecked()
        minusculas = ui.ch_minusculas.isChecked()
        numeros = ui.ch_numeros.isChecked()
        caracteres = eval(ui.txt_caracteres.text())
        senha = gerar_senha(caracteres,maiusculas,minusculas,especiais,numeros)
        ui.txt_resultado.setText(senha)
    ui.botao_enviar.clicked.connect(programa)
    ui.botao_copiar.clicked.connect(copiar)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    main(ui)
    sys.exit(app.exec_())
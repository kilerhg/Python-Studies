from interface import *
from PyQt5 import QtWidgets


def main(ui):
    def abrir_texto():
        texto = ui.txt_nome.text()
        local = QtWidgets.QFileDialog.getOpenFileName()[0]
        arquivo = open(str(local), 'r+',encoding='utf-8')
        # conteudo = arquivo.readlines()
        with arquivo as a:
            conteudo = a.readlines()
        conteudo_limpo = []
        for x in conteudo:
            x = x.replace('\n','')
            conteudo_limpo.append(x)
        print(conteudo_limpo)

    def salvar_texto():
        local = QtWidgets.QFileDialog.getSaveFileName()[0]
        arquivo = open(str(local) + '.txt','a+',encoding='utf-8')
        texto = ui.txt_nome.text()
        arquivo.write('\n' + texto)
        print(f'Salvando texto: {texto}\nno local: {local}')

    def receber_nome():
        texto = ui.txt_nome.text()
        print(texto)

    ui.botao_enviar.clicked.connect(receber_nome)
    ui.actionAbrir.triggered.connect(abrir_texto)
    ui.actionSalvar.triggered.connect(salvar_texto)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    main(ui)
    sys.exit(app.exec_())
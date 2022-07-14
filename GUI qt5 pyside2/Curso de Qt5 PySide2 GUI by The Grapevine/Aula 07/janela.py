from interface import *

def main(ui):

    def teste():
        print(ui.texto.text())

    ui.botao.clicked.connect(teste)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    main(ui)
    sys.exit(app.exec_())
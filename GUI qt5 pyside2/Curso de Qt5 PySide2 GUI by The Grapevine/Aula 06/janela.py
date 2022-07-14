from interface import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


def saudacao():
    print('Olá, Mundo')


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # def saudacao():
        #    print('Olá, Mundo')

        self.botao.clicked.connect(saudacao)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
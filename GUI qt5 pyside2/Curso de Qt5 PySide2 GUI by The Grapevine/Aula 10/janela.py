from interface import *

def main(ui):
    from PySide2 import QtCore

    class sinais(QtCore.QObject):
        sinal = QtCore.Signal()

        def __init__(self):
            QtCore.QObject.__init__(self)

    sinal = sinais()

    import threading

    def mudacor():
        import random
        MainWindow.setStyleSheet(f'background-color: #{random.randint(100000, 999999)}')

    sinal.sinal.connect(mudacor)

    def temporizador():
        import time
        while True:
            time.sleep(.1)
            sinal.sinal.emit()
    tarefa = threading.Thread(target=temporizador)
    tarefa.daemon = True
    tarefa.start()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    main(ui)
    sys.exit(app.exec_())
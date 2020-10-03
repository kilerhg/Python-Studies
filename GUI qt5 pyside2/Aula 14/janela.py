from interface import *
import time
import SysTrayIcon


def trayWaiting():

    while SysTrayIcon.SysTrayIcon.WINDOW == True:
        time.sleep(3)
    else:
        SysTrayIcon.SysTrayIcon.WINDOW == True
        MainWindow.show()
        sys.exit(app.exec_())



def main(ui):
    pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.aboutToQuit.connect(trayWaiting)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    main(ui)
    sys.exit(app.exec_())
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 240)
        MainWindow.setMinimumSize(QtCore.QSize(320, 240))
        MainWindow.setMaximumSize(QtCore.QSize(320, 240))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(0, 0, 331, 241))
        self.frame.setStyleSheet("background-color: rgb(58, 173, 173);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 321, 31))
        self.label_8.setObjectName("label_8")
        self.btn_enviar = QtWidgets.QPushButton(self.frame)
        self.btn_enviar.setGeometry(QtCore.QRect(80, 190, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.btn_enviar.setFont(font)
        self.btn_enviar.setObjectName("btn_enviar")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 40, 291, 141))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.txt_usuario = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.txt_usuario.setObjectName("txt_usuario")
        self.verticalLayout_4.addWidget(self.txt_usuario)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        self.txt_senha = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.txt_senha.setObjectName("txt_senha")
        self.verticalLayout_4.addWidget(self.txt_senha)
        self.btn_cadastrar = QtWidgets.QPushButton(self.frame)
        self.btn_cadastrar.setGeometry(QtCore.QRect(230, 200, 75, 23))
        self.btn_cadastrar.setObjectName("btn_cadastrar")
        self.btn_esqueceusenha = QtWidgets.QPushButton(self.frame)
        self.btn_esqueceusenha.setGeometry(QtCore.QRect(0, 200, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.btn_esqueceusenha.setFont(font)
        self.btn_esqueceusenha.setObjectName("btn_esqueceusenha")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setEnabled(True)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 331, 241))
        self.frame_3.setMinimumSize(QtCore.QSize(331, 241))
        self.frame_3.setMaximumSize(QtCore.QSize(331, 241))
        self.frame_3.setStyleSheet("background-color: rgb(163, 156, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.btn_enviar_4 = QtWidgets.QPushButton(self.frame_3)
        self.btn_enviar_4.setGeometry(QtCore.QRect(80, 180, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.btn_enviar_4.setFont(font)
        self.btn_enviar_4.setObjectName("btn_enviar_4")
        self.btn_login = QtWidgets.QPushButton(self.frame_3)
        self.btn_login.setGeometry(QtCore.QRect(230, 190, 75, 23))
        self.btn_login.setObjectName("btn_login")
        self.label_14 = QtWidgets.QLabel(self.frame_3)
        self.label_14.setGeometry(QtCore.QRect(0, 0, 321, 31))
        self.label_14.setObjectName("label_14")
        self.formLayoutWidget = QtWidgets.QWidget(self.frame_3)
        self.formLayoutWidget.setGeometry(QtCore.QRect(70, 80, 160, 61))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.txt_cadastrar_usuario = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_cadastrar_usuario.setObjectName("txt_cadastrar_usuario")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_cadastrar_usuario)
        self.txt_cadastrar_senha = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_cadastrar_senha.setObjectName("txt_cadastrar_senha")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_cadastrar_senha)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(80, 50, 141, 20))
        self.label_3.setObjectName("label_3")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setEnabled(True)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 331, 241))
        self.frame_4.setMinimumSize(QtCore.QSize(331, 241))
        self.frame_4.setMaximumSize(QtCore.QSize(331, 241))
        self.frame_4.setStyleSheet("background-color: rgb(134, 255, 188);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.btn_enviar_novasenha = QtWidgets.QPushButton(self.frame_4)
        self.btn_enviar_novasenha.setGeometry(QtCore.QRect(80, 180, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.btn_enviar_novasenha.setFont(font)
        self.btn_enviar_novasenha.setObjectName("btn_enviar_novasenha")
        self.btn_login_3 = QtWidgets.QPushButton(self.frame_4)
        self.btn_login_3.setGeometry(QtCore.QRect(230, 190, 75, 23))
        self.btn_login_3.setObjectName("btn_login_3")
        self.label_16 = QtWidgets.QLabel(self.frame_4)
        self.label_16.setGeometry(QtCore.QRect(0, 0, 321, 31))
        self.label_16.setObjectName("label_16")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.frame_4)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(70, 80, 160, 61))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_11.setObjectName("label_11")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.txt_novasenha_usuario = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.txt_novasenha_usuario.setObjectName("txt_novasenha_usuario")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_novasenha_usuario)
        self.txt_novasenha_senha = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.txt_novasenha_senha.setObjectName("txt_novasenha_senha")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_novasenha_senha)
        self.label_12 = QtWidgets.QLabel(self.frame_4)
        self.label_12.setGeometry(QtCore.QRect(90, 40, 141, 20))
        self.label_12.setObjectName("label_12")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setEnabled(True)
        self.frame_5.setGeometry(QtCore.QRect(0, 0, 331, 241))
        self.frame_5.setMinimumSize(QtCore.QSize(331, 241))
        self.frame_5.setMaximumSize(QtCore.QSize(331, 241))
        self.frame_5.setStyleSheet("background-color: rgb(220, 151, 255);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.btn_enviar_removerconta = QtWidgets.QPushButton(self.frame_5)
        self.btn_enviar_removerconta.setGeometry(QtCore.QRect(80, 180, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.btn_enviar_removerconta.setFont(font)
        self.btn_enviar_removerconta.setObjectName("btn_enviar_removerconta")
        self.btn_logout = QtWidgets.QPushButton(self.frame_5)
        self.btn_logout.setGeometry(QtCore.QRect(230, 190, 75, 23))
        self.btn_logout.setObjectName("btn_logout")
        self.label_17 = QtWidgets.QLabel(self.frame_5)
        self.label_17.setGeometry(QtCore.QRect(0, 0, 321, 31))
        self.label_17.setObjectName("label_17")
        self.formFrame_4 = QtWidgets.QFrame(self.frame_5)
        self.formFrame_4.setGeometry(QtCore.QRect(70, 80, 160, 38))
        self.formFrame_4.setObjectName("formFrame_4")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formFrame_4)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_13 = QtWidgets.QLabel(self.formFrame_4)
        self.label_13.setObjectName("label_13")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.txt_removerconta_usuario = QtWidgets.QLineEdit(self.formFrame_4)
        self.txt_removerconta_usuario.setObjectName("txt_removerconta_usuario")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_removerconta_usuario)
        self.label_19 = QtWidgets.QLabel(self.frame_5)
        self.label_19.setGeometry(QtCore.QRect(120, 40, 31, 20))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.frame_5)
        self.label_20.setGeometry(QtCore.QRect(50, 150, 111, 20))
        self.label_20.setObjectName("label_20")
        self.lb_nivel_acesso = QtWidgets.QLabel(self.frame_5)
        self.lb_nivel_acesso.setGeometry(QtCore.QRect(150, 150, 21, 20))
        self.lb_nivel_acesso.setObjectName("lb_nivel_acesso")
        self.lb_nomeusuario = QtWidgets.QLabel(self.frame_5)
        self.lb_nomeusuario.setGeometry(QtCore.QRect(150, 40, 61, 20))
        self.lb_nomeusuario.setObjectName("lb_nomeusuario")
        self.lb_nomeusuario_2 = QtWidgets.QLabel(self.frame_5)
        self.lb_nomeusuario_2.setGeometry(QtCore.QRect(30, 120, 261, 20))
        self.lb_nomeusuario_2.setObjectName("lb_nomeusuario_2")
        self.frame_3.raise_()
        self.frame_4.raise_()
        self.frame_5.raise_()
        self.frame.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_cadastrar.clicked['bool'].connect(self.frame.lower)
        self.btn_login.clicked['bool'].connect(self.frame_3.lower)
        self.btn_login.clicked['bool'].connect(self.frame_4.lower)
        self.btn_login_3.clicked['bool'].connect(self.frame_4.lower)
        self.btn_login_3.clicked['bool'].connect(self.frame_3.lower)
        self.btn_cadastrar.clicked['bool'].connect(self.frame_4.lower)
        self.btn_esqueceusenha.clicked['bool'].connect(self.frame.lower)
        self.btn_esqueceusenha.clicked['bool'].connect(self.frame_3.lower)
        self.btn_login_3.clicked['bool'].connect(self.frame_5.lower)
        self.btn_login.clicked['bool'].connect(self.frame_5.lower)
        self.btn_esqueceusenha.clicked['bool'].connect(self.frame_5.lower)
        self.btn_cadastrar.clicked['bool'].connect(self.frame_5.lower)
        self.btn_logout.clicked['bool'].connect(self.frame_5.lower)
        self.btn_logout.clicked['bool'].connect(self.frame_3.lower)
        self.btn_logout.clicked['bool'].connect(self.frame_4.lower)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Empresa XYZ</span></p></body></html>"))
        self.btn_enviar.setText(_translate("MainWindow", "Enviar"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Usuario</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Senha</span></p></body></html>"))
        self.btn_cadastrar.setText(_translate("MainWindow", "Cadastrar"))
        self.btn_esqueceusenha.setText(_translate("MainWindow", "Esqueceu Senha?"))
        self.btn_enviar_4.setText(_translate("MainWindow", "Enviar"))
        self.btn_login.setText(_translate("MainWindow", "Login"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Empresa XYZ</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Usuario</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Senha</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Cadastrar Conta</span></p></body></html>"))
        self.btn_enviar_novasenha.setText(_translate("MainWindow", "Enviar"))
        self.btn_login_3.setText(_translate("MainWindow", "Login"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Empresa XYZ</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Usuario</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Senha</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Esqueceu Senha?</span></p></body></html>"))
        self.btn_enviar_removerconta.setText(_translate("MainWindow", "Enviar"))
        self.btn_logout.setText(_translate("MainWindow", "Logout"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Empresa XYZ</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Usuario</span></p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Olá </span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Nivel Acesso: </span></p></body></html>"))
        self.lb_nivel_acesso.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">0</span></p></body></html>"))
        self.lb_nomeusuario.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">usuario</span></p></body></html>"))
        self.lb_nomeusuario_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Digite a conta que deseja remover</span></p><p align=\"center\"><br/></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

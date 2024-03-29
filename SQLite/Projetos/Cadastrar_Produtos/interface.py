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
        MainWindow.resize(1173, 530)
        MainWindow.setMinimumSize(QtCore.QSize(1173, 530))
        MainWindow.setMaximumSize(QtCore.QSize(1173, 530))
        MainWindow.setStyleSheet("background-color: rgb(128, 199, 203);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 1161, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 460, 1131, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_enviar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.btn_enviar.setFont(font)
        self.btn_enviar.setObjectName("btn_enviar")
        self.horizontalLayout.addWidget(self.btn_enviar)
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 140, 771, 321))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.txt_marca = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        self.txt_marca.setFont(font)
        self.txt_marca.setObjectName("txt_marca")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_marca)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.txt_descricao = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        self.txt_descricao.setFont(font)
        self.txt_descricao.setObjectName("txt_descricao")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_descricao)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.txt_custo = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        self.txt_custo.setFont(font)
        self.txt_custo.setObjectName("txt_custo")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txt_custo)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.txt_codigo = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        self.txt_codigo.setFont(font)
        self.txt_codigo.setObjectName("txt_codigo")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txt_codigo)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.txt_fornecedor = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        self.txt_fornecedor.setFont(font)
        self.txt_fornecedor.setObjectName("txt_fornecedor")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.txt_fornecedor)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.txt_preco = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        self.txt_preco.setFont(font)
        self.txt_preco.setObjectName("txt_preco")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.txt_preco)
        self.txt_produto = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        self.txt_produto.setFont(font)
        self.txt_produto.setObjectName("txt_produto")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_produto)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(830, 140, 331, 151))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(20, 20, 301, 50))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.txt_pesquisar = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.txt_pesquisar.setFont(font)
        self.txt_pesquisar.setObjectName("txt_pesquisar")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_pesquisar)
        self.btn_pesquisar = QtWidgets.QPushButton(self.frame)
        self.btn_pesquisar.setGeometry(QtCore.QRect(20, 90, 301, 43))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.btn_pesquisar.setFont(font)
        self.btn_pesquisar.setObjectName("btn_pesquisar")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(30, 90, 761, 41))
        self.label_11.setObjectName("label_11")
        self.btn_limpar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_limpar.setGeometry(QtCore.QRect(990, 400, 161, 43))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.btn_limpar.setFont(font)
        self.btn_limpar.setObjectName("btn_limpar")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_limpar.clicked['bool'].connect(self.txt_preco.clear)
        self.btn_limpar.clicked['bool'].connect(self.txt_fornecedor.clear)
        self.btn_limpar.clicked['bool'].connect(self.txt_codigo.clear)
        self.btn_limpar.clicked['bool'].connect(self.txt_custo.clear)
        self.btn_limpar.clicked['bool'].connect(self.txt_descricao.clear)
        self.btn_limpar.clicked['bool'].connect(self.txt_marca.clear)
        self.btn_limpar.clicked['bool'].connect(self.txt_produto.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.txt_produto, self.txt_marca)
        MainWindow.setTabOrder(self.txt_marca, self.txt_descricao)
        MainWindow.setTabOrder(self.txt_descricao, self.txt_custo)
        MainWindow.setTabOrder(self.txt_custo, self.txt_codigo)
        MainWindow.setTabOrder(self.txt_codigo, self.txt_fornecedor)
        MainWindow.setTabOrder(self.txt_fornecedor, self.txt_preco)
        MainWindow.setTabOrder(self.txt_preco, self.btn_enviar)
        MainWindow.setTabOrder(self.btn_enviar, self.txt_pesquisar)
        MainWindow.setTabOrder(self.txt_pesquisar, self.btn_pesquisar)
        MainWindow.setTabOrder(self.btn_pesquisar, self.btn_limpar)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cadastrar Produtos"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">Empresa XYZ</span></p></body></html>"))
        self.btn_enviar.setText(_translate("MainWindow", "Enviar"))
        self.label_2.setText(_translate("MainWindow", "Produto"))
        self.label_3.setText(_translate("MainWindow", "Marca"))
        self.label_4.setText(_translate("MainWindow", "Descrição"))
        self.label_5.setText(_translate("MainWindow", "Custo"))
        self.label_6.setText(_translate("MainWindow", "Codigo"))
        self.label_7.setText(_translate("MainWindow", "Fornecedor"))
        self.label_8.setText(_translate("MainWindow", "Preço venda"))
        self.label_9.setText(_translate("MainWindow", "Codigo"))
        self.btn_pesquisar.setText(_translate("MainWindow", "Pesquisar"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Cadastrar Produtos</span></p></body></html>"))
        self.btn_limpar.setText(_translate("MainWindow", "Limpar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

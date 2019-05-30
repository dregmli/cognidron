# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Simple.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblEiqueta = QtWidgets.QLabel(self.centralwidget)
        self.lblEiqueta.setGeometry(QtCore.QRect(60, 60, 61, 21))
        self.lblEiqueta.setObjectName("lblEiqueta")
        self.btnBoton = QtWidgets.QPushButton(self.centralwidget)
        self.btnBoton.setGeometry(QtCore.QRect(60, 120, 75, 23))
        self.btnBoton.setObjectName("btnBoton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        self.menuNada_por_aqui = QtWidgets.QMenu(self.menubar)
        self.menuNada_por_aqui.setObjectName("menuNada_por_aqui")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuNada_por_aqui.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ventana Simpler con Grafica"))
        self.lblEiqueta.setText(_translate("MainWindow", "MiEtiqueta"))
        self.btnBoton.setText(_translate("MainWindow", "MiBoton"))
        self.menuNada_por_aqui.setTitle(_translate("MainWindow", "Nada por aqui"))



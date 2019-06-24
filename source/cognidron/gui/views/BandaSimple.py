# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BandaSimple.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WindowBandaSimple(object):
    def setupUi(self, WindowBandaSimple):
        WindowBandaSimple.setObjectName("WindowBandaSimple")
        WindowBandaSimple.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(WindowBandaSimple)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 50, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 61, 16))
        self.label.setObjectName("label")
        WindowBandaSimple.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WindowBandaSimple)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        WindowBandaSimple.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WindowBandaSimple)
        self.statusbar.setObjectName("statusbar")
        WindowBandaSimple.setStatusBar(self.statusbar)

        self.retranslateUi(WindowBandaSimple)
        QtCore.QMetaObject.connectSlotsByName(WindowBandaSimple)

    def retranslateUi(self, WindowBandaSimple):
        _translate = QtCore.QCoreApplication.translate
        WindowBandaSimple.setWindowTitle(_translate("WindowBandaSimple", "Banda simple 1"))
        self.pushButton.setText(_translate("WindowBandaSimple", "Print"))
        self.label.setText(_translate("WindowBandaSimple", "Vacío"))



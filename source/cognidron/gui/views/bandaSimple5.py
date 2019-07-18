# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bandaSimple5.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BandaSimple5(object):
    def setupUi(self, BandaSimple5):
        BandaSimple5.setObjectName("BandaSimple5")
        BandaSimple5.resize(1366, 720)
        self.centralwidget = QtWidgets.QWidget(BandaSimple5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 0, 73, 691))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.verticalLayout.addWidget(self.comboBox_2)
        self.comboBox_3 = QtWidgets.QComboBox(self.widget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.verticalLayout.addWidget(self.comboBox_3)
        self.comboBox_4 = QtWidgets.QComboBox(self.widget)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.verticalLayout.addWidget(self.comboBox_4)
        self.comboBox_5 = QtWidgets.QComboBox(self.widget)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.verticalLayout.addWidget(self.comboBox_5)
        BandaSimple5.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BandaSimple5)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 21))
        self.menubar.setObjectName("menubar")
        BandaSimple5.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BandaSimple5)
        self.statusbar.setObjectName("statusbar")
        BandaSimple5.setStatusBar(self.statusbar)

        self.retranslateUi(BandaSimple5)
        QtCore.QMetaObject.connectSlotsByName(BandaSimple5)

    def retranslateUi(self, BandaSimple5):
        _translate = QtCore.QCoreApplication.translate
        BandaSimple5.setWindowTitle(_translate("BandaSimple5", "MainWindow"))
        self.comboBox.setItemText(0, _translate("BandaSimple5", "Electrodo"))
        self.comboBox_2.setItemText(0, _translate("BandaSimple5", "Electrodo"))
        self.comboBox_3.setItemText(0, _translate("BandaSimple5", "Electrodo"))
        self.comboBox_4.setItemText(0, _translate("BandaSimple5", "Electrodo"))
        self.comboBox_5.setItemText(0, _translate("BandaSimple5", "Electrodo"))



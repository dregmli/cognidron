"""
Raios, por algún motivo se borro sste codigo, tal vez por el conflicto que tuve en la lap lenovo :P

A volverlo a hacer :P

Fechas: 16 de julio de 2019
"""


import time
import numpy as np
import pyqtgraph as pg
from gui.views.BandaSimple5 import *


class MyWin(QtWidgets.QMainWindow):

    def __init__(self, parent=None):

        QtWidgets.QWidget.__init__(self, parent)

        self.ui = Ui_BandaSimple5()
        self.ui.setupUi(self)


        x = np.random.normal(loc=0.0, scale=2, size=100)

        widget = pg.PlotWidget(self.ui.centralwidget, title="Some plotting", )
        widget.setWindowTitle("Random Plottoring")
        # widget.plotItem.plot(x)
        # widget.show()
        curve = widget.plotItem.plot(pen='y')
        data = np.random.normal(size=(10, 1000))
        ptr = 0
        self.ui.grafica = widget
        self.ui.grafica.setGeometry(QtCore.QRect(200, 10, 400, 400))
        self.ui.grafica.setObjectName("miGrafica")

        p6 = widget

        # Generar hilo para graficar
        self.funcionx()
        hilo = MiHilo(ptr, p6, curve, data)
        hilo.start()

        # self.ui.btnBoton2 = QtWidgets.QPushButton(self.ui.centralwidget)
        # self.ui.btnBoton2.setGeometry(QtCore.QRect(60, 60, 75, 23))
        # self.ui.btnBoton2.setObjectName("btnBoton2")

    def funcionx(self):
        print("ok ------")

    # Evento del boton btn_CtoF
    def btn_tocado(self):
        print("me diste un clic")


import threading


class MiHilo(threading.Thread):
    breaker = 1000000
    n = 0

    def __init__(self, ptr, p6, curve, data):
        super().__init__(
            daemon=True)  # esto hace daemon a un hilo para que se cierre cuadno el hilo principal se cierre.
        self.ptr = ptr
        self.p6 = p6
        self.curve = curve
        self.data = data

    def update(self):
        print("esto se ejecuta? " + str(self.ptr))
        self.curve.setData(self.data[self.ptr % 10])
        if self.ptr == 0:
            self.p6.enableAutoRange('xy', False)  ## stop auto-scaling after the first data set is plotted
        self.ptr += 1

    def run(self):
        while self.n < self.breaker:
            self.n += 1
            self.update()
            time.sleep(0.02)
            print("####")




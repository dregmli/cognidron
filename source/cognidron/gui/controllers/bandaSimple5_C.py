"""
Raios, por algún motivo se borro sste codigo, tal vez por el conflicto que tuve en la lap lenovo :P

A volverlo a hacer :P

Fechas: 16 de julio de 2019
"""


import time
from random import random

import numpy as np
import pyqtgraph as pg
from gui.views.bandaSimple5 import *


class BandaSimple5_C(QtWidgets.QMainWindow):
    """
        Clase controlador de la vista BandaSimple5.
        Aqui se agregan 5 gráficas de pyqtgraph en una ventana de pytq5. Tales gráficas llevan los datos obtenidos de
        las bandas de frecuencia del dispositiov Emotiv Epoc + usando el API de Cortex v2.0
    """

    hilo = None

    def __init__(self, parent=None):

        QtWidgets.QWidget.__init__(self, parent)

        self.ui = Ui_BandaSimple5()
        self.ui.setupUi(self)


        # Coordenadas de las gráficas
        graphWidth = 1150
        graphHigh = 110
        spaceY = 14
        x1 = 160
        y1 = 50

        y2 = y1 + graphHigh + spaceY
        y3 = y2 + graphHigh + spaceY
        y4 = y3 + graphHigh + spaceY
        y5 = y4 + graphHigh + spaceY


        # Band theta
        widget = pg.PlotWidget(self.ui.centralwidget, title="Theta", )
        widget.setWindowTitle("Theta")
        # widget.plotItem.plot(x)
        # widget.show()
        curve = widget.plotItem.plot(pen='y')
        self.ui.bandTheta = widget
        self.ui.bandTheta.setGeometry(QtCore.QRect(x1, y1, graphWidth, graphHigh))
        self.ui.bandTheta.setObjectName("bandTheta")
        # Generar hilo para graficar
        self.threadTheta = MyThread(self.ui.bandTheta, curve)
        self.threadTheta.start()


        # Band alpha
        widget = pg.PlotWidget(self.ui.centralwidget, title="Alpha", )
        widget.setWindowTitle("Alpha")
        curve = widget.plotItem.plot(pen='r')
        self.ui.bandAlpha = widget
        self.ui.bandAlpha.setGeometry(QtCore.QRect(x1, y2, graphWidth, graphHigh))
        self.ui.bandAlpha.setObjectName("bandTheta")
        # Generar hilo para graficar
        self.threadAlpha = MyThread(self.ui.bandAlpha, curve)
        self.threadAlpha.start()

        # Band betaLow
        widget = pg.PlotWidget(self.ui.centralwidget, title="Beta Low", )
        widget.setWindowTitle("Beta Low")
        curve = widget.plotItem.plot(pen='b')
        self.ui.bandBetaL = widget
        self.ui.bandBetaL.setGeometry(QtCore.QRect(x1, y3, graphWidth, graphHigh))
        self.ui.bandBetaL.setObjectName("bandBetaL")
        # Generar hilo para graficar
        self.threadBetaL = MyThread(self.ui.bandBetaL, curve)
        self.threadBetaL.start()

        # Band betaHigh
        widget = pg.PlotWidget(self.ui.centralwidget, title="Beta High", )
        widget.setWindowTitle("Beta High")
        curve = widget.plotItem.plot(pen='g')
        self.ui.bandBetaH = widget
        self.ui.bandBetaH.setGeometry(QtCore.QRect(x1, y4, graphWidth, graphHigh))
        self.ui.bandBetaH.setObjectName("bandBetaH")
        # Generar hilo para graficar
        self.threadBetaH = MyThread(self.ui.bandBetaH, curve)
        self.threadBetaH.start()

        # Band betaGamma
        widget = pg.PlotWidget(self.ui.centralwidget, title="Gamma", )
        widget.setWindowTitle("Gamma")
        curve = widget.plotItem.plot(pen='wcapturas')
        self.ui.bandGamma = widget
        self.ui.bandGamma.setGeometry(QtCore.QRect(x1, y5, graphWidth, graphHigh))
        self.ui.bandGamma.setObjectName("bandGamma")
        # Generar hilo para graficar
        self.threadGamma = MyThread(self.ui.bandBetaH, curve)
        self.threadGamma.start()






        # self.ui.btnBoton2 = QtWidgets.QPushButton(self.ui.centralwidget)
        # self.ui.btnBoton2.setGeometry(QtCore.QRect(60, 60, 75, 23))
        # self.ui.btnBoton2.setObjectName("btnBoton2")

    def funcionx(self):
        print("ok ------")

    # Evento del boton btn_CtoF
    def btn_tocado(self):
        print("me diste un clic")


    def closeEvent(self, event):  # Se ejecuta al cerrar la ventana
        print("Cerrando ventana de 5 bandas.........")
        #self.hilo.nf.closeConnection()
        self.deleteLater()


import threading
from interfaces.nf.emotivNFAdapter import EmotivNFAdapter

class MyThread(threading.Thread):
    breaker = 1000000
    bands = None
    # el data para la grafica debe ser un array numpy
    array_y = [1.0, 0]


    def __init__(self, graphBand, curve):
        """

        :param graphBand: grafica obtenida de pyqtgraph.PlotWidget(...), donde se graficará una banda de frecuencia
        :param curve: curva obetnida de widget.plotItem.plot(pen='y') o band.plotItem.plot(pen='y') donde se asigna los valores de la señal
        """
        super().__init__(
            daemon=True)  # esto hace daemon a un hilo para que se cierre cuadno el hilo principal se cierre.
        self.graphBand = graphBand
        self.curve = curve

        # Iniciar conexión con Emotiv para obetner las bandas
        self.nf = EmotivNFAdapter()
        # self.nf.startConnection()






    def update(self):
        #print("esto se ejecuta? " + str(self.ptr))

        # Obtener los potenciales de las bandas de frecuencia
        #self.bands = self.nf.receivePow()
        #n = self.bands['AF3/theta']
        #self.array_y.append(n)
        n = random()*10+1
        print("numero random n: " + str(n) )

        self.array_y.append(n)

        self.curve.setData(self.array_y) # self.data[self.ptr % 10]

        """
        if self.ptr == 0:
            self.p6.enableAutoRange('xy', False)  ## stop auto-scaling after the first data set is plotted
        self.ptr += 1
        """

    def run(self):
        while True:
            self.update()
            time.sleep(0.1)





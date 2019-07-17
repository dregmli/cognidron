"""
Raios, por algún motivo se borro sste codigo, tal vez por el conflicto que tuve en la lap lenovo :P

A volverlo a hacer :P

Fechas: 16 de julio de 2019
"""


import time
import numpy as np
import pyqtgraph as pg
from gui.views.BandaSimple5 import *


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


        x = np.random.normal(loc=0.0, scale=2, size=100)

        widget = pg.PlotWidget(self.ui.centralwidget, title="Some plotting", )
        widget.setWindowTitle("Random Plottoring")
        # widget.plotItem.plot(x)
        # widget.show()
        curve = widget.plotItem.plot(pen='y')
        data = np.random.normal(size=(10, 1000))
        ptr = 0
        self.ui.grafica = widget
        self.ui.grafica.setGeometry(QtCore.QRect(160, 50, 850, 110))
        self.ui.grafica.setObjectName("miGrafica")

        p6 = widget

        # Generar hilo para graficar
        self.funcionx()
        self.hilo = MiHilo(ptr, p6, curve, data)
        self.hilo.start()

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
        self.hilo.nf.closeConnection()
        self.deleteLater()


import threading
from interfaces.nf.emotivNFAdapter import EmotivNFAdapter

class MiHilo(threading.Thread):
    breaker = 1000000
    n = 0
    bands = None
    # el data para la grafica debe ser un array numpy
    array_y = [1.0, 0]


    def __init__(self, ptr, p6, curve, data):
        super().__init__(
            daemon=True)  # esto hace daemon a un hilo para que se cierre cuadno el hilo principal se cierre.
        self.ptr = ptr
        self.p6 = p6
        self.curve = curve
        self.data = data

        # Iniciar conexión con Emotiv para obetner las bandas
        self.nf = EmotivNFAdapter()
        # self.nf.startConnection()





    def update(self):
        #print("esto se ejecuta? " + str(self.ptr))

        # Obtener los potenciales de las bandas de frecuencia
        #self.bands = self.nf.receivePow()
        #n = self.bands['AF3/theta']
        #self.array_y.append(n)

        

        self.curve.setData(self.array_y) # self.data[self.ptr % 10]
        """
        if self.ptr == 0:
            self.p6.enableAutoRange('xy', False)  ## stop auto-scaling after the first data set is plotted
        self.ptr += 1
        """

    def run(self):
        while self.n < self.breaker:
            self.n += 1
            self.update()
            time.sleep(0.1)




"""
Este es una modificacion del modulo GraficarBandasPoder.py para funcionar en Cortex v2.0 y usando la clase EmotivNFAdapter

En este código se busca hacer una pequeña gráfica en tiempo real de las
banda de frecuencia o potencia obtnenidas del Emotiv Epoc + mediante
el Cortex v2.0

Este programa combina el "Time.py" y "pasos para iniciar.py"
"""

# Parte Time.py
import sys
import time
import numpy as np
from interfaces.nf.emotivNFAdapter import EmotivNFAdapter

from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5

if is_pyqt5():
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

# Parte para comunicación con Cortex UI de Emotiv
from websocket import create_connection
import ssl
import json

conteo = 0
mensaje = ""

nf = EmotivNFAdapter()
nf.startConnection()

class ApplicationWindow(QtWidgets.QMainWindow):

    lista = [0]

    def __init__(self):
        super().__init__()
        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)
        layout = QtWidgets.QVBoxLayout(self._main)

        static_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        layout.addWidget(static_canvas)
        self.addToolBar(NavigationToolbar(static_canvas, self))

        dynamic_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        layout.addWidget(dynamic_canvas)
        self.addToolBar(QtCore.Qt.BottomToolBarArea,
                        NavigationToolbar(dynamic_canvas, self))

        self._static_ax = static_canvas.figure.subplots()
        t = np.linspace(0, 10, 501)
        self._static_ax.plot(t, np.tan(t), ".")

        self._dynamic_ax = dynamic_canvas.figure.subplots()
        self._timer = dynamic_canvas.new_timer(
            100, [(self._update_canvas, (), {})])
        self._timer.start()

    def _update_canvas(self):
        self._dynamic_ax.clear()
        t = np.linspace(0, 10, 101)  # (0, 10, 101)
        # Shift the sinusoid as a function of time.
        """ modificate esto para mandar a la grafica los resultados del emotiv
        self._dynamic_ax.plot(t, np.sin(t + time.time())) """

        bands = nf.receivePow()
        self.lista.append(bands['AF3/theta'])

        # self._dynamic_ax.plot( diccionario['pow'][0], diccionario['pow'][1] )
        self._dynamic_ax.plot(self.lista)  # self.dynamic_ax.plot(time.time(), diccionario['pow'][0])
        self._dynamic_ax.figure.canvas.draw()
        time.sleep(0.1)


if __name__ == "__main__":
    qapp = QtWidgets.QApplication(sys.argv)
    app = ApplicationWindow()
    app.show()
    qapp.exec_()

nf.closeConnection()
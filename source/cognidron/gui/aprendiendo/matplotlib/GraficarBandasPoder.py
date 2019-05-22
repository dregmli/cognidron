"""
En este código se busca hacer una pequeña gráfica en tiempo real de las 
banda de frecuencia o potencia obtnenidas del Emotiv Epoc + mediante
el Cortex UI, con el cual se realiza una comunicación por Web Sockets usando Jsons.

Este programa combina el "Time.py" y "pasos para iniciar.py"
"""

#Parte Time.py
import sys
import time
import numpy as np

from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5
if is_pyqt5():
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure



#Parte para comunicación con Cortex UI de Emotiv
from websocket import create_connection
import ssl
import json

conteo = 0
mensaje = ""

#conectamos el WS
ws = create_connection("wss://emotivcortex.com:54321",
sslopt={"cert_reqs": ssl.CERT_NONE})

def principal():
    #ws = create_connection("wss://emotivcortex.com:54321") #ws://echo.websocket.org/
    #1. 
    mensaje = ' {"jsonrpc": "2.0", "method": "queryHeadsets","params": {},"id": 1} '
    ejecutar(mensaje)


    mensaje = '{"jsonrpc": "2.0","method": "authorize","params": {}, "id": 1 }'
    jsonData = ejecutar(mensaje)

    JsonToPython = json.loads(jsonData)

    #2. 
    mensaje = ' {"jsonrpc": "2.0", "method": "createSession", "params": {"_auth": "' + JsonToPython['result']['_auth'] + '","status": "open", "title": "prueba1"}, "id": 1}'
    ejecutar(mensaje)

    #3
    mensaje = '{"jsonrpc": "2.0","method": "subscribe","params": {"_auth": "' + JsonToPython['result']['_auth'] + '","streams": ["pow"]},"id": 1}'
    ejecutar(mensaje)

    result =  ws.recv()
    print("Received '%s'" % result)
    print("")
    result =  ws.recv()
    print("Received '%s'" % result)
    print("")
    result =  ws.recv()
    print("Received '%s'" % result)
    print("")
    result =  ws.recv()
    print("Received '%s'" % result)
    print("")
    result =  ws.recv()
    print("Received '%s'" % result)
    print("")
    result =  ws.recv()
    print("Received '%s'" % result)
    print("")
    result =  ws.recv()
    print("Received '%s'" % result)
    print("")
    result =  ws.recv()
    print("Received '%s'" % result)

    #ws.close()

    return 0

def ejecutar(txt):
    global conteo
    conteo =+ 1
    print(str(conteo) + ": ----------------------------------------------------------------------")
    print("Sending mensaje: ")
    print(txt)
    ws.send(txt)
    print("Sent")
    print("Receiving...")
    result =  ws.recv()
    print("Received '%s'" % result)
    return result

#y ahora si ejecutamos las funciones
principal()





class ApplicationWindow(QtWidgets.QMainWindow):
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
        t = np.linspace(0, 10, 101) #(0, 10, 101)
        # Shift the sinusoid as a function of time.
        """ modificate esto para mandar a la grafica los resultados del emotiv
        self._dynamic_ax.plot(t, np.sin(t + time.time())) """
        
        #mensaje = '{"jsonrpc": "2.0","method": "authorize","params": {}, "id": 1 }'
        #jsonData = ejecutar(mensaje)
        
        #en este momento se supone que estamos suscritos en modo 'pwr'
        respuesta = ""
        respuesta =  ws.recv()
        diccionario = json.loads(respuesta) #se transforma el json en un diccionario de python

        #print("Received '%s'" % respuesta)
        print("pow: '%s'"  %str(diccionario['pow'][0]) )
        print("")

        #self._dynamic_ax.plot( diccionario['pow'][0], diccionario['pow'][1] )
        self._dynamic_ax.plot(time.time(), diccionario['pow'][0]) 
        self._dynamic_ax.figure.canvas.draw()


if __name__ == "__main__":
    qapp = QtWidgets.QApplication(sys.argv)
    app = ApplicationWindow()
    app.show()
    qapp.exec_()


ws.close()
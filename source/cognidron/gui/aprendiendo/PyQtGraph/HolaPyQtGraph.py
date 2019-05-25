# hola mundo con PyQtGrapgh
#tuto de aca: http://www.laboratoriogluon.com/pyqtgraph-graficas-tiempo-real-con-python/

from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg 
import sys

from random import randrange

cerrar = False
app = QtGui.QApplication(sys.argv)
app.quitOnLastWindowClosed = True
win = pg.GraphicsWindow(title="Gráfica en tiempo real")
p = win.addPlot(title="Gráfica tiempo real")

curva = p.plot(pen='y')
p.setRange(yRange=[0, 110]) #rango para Y

#curva.setData([0,10,20,30,40],[10,20,40,80,160]) #.setData(X_data, Y_data)

dataX = [] #Array para guardar los datos
dataY = []
lastY = 0

def update():
    global curva, dataX, dataY, lastY

    #Obtenemos el nuevo valor
    nuevoDato = randrange(100)

    #Agregamos los datos al array
    dataX.append(nuevoDato)
    dataY.append(lastY)
    lastY += 1

    # Limitamos a mostrar solo 300 muestras
    if len(dataX) > 100:
        #dataX = dataX[:-1]
        #dataY = dataY[:-1]
        dataX.pop(0)
        dataY.pop(0)

    #Actualizamos los datos y refrescamos la grafica
    curva.setData(dataY, dataX)
    QtGui.QGuiApplication.processEvents()

#no se ocmo usar eso:::: app.lastWindowClosed(): 
    



while (cerrar != True): 
    update()



pg.QtGui.QApplication.exec_()
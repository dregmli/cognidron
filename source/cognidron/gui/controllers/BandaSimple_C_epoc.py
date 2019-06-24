#informacion muy util de hilos:
#   https://python-para-impacientes.blogspot.com/2016/12/threading-programacion-con-hilos-i.html


import sys 

#esto es temporal, mientras no se corre el mainpy desde el root de cognidron
sys.path.append("D:\\Usuarines\\mora dulce\\Documentox\\PythonProjects\\Cognidron Dev\\source\\cognidron\\gui\\ventanas")
    
print(sys.path)

import time
import numpy as np
import pyqtgraph as pg 
from BandaSimple import *




class MyWin(QtWidgets.QMainWindow):

  def __init__ (self, parent=None):

        #configuracion de inicio
        #sys.append("../..") #ruta root del programa: cognidron/

        QtWidgets.QWidget.__init__(self, parent)

        self.ui = Ui_WindowBandaSimple()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.btn_tocado)


        x = np.random.normal(loc=0.0, scale=2, size=100)
        
        widget = pg.PlotWidget(self.ui.centralwidget, title="Some plotting",)
        widget.setWindowTitle("Random Plottoring")
        #widget.plotItem.plot(x)
        #widget.show()
        curve = widget.plotItem.plot(pen='y')
        data = np.random.normal(size=(10,1000))
        ptr = 0
        self.ui.grafica = widget
        self.ui.grafica.setGeometry(QtCore.QRect(200, 10, 400, 400))
        self.ui.grafica.setObjectName("miGrafica")

        p6 = widget

        #Generar hilo para graficar
        self.funcionx()
        hilo = MiHilo(ptr, p6, curve, data)
        hilo.start()

        



        #self.ui.btnBoton2 = QtWidgets.QPushButton(self.ui.centralwidget)
        #self.ui.btnBoton2.setGeometry(QtCore.QRect(60, 60, 75, 23))
        #self.ui.btnBoton2.setObjectName("btnBoton2")

  
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
      super().__init__(daemon=True) #esto hace daemon a un hilo para que se cierre cuadno el hilo principal se cierre.
      self.ptr = ptr
      self.p6 = p6
      self.curve = curve
      self.data = data

    def update(self):
      print("esto se ejecuta? " + str(self.ptr))
      self.curve.setData(self.data[self.ptr%10])
      if self.ptr == 0:
          self.p6.enableAutoRange('xy', False)  ## stop auto-scaling after the first data set is plotted
      self.ptr += 1


    def run(self):
      while self.n < self.breaker: 
        self.n += 1
        self.update()
        time.sleep(0.02)
        print("####")
      
      


if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        print("1: esto si sucede")
        myapp = MyWin()
        print("2: esto si sucede")
        myapp.show()

        print("3: esto si sucede")
        sys.exit(app.exec_())
        print("4: esto si sucede")

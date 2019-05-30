


import sys 

#esto es temporal, mientras no se corre el mainpy desde el root de cognidron
sys.path.append("D:\\Usuarines\\mora dulce\\Documentox\\PythonProjects\\Cognidron Dev\\source\\cognidron\\gui\\ventanas")
    
print(sys.path)

import numpy as np
import pyqtgraph as pg 
from BandaSimple import *




class MyWin(QtWidgets.QMainWindow):
  curve = None
  data = None
  ptr = 0
  p6 = None

  def __init__ (self, parent=None):
        global curve, data, p6

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

        timer = QtCore.QTimer()
        p6 = widget
        print("se conectara el timer con updat")
        timer.timeout.connect(self.update)
        timer.start(5)


     


        #self.ui.btnBoton2 = QtWidgets.QPushButton(self.ui.centralwidget)
        #self.ui.btnBoton2.setGeometry(QtCore.QRect(60, 60, 75, 23))
        #self.ui.btnBoton2.setObjectName("btnBoton2")

  def update():
    
    global curve, data, ptr, p6
    print("esto se ejecuta? " + str(ptr))
    curve.setData(data[ptr%10])
    if ptr == 0:
        p6.enableAutoRange('xy', False)  ## stop auto-scaling after the first data set is plotted
    ptr += 1
    
    


  # Evento del boton btn_CtoF
  def btn_tocado(self):
    print("me diste un clic")


if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        myapp = MyWin()
        myapp.show()
        sys.exit(app.exec_())

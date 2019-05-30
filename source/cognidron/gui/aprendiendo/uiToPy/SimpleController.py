
from Simple import *
import sys 
import numpy as np
import pyqtgraph as pg 

class MyWin(QtWidgets.QMainWindow):
  def __init__ (self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnBoton.clicked.connect(self.btn_tocado)

        x = np.random.normal(loc=0.0, scale=2, size=100)

        widget = pg.PlotWidget(self.ui.centralwidget, title="Some plotting",)
        widget.setWindowTitle("Random Plottoring")
        widget.plotItem.plot(x)
        #widget.show()

        self.ui.grafica = widget
        self.ui.grafica.setGeometry(QtCore.QRect(200, 10, 400, 400))
        self.ui.grafica.setObjectName("miGrafica")

        self.ui.btnBoton2 = QtWidgets.QPushButton(self.ui.centralwidget)
        self.ui.btnBoton2.setGeometry(QtCore.QRect(60, 60, 75, 23))
        self.ui.btnBoton2.setObjectName("btnBoton2")




  # Evento del boton btn_CtoF
  def btn_tocado(self):
    print("me diste un clic")


if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        myapp = MyWin()
        myapp.show()
        sys.exit(app.exec_())

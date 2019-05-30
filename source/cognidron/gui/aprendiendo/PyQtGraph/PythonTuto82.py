#tuto obtenido de aca https://www.youtube.com/watch?v=a8xNuu-2X_4

import sys
import pyqtgraph as pg 
import numpy as np 
from PyQt5 import QtGui, QtCore

app = QtGui.QApplication(sys.argv) #QGuiApplication

x = np.random.normal(loc=0.0, scale=2, size=100)

widget = pg.PlotWidget(title="Some plotting")
widget.setWindowTitle("Random Plottoring")
widget.plotItem.plot(x)
widget.show()

sys.exit(app.exec_())

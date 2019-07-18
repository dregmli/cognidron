

from gui.views.mainWndow import *
from gui.controllers.bandaSimple5_C import *

class MainWindow_C(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnBands.setToolTip("Mostrar las graficas de als bandas en tiempo real de potenciales de frecuencia")
        self.ui.btnBands.clicked.connect(self.on_click)

    def on_click(self):
        print("diste click al boton")
        wBands = BandaSimple5_C()
        wBands.show()





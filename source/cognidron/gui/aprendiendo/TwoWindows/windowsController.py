
import sys
from PyQt5 import QtWidgets
from gui.aprendiendo.TwoWindows.window1 import *
from gui.aprendiendo.TwoWindows.window2 import *

class WindowsController(QtWidgets.QMainWindow, Ui_FirstWindow):
    ventana = None
    ui = None

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_FirstWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.abrir)

    def abrir(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

# Esto no jala, rayos :P
# tuto seguido de aca https://www.youtube.com/watch?v=V4ACsfbKtpU

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WindowsController()
    window.show()

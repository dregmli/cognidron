
from gui.controllers.BandaSimple5_C import *
import sys


app = QtWidgets.QApplication(sys.argv)
print("1: esto si sucede")
myapp = MyWin()
print("2: esto si sucede")
myapp.show()

print("3: esto si sucede")
sys.exit(app.exec_())
print("4: esto si sucede")


# Pendiente: rehacer el contrlador de la ventana de 5 Bandas
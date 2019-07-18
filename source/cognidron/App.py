"""
Aplicaciòn principal del Cognidron. Aquí inicia todo.
"""
from interfaces.simulador.simudrouAdapter import SimudrouAdapter
from main.centroControlEegSimulador import CentroControlEegSimulador
from gui.controllers.mainWindow_C import *
import sys

print("Inciando Cognidron v0.01")


# Verificar que existan todos los modulos


print("")
print("- hasta aqui todo bien - ")

# Test de comunicación con el simulador


# CentroControlEegSimulador()

# Ventana principal
app = QtWidgets.QApplication(sys.argv)
myapp = MainWindow_C()
myapp.show()
sys.exit(app.exec_())



import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog
from PyQt5 import uic

# Clase heredada de QMainWindow
class Principal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)  # Iniciar el objeto QMainWindow
        # Cargar la configuración del archivo .ui
        uic.loadUi("myWindow.ui", self)

        # Conectar el click con el método
        self.btnAceptar.clicked.connect(self.conectar)
        self.ventana = Ventana()  # se instancia la ventana al inicio

    def showEvent(self, event):
        self.lblBienvenida.setText("Bienvenido a la aplicación")

    def closeEvent(self, event):
        pregunta = QMessageBox.question(self, "Salir", "¿Seguro que quiere salir?", QMessageBox.Yes | QMessageBox.No)
        if pregunta == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def moveEvent(self, event):
        x = str(event.pos().x())
        y = str(event.pos().y())
        self.lblPosicion.setText("x: " + x + ",  y: " + y)

    def conectar(self):
        self.ventana.exec_()  # y se ejecuta aqui


class Ventana(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("ventana.ui", self)


# Instancia para iniciar una plaicación
app = QApplication(sys.argv)
# Crear un objeto d ela clase
principal = Principal()
principal.show()
# Ejecutar la aplicación
app.exec_()

# sigue seguir este tutorial: https://www.youtube.com/watch?v=2-gZKRD4CYs
# el pendiente actual:
#   - tratar de cargar una ventana completa (QMainWindow) en lugar de un Qdialog
#   - aprender a usar el MDI Area
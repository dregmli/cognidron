#tuto seguido de https://www.youtube.com/watch?v=xC9zV3QVqVs
#                1 - Python PyQt (Interfaz gráfica) - Instalación y primer archivo .ui      

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow #para trabajar con la aplicación y con ventanas
from PyQt5 import uic #para manejar archivos .uic
import os


#Clase heredada de QMainWindow (Constructor de ventanas)
class Ventana(QMainWindow):
    #Método constructor de la clase
    def __init__(self):
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)

        #Obtener el directorrio "ventanas" dónde estan los .ui
        os.chdir("../ventanas")
        ruta = os.getcwd()  
        #print("::::nuevo directorio: " + ruta)


        #Cargar la configuración del archivo .ui en el objeto
        uic.loadUi(ruta + "/VPrincipal2.ui",self)

        #ejemplo cambiar el titulo
        #self.setWindowTitle("Cambiando el título desde código")

# Instancia para inciar una aplicación
app = QApplication(sys.argv)

#Crear un objeto de la clase Ventana
_ventana = Ventana()

#Mostrar la ventana
_ventana.show()

#Ejecutar la aplicación
app.exec_()
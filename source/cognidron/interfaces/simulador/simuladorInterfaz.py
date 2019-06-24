

# Para usar esta clase como una interfaz en POO se utiliza esta libreria
# mas info en: https://www.python-course.eu/python3_abstract_classes.php
from abc import ABC, abstractmethod


class SimuladorInterfaz(ABC):
    """
        Interfaz abstracta que debe implementarse para conectar el cognidron con el simulador de drones.
    """

    conectado = False

    def __init__(self):
        print(":)")

    @abstractmethod
    def decirHola(self):
        # Debes implementar este método para decir hola como tu quieras
        pass

    @abstractmethod
    def iniciarConexion(self):
        pass

    @abstractmethod
    def cerrarConexion(self):
        pass

    @abstractmethod
    def enviarMensaje(self, mensaje):
        pass

    @abstractmethod
    def recibirMensaje(self):
        return ""


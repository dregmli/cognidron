

# Para usar esta clase como una interfaz en POO se utiliza esta libreria
# mas info en: https://www.python-course.eu/python3_abstract_classes.php
from abc import ABC, abstractmethod


class EegInterfaz(ABC):
    """
        Interfaz abstracta que debe implementarse para conectar el cognidron con el dispositivo de EEG.
    """

    conectado = False
    # para saber si se encuentra conectado con el dispositivo EEG

    def __init__(self):
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


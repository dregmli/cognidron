"""
Interfaz para realizar adapatadores del protoco NF con el dispositivo EEG.
"""


from abc import ABC, abstractmethod


class NFInterface(ABC):
    """
        Interfaz abstracta que debe implementarse para conectar el cognidron con el dispositivo de EEG.
    """
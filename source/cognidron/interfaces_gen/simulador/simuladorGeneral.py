"""
    Esta es una implementación del adapatador de algun simulador de dron para el Cognidron.
"""

from interfaces_esp.simulador.simdrouAdapter import SimdrouAdapter


class SimuladorGeneral:
    # Clase que Implementa una interfaz especifica de un simulador de drones.

    def __init__(self):
        print("Iniciando implementación del simulador")

        simulador = SimdrouAdapter()
        simulador.decirHola()

        simulador.prueba()


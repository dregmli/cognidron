"""
Aplicaciòn principal del Cognidron. Aquí inicia todo.
"""
from interfaces_gen.comandos.eegGeneral import EegGeneral
from interfaces_gen.simulador.simuladorGeneral import SimuladorGeneral
from main.centroControlEegSimulador import CentroControlEegSimulador

print("Inciando Cognidron v0.01")


# Verificar que existan todos los modulos

# Usar el simulador del dron
# simu = SimuladorGeneral()

print("")
print("- hasta aqui todo bien - ")

print()
print("Sigue usar el eeg emotiv")

# eeg = EegGeneral()

CentroControlEegSimulador()

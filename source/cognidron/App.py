"""
Aplicaciòn principal del Cognidron. Aquí inicia todo.
"""
from interfaces.simulador.simudrouAdapter import SimudrouAdapter
from main.centroControlEegSimulador import CentroControlEegSimulador

print("Inciando Cognidron v0.01")


# Verificar que existan todos los modulos


print("")
print("- hasta aqui todo bien - ")

# Test de comunicación con el simulador


CentroControlEegSimulador()

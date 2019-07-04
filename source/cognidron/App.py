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
simulador = SimudrouAdapter()
simulador.iniciarConexion()
i = 0
while i < 100:
    simulador.enviarMensaje("que ondas!")
    i += 1
simulador.cerrarConexion()
# CentroControlEegSimulador()

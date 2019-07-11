import json
import time
from interfaces.nf.emotivNFAdapter import EmotivNFAdapter
from interfaces.simulador.simudrouAdapter import SimudrouAdapter

"""
Clase que utiliza y controla el NF.
"""

nf = EmotivNFAdapter()
simu = SimudrouAdapter()

simu.iniciarConexion()
nf.startConnection()

nf.receivePow()
nf.receivePow()
nf.receivePow()
nf.receivePow()

# Comenzamos con la intercomunicación
go = True
while go:

    result = nf.receivePow()

    """
    Indicaciones:
    Para usar el Theta Beta Ratio con emotiv epoc +:
     - Usar de ratio a Theta/Betha Low
     - Promediar los valores de F3 y F4, debido a no tener CZ ni FCZ
    """

    # Promediamos los valores theta de F3 y F4
    thetaMean = (result["F3/theta"] + result["F4/theta"]) / 2
    betaMean = (result["F3/betaL"] + result["F4/betaL"]) / 2

    # Obtenemos el ratio
    tbr = thetaMean/betaMean

    # Imprimimos resultados
    print("////////////////////////////////////////////////////")
    print("theta: " + str(thetaMean))
    print("       ------------")
    print("beta:  " + str(betaMean))
    print("tbr = " + str(tbr))
    print()

    simu.enviarMensaje("theta:" + str(thetaMean))
    time.sleep(0.050)  # 8 hz
    simu.enviarMensaje("beta:" + str(betaMean))
    time.sleep(0.050)  # 8 hz



# Al final
nf.closeConnection()
simu.cerrarConexion()
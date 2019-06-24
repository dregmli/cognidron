from interfaces.eeg.emotivAdapter import EmotivAdapter
from interfaces.simulador.simdrouAdapter import SimdrouAdapter
import json
import time

class CentroControlEegSimulador:
    """
    Clase para llevar la comunicación entre el simulador y el dispositivo EEG, usando los comandos mentales.
    """

    def __init__(self):
        eeg = EmotivAdapter()
        eeg.iniciarConexion()

        simu = SimdrouAdapter()
        simu.iniciarConexion()

        # Comenzamos con la intercomunicación
        go = True
        while go:
            comando = ""
            intensidad = 0.0
            result = eeg.recibirMensaje()
            dic = json.loads(result)

            if 'com' in result:  # asegurar que se reciba un comando mental
                comando = dic["com"][0]
                intensidad = dic["com"][1]
                print("comando:::: ", comando)
                print("intensidad: ", intensidad)
                simu.enviarMensaje(comando + ":" + str(intensidad))

            time.sleep(0.125)  # 8 hz

        # Al final
        eeg.cerrarConexion()
        simu.cerrarConexion()



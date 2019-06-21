from interfaces_esp.eeg.emotivAdapter import EmotivAdapter


class EegGeneral:
    """
    Clase de la Interfaz General del EEG que utiliza la clase Adaptador de algun dispositivo EEG.

    En este caso se está usando el EEG: Emotiv Epoc + con el API Cortex v2.0

    Fecha: Jueves 20 de Junio 2019
    Autor: dregmli
    """

    def __init__(self):
        print("Eeg: Iniciando instancia del EegGeneral")

        # Prueba 1 del emotivAdapter
        eeg = EmotivAdapter()
        eeg.iniciarConexion()
        #eeg.iniciarSesion()
        result = eeg.recibirMensaje()
        print("Recibido del eeg: " + result)
        result = eeg.recibirMensaje()
        print("Recibido del eeg: " + result)
        result = eeg.recibirMensaje()
        print("Recibido del eeg: " + result)
        result = eeg.recibirMensaje()
        print("Recibido del eeg: " + result)
        result = eeg.recibirMensaje()
        print("Recibido del eeg: " + result)


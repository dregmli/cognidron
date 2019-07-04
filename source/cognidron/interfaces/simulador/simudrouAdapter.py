"""
Interfaz especifica que sirve como adapatador para realizar conexión de cognidron con el simulador de drones en Unity 3D llamado "SimdroU" (simulador dron unity)
"""
from interfaces_esp.simulador.simuladorInterfaz import SimuladorInterfaz


import zmq


class SimudrouAdapter(SimuladorInterfaz):

    protocol = "tcp"
    port = "5555"
    ip = "*"
    url = "%s://%s:%s" %(protocol, ip, port)  # example: "tcp://*:5555

    context = None
    socket = None
    # conectado = False

    # esta conexión usando ZMQ con unity tiene una peculiaridad, que se debe recibir mensaje paara poder enviar uno.
    recibido = False


    def decirHola(self):
        print("Que ondas brothersss!!!")


    def iniciarConexion(self):
        print("Inciando servidor de sockets en " + self.url)
        try:
            self.context = zmq.Context()
            self.socket = self.context.socket(zmq.REP)
            self.socket.bind(self.url)
            self.conectado = True
        except:
            self.conectado = False
            print("Error!!: al iniciar el servidor de socket en " + self.url)




    def cerrarConexion(self):
        self.conectado = False
        # al parecer el socket de ZMQ no tiene método de cerrar

    def recibirMensaje(self):
        if self.conectado:

            if self.recibido:  # si no se ha enviado un mensaje antes, se envia uno vacio
                self.enviarMensaje("vacio")

            mensaje = self.socket.recv()
            print("Received request: %s" % mensaje)
            mensaje = str(mensaje)  # no se exactamente que recibo pero lo convierto a string para manipularlo
            mensaje = mensaje[2:-1] # se reciben mensajes como b'hola' y hay que recortar a hola
            print("Received request: %s" % mensaje)
            self.recibido = True
            return mensaje
        else:
            print("Error!! al recibir mensaje: No hay servidor establecido previamente")
            message = ""
            return message


    def enviarMensaje(self, mensaje):
        if self.conectado:
            if not self.recibido:  # Si no se ha recibido un mensaje previamente, se recibe
                self.recibirMensaje()
            print("simdrou: >> enviando: " + mensaje)
            self.socket.send(bytes(mensaje, 'utf-8'))
            self.recibido = False
        else:
            print("Error!! al enviar mensaje: No hay servidor establecido previamente")

    def prueba(self):

        # Primero establecer la conexión
        self.iniciarConexion()

        # Esperar recibir el mensaje
        self.recibirMensaje()
        # Despues se puede enviar un mensaje
        self.enviarMensaje("Hola mundo 01")

        self.recibirMensaje()
        self.enviarMensaje("Hola mundo 02")

        self.recibirMensaje()
        self.enviarMensaje("Hola mundo 03")

        self.recibirMensaje()
        self.enviarMensaje("Hola mundo 04")

        print("--------------------")

        self.enviarMensaje("vientos")
        self.enviarMensaje("huracanados")
        self.enviarMensaje("geniales")
        self.enviarMensaje("y frescos")

        self.recibirMensaje()
        self.recibirMensaje()
        self.recibirMensaje()
        self.recibirMensaje()

        # Por ultimo, cerrar conexión
        self.cerrarConexion()
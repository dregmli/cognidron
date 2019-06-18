"""
Interfaz especifica que sirve como adapatador para realizar conexión de cognidron con el simulador de drones en Unity 3D llamado "SimdroU" (simulador dron unity)
"""
from interfaces_esp.simulador.simuladorInterfaz import SimuladorInterfaz


import zmq


class SimdrouAdapter(SimuladorInterfaz):

    protocol = "tcp"
    port = "5555"
    ip = "*"
    url = "%s://%s:%s" %(protocol, ip, port)  # example: "tcp://*:5555

    context = None
    socket = None

    def decirHola(self):
        print("Que ondas brothersss!!!")


    def iniciarConexion(self):
        print("Inciando servidor de sockets en " + self.url)
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)
        self.socket.bind(self.url)


    def cerrarConexion(self):
        pass  # al parecer el socket de ZMQ no tiene método de cerrar

    def recibirMensaje(self):
        message = self.socket.recv()
        print("Received request: %s" % message)
        return message

    def enviarMensaje(self, message):
        self.socket.send(bytes(message, 'utf-8'))

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

        # Por ultimo, cerrar conexión
        self.cerrarConexion()
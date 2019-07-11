


from websocket import create_connection
import json
import time
import ssl

from interfaces.nf.nfInterface import NFInterface


class EmotivNFAdapter(NFInterface):
    """
    Clase para conectar Cognidron con el headset de Emotiv implementando el API de Emotiv Cortex V2.0
    y utilizar las bandas para Neurofeedback TBR.

    Fecha: Jueves 11 Juliso 2019
    Author: dregmli

    Basado en la clase EmotivAdapater, con modificaciones para usarlo solo con las bandas de frecuencia.

    """



    # PENDIENTE: que obtenga la informacion de clientID y clientSecret desde un archivo de txt

    # - - - - - - - - - - - - - - - - -
    # Nesesarias definiarlas previamente
    clientId = "3nQdijGriE91rx1CPFvdQiDUrHpN1Ore2tXonEE2"
    clientSecret = "mm25AgYCqSvGQd8Onrz7uX4tSWO3zY6RLGo66oEomO3ubRH00lhs7EyhGTr1cAqY7nuATvDFAfuZFQyRymFyP0knjVtzlZXVAmsJrp5nShr9p1NCcqoNIURJ553k7bAK"
    profile = "j3"
    # - - - - - - - - - - - - - - - - -

    # Estas las define el programa por si solas
    answer = ""
    token = None
    headset = ""
    sesion = ""
    lstCanales = None

    ws = None

    URLwebsocket = "wss://localhost:6868"  # anteriormente en Cortex v1.x era wss://emotivcortex.com:54321




    def startConnection(self):
        """
        Iniciar la conexión por websocket a Cortex v2.0
        :return: nothing.
        """
        print("Iniciando conexión de websocket client a " + self.URLwebsocket)
        try:
            self.ws = create_connection(self.URLwebsocket, sslopt={"cert_reqs": ssl.CERT_NONE})
            self.connected = True  # Importante que vaya aqui, para que pueda funconar iniciarSesion()
            self.__startSession()
        except:
            self.connected = False
            print("Error!!: al conectarse como websocket client a " + self.URLwebsocket)


    def closeConnection(self):
        self.__closeSession()
        self.ws.close()
        self.connected = False
        print("Conexión de websocket con Emotiv Cortex cerrada.")

    def send(self, message):
        if self.connected:
            print(": ----------------------------------------------------------------------")
            print("Enviando mensaje a Cortex: ")
            print(message)
            self.ws.send(message)
            print("Recibiendo de Cortex...")
            result = self.ws.recv()
            print("Recibido: '%s'" % result)
            return result
        else:
            print("Error!! al enviar mensaje a Cortex: no ha iniciado conexión")
            return ""

    def receive(self):
        if self.connected:
            result = self.ws.recv()
            return result
        else:
            print("Error!! recibiendo mensaje de Cortex: no ha iniciado conexión")


    # ------------------------------------------------------------------------------
    # Métodos particulares para el Emotiv Cortex V2.0


    def __startSession(self):
        """
        Se realizan todos los pasos necesarios para iniciar la sesión con Cortex v2.0
        :return:
        """

        # RequestAccess: solicitar permiso al usuario por medio de Emotiv App
        print("Cortex: Hacer RequestAccess: ")
        message = """{
                        "id": 1,
                        "jsonrpc": "2.0",
                        "method": "requestAccess",
                        "params": {
                            "clientId": "%s",
                            "clientSecret": "%s"
                        }
                    }""" % (self.clientId, self.clientSecret)
        self.send(message)


        # Autorización
        message = """{
                        "id": 1,
                        "jsonrpc": "2.0",
                        "method": "authorize",
                        "params": {
                            "clientId": "%s",
                            "clientSecret": "%s"
                        }
                    }""" % (self.clientId, self.clientSecret)
        answer = self.send(message)
        dic = json.loads(answer)
        self.token = dic["result"]["cortexToken"]
        print("@@@@@@@@@@@@@@@@@@@@")
        print(dic)
        print("token es: ", self.token)


        # Saber si existen headsets conectados
        print("\n>> Headsets disponibles: ")
        message = """{"jsonrpc": "2.0", 
                        "method": "queryHeadsets",
                        "params": {},
                        "id": 1
                    }"""
        answer = self.send(message)
        dic = json.loads(answer)
        if 'dongle' in answer:
            self.headset = dic["result"][0]["id"]  # Obtener el ID del headset
            print("id del headset: ", self.headset)
        else:
            print("Error: No hay ningun headset disponible")
            self.closeConnection()


        # Conectarse con el headset con controlDevice
        print(">> Conectarse con el headset: ")
        message = """{
                        "id": 1,
                        "jsonrpc": "2.0",
                        "method": "controlDevice",
                        "params": {
                            "command": "connect",
                            "headset": "%s"
                        }
                    }""" % self.headset
        self.send(message)


        # Iniciar la sesión
        print(">> Iniciando la sesión")
        message = """{
                        "id": 1,
                        "jsonrpc": "2.0",
                        "method": "createSession",
                        "params": {
                            "cortexToken": "%s",
                            "headset": "%s",
                            "status": "open"
                        }
                    }""" % (self.token, self.headset)
        answer = self.send(message)

        if 'appId' in answer:
            dic = json.loads(answer)
            self.sesion = dic['result']['id']
        else:
            print("Error: Problemas al iniciar sesión con el dispositivo en Cortex")
            self.closeConnection()
        print('sesion : ', self.sesion)





        # Suscribirse a bandas del potencial de frecuencias
        print(">> Suscribirse")
        message = """{
                        "id": 1,
                        "jsonrpc": "2.0",
                        "method": "subscribe",
                        "params": {
                            "cortexToken": "%s",
                            "session": "%s",
                            "streams": ["pow"]
                        }
                    }""" % (self.token, self.sesion)
        answer = self.send(message)


        # Primero hay que obtener la lista de las columnas de canales
        print(">> obtener lista de canales")
        if 'pow' in answer:
            print(">> va todo bien")
            dic = json.loads(answer)
            self.lstCanales = dic['result']['success'][0]['cols']
            print("CANALES: " + self.lstCanales[0])
        else:
            print("Error: Problemas al iniciar suspcripción con el dispositivo en Cortex")
            self.closeConnection()




    def receivePow(self):
        """
        Recibe los valores de potencial de las bandas de frecuencia del emotiv epoc
        :return: un diccionario con el nombre de cada canal/banda y su valor en potencial
        """

        answer = self.receive()
        if self.lstCanales is not None:
            dic = json.loads(answer)
            lstValues = dic["pow"]
            # Combinar lista columnas de cada canal con sus respectivos valores
            bands = dict(zip(self.lstCanales, lstValues))
            print("test bands AF3/theta = " + str(bands['AF3/theta']))
            return bands


    # Cerrar sesion
    def __closeSession(self):
        if self.sesion != "":
            print(">> Cerrando sesión...: ")
            message = """{
                            "id": 1,
                            "jsonrpc": "2.0",
                            "method": "updateSession",
                            "params": {
                                "cortexToken": "%s",
                                "session": "%s",
                                "status": "close"
                            }
                        }""" % (self.token, self.sesion)
            self.send(message)





"""
Clase para conectar Cognidron con el headset de Emotiv implementando el API de Emotiv Cortex V2.0

Fecha: Miércoles 19 de Junio 2019
Author: dregmli

Basado en los modulos experimentales "control dron virtual.py" y otros del paquete "cognidron.experimentos.websocket_client"

Para realizar la conexión con Emotiv Cortex v2.0 se usan websockets.
"""


from websocket import create_connection
import json
import time
import ssl

from interfaces_esp.eeg.eegInterfaz import EegInterfaz


class EmotivAdapter(EegInterfaz):



    # conectado = False

    # PENDIENTE: que obtenga la informacion de clientID y clientSecret desde un archivo de txt

    clientId = ""
    clientSecret = ""
    answer = ""
    token = None
    headset = ""
    sesion = ""
    profile = "gogo"
    ws = None

    URLwebsocket = "wss://localhost:6868"  # anteriormente en Cortex v1.x era wss://emotivcortex.com:54321




    def iniciarConexion(self):
        print("Iniciando conexión de websocket client a " + self.URLwebsocket)
        try:
            self.ws = create_connection(self.URLwebsocket, sslopt={"cert_reqs": ssl.CERT_NONE})
            self.conectado = True
        except:
            self.conectado = False
            print("Error!!: al conectarse como websocket client a " + self.URLwebsocket)


    def cerrarConexion(self):
        self.__cerrarSesion()
        self.ws.close()
        self.conectado = False
        print("Conexión de websocket con Emotiv Cortex cerrada.")

    def enviarMensaje(self, mensaje):
        if self.conectado:
            print(": ----------------------------------------------------------------------")
            print("Enviando mensaje a Cortex: ")
            print(mensaje)
            self.ws.send(mensaje)
            print("Recibiendo de Cortex...")
            result = self.ws.recv()
            print("Recibido: '%s'" % result)
            return result
        else:
            print("Error!! al enviar mensaje a Cortex: no ha iniciado conexión")
            return ""

    def recibirMensaje(self):
        if self.conectado:
            result = self.ws.recv()
            return result
        else:
            print("Error!! recibiendo mensaje de Cortex: no ha iniciado conexión")


    # ------------------------------------------------------------------------------
    # Métodos particulares para el Emotiv Cortex V2.0


    def iniciarSesion(self):
        """
        Se realizan todos los pasos necesarios para iniciar la sesión con Cortex v2.0
        :return:
        """

        # RequestAccess: solicitar permiso al usuario por medio de Emotiv App
        print("Cortex: Hacer RequestAccess: ")
        mensaje = """{
                        "id": 1,
                        "jsonrpc": "2.0",
                        "method": "requestAccess",
                        "params": {
                            "clientId": "%s",
                            "clientSecret": "%s"
                        }
                    }""" % (self.clientId, self.clientSecret)
        self.enviarMensaje(mensaje)


        # Autorización
        mensaje = """{
                        "id": 1,
                        "jsonrpc": "2.0",
                        "method": "authorize",
                        "params": {
                            "clientId": "%s",
                            "clientSecret": "%s"
                        }
                    }""" % (self.clientId, self.clientSecret)
        answer = self.enviarMensaje(mensaje)
        dic = json.loads(answer)
        self.token = dic["result"]["cortexToken"]
        print("@@@@@@@@@@@@@@@@@@@@")
        print(dic)
        print("token es: ", self.token)


        # Saber si existen headsets conectados
        print("\n>> Headsets disponibles: ")
        mensaje = """{"jsonrpc": "2.0", 
                        "method": "queryHeadsets",
                        "params": {},
                        "id": 1
                    }"""
        answer = self.enviarMensaje(mensaje)
        dic = json.loads(answer)
        if 'dongle' in answer:
            self.headset = dic["result"][0]["id"]  # Obtener el ID del headset
            print("id del headset: ", self.headset)
        else:
            print("Error: No hay ningun headset disponible")
            self.cerrarConexion()


        # Conectarse con el headset con controlDevice
        print(">> Conectarse con el headset: ")
        mensaje = """{
                        "id": 1,
                        "jsonrpc": "2.0",
                        "method": "controlDevice",
                        "params": {
                            "command": "connect",
                            "headset": "%s"
                        }
                    }""" % self. headset
        self.enviarMensaje(mensaje)


        # Iniciar la sesión
        print(">> Iniciando la sesión")
        mensaje = """{
                        "id": 1,
                        "jsonrpc": "2.0",
                        "method": "createSession",
                        "params": {
                            "cortexToken": "%s",
                            "headset": "%s",
                            "status": "open"
                        }
                    }""" % (self.token, self.headset)
        answer = self.enviarMensaje(mensaje)

        if 'appId' in answer:
            dic = json.loads(answer)
            sesion = dic['result']['id']
        else:
            print("Error: Problemas al iniciar sesión con el dispositivo en Cortex")
            self.cerrarConexion()
        print('sesion : ', sesion)


        # Cargar un perfil para comenados mentales
        print(">> Cargar perfil")
        mensaje = """{
                        "id": 1,
                        "jsonrpc": "2.0",
                        "method": "setupProfile",
                        "params": {
                            "cortexToken": "%s",
                            "headset": "%s",
                            "profile": "%s",
                            "status": "load"
                        }
                    }""" % (self.token, self.headset, self.profile)
        answer = self.enviarMensaje(mensaje)


        # Suscribirse a comandos mentales y faciales
        print(">> Suscribirse")
        mensaje = """{
                        "id": 1,
                        "jsonrpc": "2.0",
                        "method": "subscribe",
                        "params": {
                            "cortexToken": "%s",
                            "session": "%s",
                            "streams": ["com"]
                        }
                    }""" % (self.token, self.sesion)
        answer = self.enviarMensaje(mensaje)




    # Cerrar sesion
    def __cerrarSesion(self):
        if self.sesion != "":
            print(">> Cerrando sesión...: ")
            mensaje = """{
                            "id": 1,
                            "jsonrpc": "2.0",
                            "method": "updateSession",
                            "params": {
                                "cortexToken": "%s",
                                "session": "%s",
                                "status": "close"
                            }
                        }""" % (self.token, self.sesion)
            self.enviarMensaje(mensaje)





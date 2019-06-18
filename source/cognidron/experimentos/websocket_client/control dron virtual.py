""" Se siguen los pasos para establecer conexion con el emotiv app en mac os x
    Usando Cortex v2.0

    Hacer de servidor para enviar los comandos mentales a unity por sockets y mover el dron

    Actualziación: 11 de junio 2019
"""

from websocket import create_connection
import ssl
import json
import time
import zmq


clientId = "3nQdijGriE91rx1CPFvdQiDUrHpN1Ore2tXonEE2"
clientSecret = "mm25AgYCqSvGQd8Onrz7uX4tSWO3zY6RLGo66oEomO3ubRH00lhs7EyhGTr1cAqY7nuATvDFAfuZFQyRymFyP0knjVtzlZXVAmsJrp5nShr9p1NCcqoNIURJ553k7bAK"
answer = ""
token = None
headset = ""
sesion = ""
profile = "nay"

URLwebsocket = "wss://localhost:6868"  # anteriormente era wss://emotivcortex.com:54321


print("Comenzando...")

# 1. Conectarse con el websocket del emotiv app cortex
print("1. Estableciendo conexión con websocket", URLwebsocket)
ws = create_connection(URLwebsocket, sslopt={"cert_reqs": ssl.CERT_NONE})


# Función para mandar mensajes string JSon al Emotiv Cortex
def ejecutar(txt):
    global conteo
    conteo =+ 1
    print(": ----------------------------------------------------------------------")
    print("Sending mensaje: ")
    print(txt)
    ws.send(txt)
    print("Sent")
    print("Receiving...")
    result =  ws.recv()
    print("Received '%s'" % result)
    return result

# Cerrar sesion
def cerrarSesion():
    if sesion != "":
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
                    }""" % (token, sesion)
        ejecutar(mensaje)


# Para finalizar el programa desde un punto determinado
def terminar():
    #cerrarSesion()
    # Y al final, cerrar la conexión
    ws.close()
    print("Finalizando aplicación")
    exit()



# 2. RequestAccess: solicitar permiso al usrio por medio de Emotiv App
print("2. Hacer RequestAccess: ")
mensaje = """{
                "id": 1,
                "jsonrpc": "2.0",
                "method": "requestAccess",
                "params": {
                    "clientId": "%s",
                    "clientSecret": "%s"
                }
            }""" % (clientId, clientSecret)
ejecutar(mensaje)











# Autorización+
mensaje = """{
                "id": 1,
                "jsonrpc": "2.0",
                "method": "authorize",
                "params": {
                    "clientId": "%s",
                    "clientSecret": "%s"
                }
            }""" % (clientId, clientSecret)
answer = ejecutar(mensaje)
dic = json.loads(answer)
token = dic["result"]["cortexToken"]
print("@@@@@@@@@@@@@@@@@@@@")
print(dic)
print("token es: ", token)


# . Saber si existen headsets conectados
print("\n>> Headsets disponibles: ")
mensaje = """{"jsonrpc": "2.0", 
                "method": "queryHeadsets",
                "params": {},
                "id": 1
            }"""
answer = ejecutar(mensaje)
dic = json.loads(answer)
if 'dongle' in answer:
    headset = dic["result"][0]["id"]
    print("id del headset: ", headset)
else:
    print("Error: No hay ningun headset disponible")
    terminar()


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
            }""" % headset
ejecutar(mensaje)


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
            }""" % (token, headset)
answer = ejecutar(mensaje)

if 'appId' in answer:
    dic = json.loads(answer)
    sesion = dic['result']['id']
else:
    print("Error: Problemas al iiciar sesión con el dispositivo")
    terminar()
print('sesion : ', sesion )


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
            }""" % (token, headset, profile)
answer = ejecutar(mensaje)


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
            }""" % (token, sesion)
answer = ejecutar(mensaje)




# ----------------------------------------------
# conectarse con unity

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
j = 0




result = ws.recv()
print("Received '%s'" % result)
i = 0
while i < 10000:
    answer = ws.recv()
    print("Received '%s'" % result)

    dic = json.loads(answer)
    comando = ""
    intensidad = 0.0

    if 'com' in answer:  # asegurar que se reciba un comando mental
        comando = dic["com"][0]
        intensidad = dic["com"][1]

        print("comando:::: ", comando)
        print("intensidad: ", intensidad)


        # -------------------------------------------------------
        #  Wait for next request from client Unity
        message = socket.recv()
        print("Received request: %s" % message)
        socket.send(bytes(comando, 'utf-8'))


    i += 1
    time.sleep(0.125)  # 8 hz



terminar()



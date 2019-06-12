""" Se siguen los pasos para establecer conexion con el emotiv app en mac os x
    Usando Cortex v2.0

    Actualziación: 11 de junio 2019
"""

from websocket import create_connection
import ssl
import json


clientId = ""
clientSecret = ""
answer = ""
token = None
headset = ""

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

# Para finalizar el programa desde un punto determinado
def terminar():
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


# conectarse con el headset con controlDevice
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






terminar()



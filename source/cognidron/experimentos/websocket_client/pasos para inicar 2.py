""" Se siguen los pasos para establecer conexion con el emotiv app en mac os x
    Esta vez, usando el login por codigo en lugar de usar el Cortex GUI

    Fecha: 6 de junio 2019
"""

from websocket import create_connection
import ssl
import json



URLwebsocket = "wss://localhost:6868"  # anteriormente era wss://emotivcortex.com:54321


print("Comenzando...")

# 1. Conectarse con el websocket del emotiv app cortex
print("1. Estableciendo conexión con websocket", URLwebsocket)
ws = create_connection("wss://localhost:6868", sslopt={"cert_reqs": ssl.CERT_NONE})


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


# 2. Saber si existen headsets conectados
print("2. hHeadsets conectados: ")
# mensaje = ' {"jsonrpc": "2.0", "method": "queryHeadsets","params": {},"id": 1} '
mensaje = """{"jsonrpc": "2.0", 
                "method": "queryHeadsets",
                "params": {},
                "id": 1
            }"""
ejecutar(mensaje)


mensaje = """{
    "jsonrpc": "2.0",
    "method": "getUserLogin",
    "id": 1
  }"""
ejecutar(mensaje)



# 3. Login
print("3. Login to emotiv cloud")
mensaje = """{
    "jsonrpc": "2.0",
    "method": "login",
    "params": {
      "username": "",
      "password": "",
      "client_id": "",
      "client_secret": ""
    },
    "id": 1
  }"""


ejecutar(mensaje)







print("Como se llama")
# nombre = input()
# print("Hola", nombre)


# Y al final, cerrar la conexión
ws.close()


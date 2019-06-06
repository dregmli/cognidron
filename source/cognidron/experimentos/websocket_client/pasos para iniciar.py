""" 
# https://emotiv.github.io/cortex-docs/#how-to-get-data-from-cortex

Step 1: 
You need to make sure your headset connected with Cortex by the way call query headset

Step 2:
Call method create session with that headset.

Step 3:
Subscribe stream type which you want to get

"""



from websocket import create_connection
import ssl
import json


conteo = 0
mensaje = ""

#conectamos el WS
#ws = create_connection("wss://emotivcortex.com:54321", sslopt={"cert_reqs": ssl.CERT_NONE})
ws = create_connection("wss://localhost:6868", sslopt={"cert_reqs": ssl.CERT_NONE})

def principal():
    #ws = create_connection("wss://emotivcortex.com:54321") #ws://echo.websocket.org/
    #1.
    mensaje = ' {"jsonrpc": "2.0", "method": "queryHeadsets","params": {},"id": 1} '
    ejecutar(mensaje)


    mensaje = '{"jsonrpc": "2.0","method": "authorize","params": {}, "id": 1 }'
    jsonData = ejecutar(mensaje)

    JsonToPython = json.loads(jsonData)



    #2. 
    mensaje = ' {"jsonrpc": "2.0", "method": "createSession", "params": {"_auth": "' + JsonToPython['result']['_auth'] + '","status": "open", "title": "prueba1"}, "id": 1}'
    ejecutar(mensaje)
    

    #3
    mensaje = '{"jsonrpc": "2.0","method": "subscribe","params": {"_auth": "' + JsonToPython['result']['_auth'] + '","streams": ["pow"]},"id": 1}'
    ejecutar(mensaje)



    result =  ws.recv()
    print("Received '%s'" % result)
    print("")
    result =  ws.recv()
    print("Received '%s'" % result)
    print("")
    result =  ws.recv()
    print("Received '%s'" % result)
    print("")
    result =  ws.recv()
    print("Received '%s'" % result)
    print("")
    result =  ws.recv()
    print("Received '%s'" % result)
    print("")
    result =  ws.recv()
    print("Received '%s'" % result)
    print("")
    result =  ws.recv()
    print("Received '%s'" % result)
    print("")
    result =  ws.recv()
    print("Received '%s'" % result)

    ws.close()

    return 0




def ejecutar(txt):
    global conteo
    conteo =+ 1
    print(str(conteo) + ": ----------------------------------------------------------------------")
    print("Sending mensaje: ")
    print(txt)
    ws.send(txt)
    print("Sent")
    print("Receiving...")
    result =  ws.recv()
    print("Received '%s'" % result)
    return result


#y ahora si ejecutamos las funciones
principal()
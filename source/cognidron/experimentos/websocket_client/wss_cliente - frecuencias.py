#info obtenida de https://pypi.org/project/websocket_client/

from websocket import create_connection
import ssl
#ws = create_connection("wss://emotivcortex.com:54321") #ws://echo.websocket.org/

"""ws = create_connection("wss://emotivcortex.com:54321",
  sslopt={"cert_reqs": ssl.CERT_NONE})"""

ws = create_connection("wss://localhost:6868",
  sslopt={"cert_reqs": ssl.CERT_NONE})


#mensaje = ' {"jsonrpc": "2.0", "method": "queryHeadsets","params": {},"id": 1} '
mensaje = '{"jsonrpc": "2.0", "method": "hello","params": {"hello": "world"},"id": 1}'

print("Sending mensaje: ")
print(mensaje)
ws.send(mensaje)
print("Sent")
print("Receiving...")
result =  ws.recv()
print("Received '%s'" % result)
ws.close()
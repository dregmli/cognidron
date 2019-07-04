using AsyncIO;
using NetMQ;
using NetMQ.Sockets;
using UnityEngine;

/// <summary>
///     Example of requester who only sends Hello. Very nice guy.
///     You can copy this class and modify Run() to suits your needs.
///     To use this class, you just instantiate, call Start() when you want to start and Stop() when you want to stop.
/// </summary>
public class HelloRequester2 : RunAbleThread
{

public string comando = "";
public float intensidad = 0;
    /// <summary>
    ///     Request Hello message to server and receive message back. Do it 10 times.
    ///     Stop requesting when Running=false.
    /// </summary>
    protected override void Run()
    {
        ForceDotNet.Force(); // this line is needed to prevent unity freeze after one use, not sure why yet
        using (RequestSocket client = new RequestSocket())
        {
            client.Connect("tcp://localhost:5555");
            

            for (int i = 0; i < 10000 && Running; i++)
            {
                Debug.Log("Sending Hello");
                client.SendFrame("Hello");

                // ReceiveFrameString() blocks the thread until you receive the string, but TryReceiveFrameString()
                // do not block the thread, you can try commenting one and see what the other does, try to reason why
                // unity freezes when you use ReceiveFrameString() and play and stop the scene without running the server
//                string message = client.ReceiveFrameString();
//                Debug.Log("Received: " + message);
                string message = null;
                string stringIntensidad = "";
                bool gotMessage = false;
                int indice = 0;
                while (Running)
                {
                    gotMessage = client.TryReceiveFrameString(out message); // this returns true if it's successful
                    if (gotMessage) {
                        if (message != null && message.Contains(":")) { 
                            //Debug.Log("recibido:: " + message);
                            indice = message.LastIndexOf(":");
                            comando = message.Substring(0,indice); //obtenermos el primer substring, que es el comando mental
                            stringIntensidad = message.Substring(indice+1); //obtnemos el segundo substring, la intensidad del comando
                            intensidad = float.Parse(stringIntensidad, System.Globalization.CultureInfo.InvariantCulture); //lo convertimos a float
                            //System.Globalization.CultureInfo.InvariantCulture se usa porque el string usa '.' en lugar de ',' para separar las decimales
                        }
                        break;
                    }
                }

                //ESTOLOCOMENTE     if (gotMessage) Debug.Log("Received " + message);
            }
        }

        NetMQConfig.Cleanup(); // this line is needed to prevent unity freeze after one use, not sure why yet
    }
}
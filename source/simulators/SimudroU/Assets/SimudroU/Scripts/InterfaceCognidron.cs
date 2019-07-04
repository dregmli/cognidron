using AsyncIO;
using NetMQ;
using NetMQ.Sockets;
using UnityEngine;

/// <summary>
///     Clase que genera un hilo para comunicarse constantemente mediante sockets NetMQ a Cognidron
/// </summary>
public class InterfaceCognidron : RunAbleThread
{
    public string mensaje = "";

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
                bool gotMessage = false;
                int indice = 0;
                while (Running)
                {
                    gotMessage = client.TryReceiveFrameString(out message); // this returns true if it's successful
                    if (gotMessage)
                    {
                        if (message != null && message != "")
                        {
                             mensaje = message;
                        }
                        break;
                    }
                }

                //ESTOLOCOMENTE     if (gotMessage) Debug.Log("Received " + message);
            }
        }

        NetMQConfig.Cleanup(); // this line is needed to prevent unity freeze after one use, not sure why yet
    }

    public void pruebaHolaMundo() {
        Debug.Log("ejecutando un metdo de un hilo que esta en run?? O.o");
    }
}
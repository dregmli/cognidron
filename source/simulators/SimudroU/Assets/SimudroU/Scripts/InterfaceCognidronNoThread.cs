using System.Collections;
using System.Collections.Generic;
using AsyncIO;
using NetMQ;
using NetMQ.Sockets;
using UnityEngine;

public class InterfaceCognidronNoThread
{
	private RequestSocket client;


	public InterfaceCognidronNoThread() 
    {

		// Establecer la conexión del socket
		ForceDotNet.Force(); // this line is needed to prevent unity freeze after one use, not sure why yet
		using (client = new RequestSocket())
		{
			client.Connect("tcp://localhost:5555");

		}

		
	}


	public void send(string message)
	{
		Debug.Log("Sending message: " + message);
		client.SendFrame("Hello");

		// ReceiveFrameString() blocks the thread until you receive the string, but TryReceiveFrameString()
		// do not block the thread, you can try commenting one and see what the other does, try to reason why
		// unity freezes when you use ReceiveFrameString() and play and stop the scene without running the server
		//                string message = client.ReceiveFrameString();
		//                Debug.Log("Received: " + message);
		string response = null;
		bool gotMessage = false;

		gotMessage = client.TryReceiveFrameString(out response); // this returns true if it's successful
		if (gotMessage)
		{
			if (response != null && response != "")
			{
				Debug.Log("respuesta: " + response);
			}
		}
		

	}

    // Destructor
    /*
	~InterfaceCognidronNoThread()
	{
		Debug.Log("Destruyendo objeto interfazcognidronNoHilo");
		NetMQConfig.Cleanup(); // this line is needed to prevent unity freeze after one use, not sure why yet
	} */
}

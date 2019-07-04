using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MainTrainingBasic : MonoBehaviour
{
    InterfaceCognidron ic;
    void Start()
    {
        ic = new InterfaceCognidron();
        ic.Start();

        
    }

    void Update()
    {
        Debug.Log("Receivedo de cognidron: " + ic.mensaje);

        // Falta diseñar la parte de recibir mensajes y comenzar tipo de entrenamiento de comandos mentales.
        // Por lo pronto es un test

        if (ic.mensaje.Contains("startTraining")) {
            //ic.enviarMensaje("");
        }
        ic.pruebaHolaMundo();
    }
}

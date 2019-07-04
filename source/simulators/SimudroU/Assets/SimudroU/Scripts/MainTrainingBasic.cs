using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MainTrainingBasic : MonoBehaviour
{
    InterfaceCognidron ic;
    void Start()
    {
        // ic = new InterfaceCognidron();
        ic = new InterfaceCognidron();
        ic.Start();

        
        // ic.send("Enviadno respuesta desde NO hilo 2");
    }

    void Update()
    {
        // Debug.Log("Receivedo de cognidron: " + ic.mensaje);

        // Falta diseñar la parte de recibir mensajes y comenzar tipo de entrenamiento de comandos mentales.
        // Por lo pronto es un test

        ic.send("Enviadno respuesta desde NO hilo");
    }
}

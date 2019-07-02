using System.Collections;
using System.Collections.Generic;
using UnityEngine;

/**
 * Esta clase implementa un PID (controlador proporcional integral derivativo) para estabilizar el movimiento del dron. 
 */
public class DronePID : MonoBehaviour
{
    
    private PID pidx = new PID(0.1f, 0.1f, 0f); 
    public PID pidy = new PID(0.1f, 0.1f, 0f); // por default: 0.1, 0.1, y 0
    private PID pidz = new PID(0.1f, 0.1f, 0f);

    public Transform transGuide; // Objeto vacio que sirve como guía hacía donde mover el drone
    private Transform transDrone;  // Para aplicar fuerzas al drone.

    private Vector3 v;
    
    void Start()
    {
        transDrone = GetComponent<Transform>();
        v = new Vector3(transGuide.position.x, transGuide.position.y, transGuide.position.z);
    }


    void Update()
    {
        
    }


    private void FixedUpdate()
    {
        //transDrone.Translate(0, pid.Update(transGuide.position.y, transDrone.position.y, Time.deltaTime), 0);

        /*
         * Esto actualiza la posicion del Dron en x,y,z siguiendo la posición del objeto Guia, usando un PID para estabilizar la posición de cada eje.
         */
        v.x = pidx.Update(transGuide.position.x, transDrone.position.x, Time.deltaTime);
        v.y = pidy.Update(transGuide.position.y, transDrone.position.y, Time.deltaTime);
        v.z = pidz.Update(transGuide.position.z, transDrone.position.z, Time.deltaTime);

        transDrone.Translate(v);

    }

}

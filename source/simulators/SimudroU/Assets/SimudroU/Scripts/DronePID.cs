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

    public Transform guide; // Objeto vacio que sirve como guía hacía donde mover el drone
    private Transform drone;  // Para aplicar fuerzas al drone.

    private Vector3 v;
    
    void Start()
    {
        drone = GetComponent<Transform>();
        v = new Vector3(guide.position.x, guide.position.y, guide.position.z);
    }


    void Update()
    {
        
    }


    private void FixedUpdate()
    {
        //drone.Translate(0, pid.Update(guide.position.y, drone.position.y, Time.deltaTime), 0);

        /*
         * Esto actualiza la posicion del Dron en x,y,z siguiendo la posición del objeto Guia, usando un PID para estabilizar la posición de cada eje.
         */
        v.x = pidx.Update(guide.position.x, drone.position.x, Time.deltaTime);
        v.y = pidy.Update(guide.position.y, drone.position.y, Time.deltaTime);
        v.z = pidz.Update(guide.position.z, drone.position.z, Time.deltaTime);

        drone.Translate(v);

    }

}

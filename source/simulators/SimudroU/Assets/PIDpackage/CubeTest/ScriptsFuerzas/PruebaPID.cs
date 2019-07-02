using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// Super clase de PID extraida de https://forum.unity.com/threads/pid-controller.68390/

/*
 * La idea es probar esto en un cubo.
 * El cubo será cambiado de posicion "manualmente" en Y en el editor, y el pid debera regresarloa la posición deseada que es setY.
*/
public class PruebaPID : MonoBehaviour
{
    public PID pid; // por default probar: 0.1, 0.1, y 0
    Transform t;
    public float setY = 10f;

    // Start is called before the first frame update
    void Start()
    {
        //pid = new PID(0.1f,0.1f,0f);  // al parecer no requiere instanciar O.o
        t = GetComponent<Transform>();
    }

    // Update is called once per frame
    void Update()
    {
        //t.Translate(0, pid.Update(setY, t.position.y, Time.deltaTime), 0);
    }

    private void FixedUpdate()
    {
        t.Translate(0, pid.Update(setY, t.position.y, Time.deltaTime), 0);
    }
}

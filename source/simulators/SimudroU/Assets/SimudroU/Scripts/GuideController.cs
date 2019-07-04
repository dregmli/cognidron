using System.Collections;
using System.Collections.Generic;
using UnityEngine;

/**
 * Controlador para mover el objeto Guía, al cual sigue el Drone usando el PID.
 */

public class GuideController : MonoBehaviour
{
    public float speed = 8f;
    Transform transf;

    void Start()
    {
        transf = GetComponent<Transform>();
    }


    void Update()
    {
        
    }

    private void FixedUpdate()
    {
        //avanzar
        if (Input.GetKey(KeyCode.W))
        {
            transf.Translate(new Vector3(0, 0, speed) * Time.deltaTime);
            Debug.Log("Esto funcina ww");
        }
        //reversa
        if (Input.GetKey(KeyCode.S))
        {
            transf.Translate(new Vector3(0, 0, -1 * speed) * Time.deltaTime);
        }
        //derecha
        if (Input.GetKey(KeyCode.D))
        {
            transf.Translate(new Vector3(speed, 0, 0) * Time.deltaTime);
        }
        //izquierda
        if (Input.GetKey(KeyCode.A))
        {
            transf.Translate(new Vector3(-1 * speed, 0, 0) * Time.deltaTime);
        }

        //Para arriba
        if (Input.GetKey(KeyCode.I))
        {
            transf.Translate(new Vector3(0, speed, 0) * Time.deltaTime);
        }
        //Para abajo
        if (Input.GetKey(KeyCode.K))
        {
            transf.Translate(new Vector3(0, -1 * speed, 0) * Time.deltaTime);
        }





        if (Input.GetKeyDown(KeyCode.Space))
        {
            Debug.Log("Space key was pressed.");
        }


        if (Input.GetKeyUp(KeyCode.Space))
        {
            Debug.Log("Space key was released.");
        }
    }
}

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class InterfazPython : MonoBehaviour
{

    private Transform myTransform;
    public float speed = 2;
    HelloRequester2 con;

    // Start is called before the first frame update
    void Start()
    {
        myTransform = GetComponent <Transform> ();
        con = new HelloRequester2();
        con.Start();

    }

    // Update is called once per frame
    void Update()
    {
        Debug.Log("Receivedo de python: " + con.comando + con.intensidad);


        //avanzar
        if (con.comando.Equals("push")) {
            myTransform.Translate(new Vector3(0,0,speed) * Time.deltaTime * con.intensidad);
        }
        //derecha
        if (con.comando.Equals("right")) {
            myTransform.Translate(new Vector3(speed,0,0) * Time.deltaTime * con.intensidad);
        }
        //Para arriba
        if (con.comando.Equals("lift")) {
            myTransform.Translate(new Vector3(0,speed,0) * Time.deltaTime * con.intensidad);
        }





        //avanzar
        if (Input.GetKey(KeyCode.W)) {
            myTransform.Translate(new Vector3(0,0,speed) * Time.deltaTime);
        }
        //reversa
        if (Input.GetKey(KeyCode.S)) {
            myTransform.Translate(new Vector3(0,0,-1 * speed) * Time.deltaTime);
        }
        //derecha
        if (Input.GetKey(KeyCode.D)) {
            myTransform.Translate(new Vector3(speed,0,0) * Time.deltaTime);
        }
        //izquierda
        if (Input.GetKey(KeyCode.A)) {
            myTransform.Translate(new Vector3(-1*speed,0,0) * Time.deltaTime);
        }

        //Para arriba
        if (Input.GetKey(KeyCode.I)) {
            myTransform.Translate(new Vector3(0,speed,0) * Time.deltaTime);
        }

        //Para abajo
        if (Input.GetKey(KeyCode.K)) {
            myTransform.Translate(new Vector3(0,-1*speed,0) * Time.deltaTime);
        }





        if( Input.GetKeyDown( KeyCode.Space ) ) {
                Debug.Log( "Space key was pressed." );
            }


        if( Input.GetKeyUp( KeyCode.Space ) ) {
                Debug.Log( "Space key was released." );
            }
    }


    void OnDestroy()
    {
        con.Stop();
    }



}

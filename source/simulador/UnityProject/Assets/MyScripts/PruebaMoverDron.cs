using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PruebaMoverDron : MonoBehaviour
{

	private Transform myTransform;
    public float speed = 2;
    

    // Start is called before the first frame update
    void Start()
    {
        myTransform = GetComponent <Transform> ();
    }

    // Update is called once per frame
    void Update()
    {
       

        //avanzar
        if (Input.GetKey(KeyCode.T)) {
            myTransform.Translate(new Vector3(0,0,speed) * Time.deltaTime);
        }
        //reversa
        if (Input.GetKey(KeyCode.G)) {
            myTransform.Translate(new Vector3(0,0,-1 * speed) * Time.deltaTime);
        }
        //derecha
        if (Input.GetKey(KeyCode.H)) {
            myTransform.Translate(new Vector3(speed,0,0) * Time.deltaTime);
        }
        //izquierda
        if (Input.GetKey(KeyCode.F)) {
            myTransform.Translate(new Vector3(-1*speed,0,0) * Time.deltaTime);
        }

        //Para arriba
        if (Input.GetKey(KeyCode.Y)) {
            myTransform.Translate(new Vector3(0,speed,0) * Time.deltaTime);
        }

        //Para abajo
        if (Input.GetKey(KeyCode.R)) {
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
        //con.Stop();
    }
}

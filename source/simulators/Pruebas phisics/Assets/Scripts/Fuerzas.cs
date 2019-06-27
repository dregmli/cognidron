using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Fuerzas : MonoBehaviour
{
	public int fuerza = 10;
	public float volar = 8f;

	private Rigidbody rb;
    // Start is called before the first frame update
    void Start()
    {
        rb = GetComponent<Rigidbody>();
    }

    // Update is called once per frame
    void Update()
    {

    	if (Input.GetKey(KeyCode.W)) {
            rb.AddForce(new Vector3(fuerza,0,0));
            estabilizar(true);
        }
        if (Input.GetKey(KeyCode.S)) {
            rb.AddForce(new Vector3(fuerza * -1,0,0));
        }
        if (Input.GetKey(KeyCode.D)) {
            rb.AddForce(new Vector3(0,fuerza,0));
        }
        if (Input.GetKey(KeyCode.A)) {
            rb.AddForce(new Vector3(0,fuerza * -1,0));
        }
        
        
    }


    void FixedUpdate(){
    	// Para mantenerlo flotando como si volara
    	estabilizar(true);
    		
    	//Debug.Log("estooo funcinaaa??");
    }


    // Para estabilizar el dron a cierta altura.
    private Vector3 pOld; // position old
    private int contador = 0;
    public int delay = 20; // espacio en el tiempo en cantidad de FiexedUpdates ejecutados, de la posicion anterior a la actual
    public float maxY = 0.1f; // limite mazximo de caida y subida
    void estabilizar(bool flag){
    	if (flag == true){
    		if (pOld != null){
    			contador++;
    			//Debug.Log("contador: " + contador);
    			if(contador >= delay){
	    			Vector3 pNow = GetComponent<Transform>().position; 
	    			//Debug.Log("Position-> x:" + t.position.x + ", y:" + t.position.y + ", z:" + t.position.z);
	    			float r = pNow.y  - pOld.y;
	    			Debug.Log("r: " + r);
	    			if ( r * -1 > maxY){
	    				rb.AddForce(new Vector3(0,volar,0));
	    			}
	    			pOld = new Vector3(pNow.x, pNow.y, pNow.z);
	    			contador = 0;
    			}
    		}else{pOld = GetComponent<Transform>().position;}

    	}
    }

}

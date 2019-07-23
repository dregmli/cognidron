using System.Collections;
using System.Collections.Generic;
using UnityEngine;

//Para agregar lo de fuerza relativa, agregar el componente en unity.
//mas info en : https://docs.unity3d.com/es/current/Manual/class-ConstantForce.html

public class FuerzaConstante : MonoBehaviour
{
    Rigidbody rb;
    // Start is called before the first frame update
    void Start()
    {
        rb = GetComponent<Rigidbody>();
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}

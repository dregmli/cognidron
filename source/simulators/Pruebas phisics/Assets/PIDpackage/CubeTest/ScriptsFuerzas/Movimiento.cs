using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Movimiento : MonoBehaviour
{
	public float moveSpeed;
	private Vector3 moveInput;
	private Vector3 moveVelocity;
	private Rigidbody rb;

    // Start is called before the first frame update
    void Start()
    {
        rb = GetComponent<Rigidbody>();

    }

    // Update is called once per frame
    void Update()
    {
        float lh = Input.GetAxis("Horizontal");
        float lv = Input.GetAxis("Vertical");

        moveInput = new Vector3(lh, 0f, lv);
        moveVelocity = transform.forward * moveSpeed * moveInput.sqrMagnitude;
        Debug.Log("moveVelocity = " + transform.forward + ", " + moveSpeed + ", " + moveInput.sqrMagnitude);
        //Debug.Log("= ", moveVelocity);
    }

    void FixedUpdate() //se ejecuta cada 20 ms
    {
    	rb.velocity = moveVelocity;
    }
}

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// En esta clase se busca emular los movimientos del cubo de Emotiv BCI para entrenar los comando
public class ManualTrainingBasics : MonoBehaviour
{

    public int entrenamiento = 1; // 1: elevar, 2: empujar, 3: derecha
    public float speed = 2;

    Transform t;
    

    void Start()
    {
        t = GetComponent<Transform>();
    }

    // Update is called once per frame
    void Update()
    {
        
        
    }

    private void FixedUpdate()
    {
        if (entrenamiento == 1)
        {
            t.Translate(new Vector3(0, speed, 0) * Time.deltaTime);
            if (t.position.y > 600) {
                t.Translate(new Vector3(0, -4, 0));
            }
        }
        else if (entrenamiento == 2)
        {
            t.Translate(new Vector3(0, 0, speed) * Time.deltaTime);
        }
        else if (entrenamiento == 3)
        {
            t.Translate(new Vector3(speed, 0, 0) * Time.deltaTime);
        }
    }
}

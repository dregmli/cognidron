using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

// https://emotiv.gitbook.io/epoc-user-manual/using-headset/epoc+_headset_details

public class LevelInterfacePython : MonoBehaviour
{

    public float amplitudTBR = 2;
    public Scrollbar HealthBar1;
    public Scrollbar HealthBar2;
    public Scrollbar HealthBar3;
    public Text txt;
    LevelRequesterThread con;

    private float tbr = 0.1f;

    // Start is called before the first frame update
    void Start()
    {
        // myTransform = GetComponent<Transform>();
        con = new LevelRequesterThread();
        con.Start();

    }

    private void Update()
    {
        txt.text = "TBR: " + tbr.ToString();
        
    }

    // Update is called once per frame
    void FixedUpdate()
    {
        

        //comando seria : m1, m2 o m3,
        //intensidad seria el valor del canal de la banda

        if (con.comando.Equals("theta")) // f3 theta
        {
            //mover la barra
            HealthBar1.size = con.intensidad;
        }
        if (con.comando.Equals("beta")) // f3 betha low
        {
            //mover la barra
            HealthBar2.size = con.intensidad;
            actualizarTBR();
        }
        
      
    }


    void actualizarTBR()
    {
        tbr = HealthBar1.size / HealthBar2.size;
        HealthBar3.size =  ( tbr / 10) * amplitudTBR;
        // Debug.Log(">> TBR = " + tbr);
        
    }


    void OnDestroy()
    {
        con.Stop();
    }



}

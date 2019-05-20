#obtenido de aca https://geekytheory.com/pylab-parte-1-python-se-viste-de-matlab

import numpy as np 
import matplotlib.pyplot as pyplot

#Se crea la nube de puntos
x = np.array([0, 1, 2, 3])
y = np.array([1,1.5,1.8,2.6])

#Construimos una matriz
A = np.vstack([x, np.ones(len(x))])
A = A.T #hacemos su traspuesta

#Obtenemos parametros de la recta
m, c = np.linalg.lstsq(A,y)[0]
print("La recta obtenida es: y = " + str(m) + "x + " + str(c))


pyplot.plot(x, y, 'o', label='Nubes puntos', markersize=15 )
pyplot.plot(x, m*x + c, 'r', label='Regresion Lineal')
pyplot.legend()
pyplot.show()  

raw_input("Enter para salir")
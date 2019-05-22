# Aprendiendo a graficar simple con matplotlib
# tuto de https://matplotlib.org/tutorials/introductory/pyplot.html

import matplotlib.pyplot as plt

listaX = [1,2,3,4,5,6,7,8]
listaY = [1,2,4,8,16,32,64,128]

plt.plot(listaX, listaY) #plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()


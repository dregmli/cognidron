import matplotlib.animation as animation
import numpy as np
 
COUNT = 100
fig, ax = plt.subplots()
line, = ax.plot([], [])
ax.set_ylim([-1.5, 1.5])
ax.set_xlim(0, COUNT)
xdata = []
ydata = [] 
def next():
   i = 0
   while i &lt;= COUNT:
      i += 1
      yield i
def update(i):
   xdata.append(i)
   y = np.sin(i / 10.)
   ydata.append(y)
   line.set_data(xdata, ydata)
   return line,
 
if __name__ == '__main__':
   a = animation.FuncAnimation(fig, update, next, blit = False, interval = 60,
                               repeat = False)
   plt.show()
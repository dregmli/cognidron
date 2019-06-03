import sys

#from PyQt5.QtCore import QTimer
#from PyQt5.QtGui import QApplication
from PyQt5 import QtGui, QtCore

app = QtGui.QApplication(sys.argv)

app.setQuitOnLastWindowClosed(False)

def tick():
    print ('tick')

timer = QtCore.QTimer()
timer.timeout.connect(tick)
timer.start(1000)

# run event loop so python doesn't exit
app.exec_()
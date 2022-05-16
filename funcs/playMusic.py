from PyQt5 import QtWidgets, QtGui, QtCore
from playsound import playsound

class CloneThread(QtCore.QThread):
    signal = QtCore.pyqtSignal('PyQt_PyObject')
    def __init__(self):
        QtCore.QThread.__init__(self)
    def run(self):
        playsound(u"./gui/bruh.wav")
        self.signal.emit('')  # signal for main thread to understand this thread working has finished!

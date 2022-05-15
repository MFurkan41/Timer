from PyQt5 import QtWidgets, QtGui, QtCore
from pydub import AudioSegment
from pydub.playback import play

class CloneThread(QtCore.QThread):
    signal = QtCore.pyqtSignal('PyQt_PyObject')
    def __init__(self):
        QtCore.QThread.__init__(self)
    def run(self):
        music = AudioSegment.from_mp3(
            "D:\PROJECTS\Timer\gui\bruh.mp3")  # path to the audio file that will play after time is over
        play(music)
        self.signal.emit('')  # signal for main thread to understand this thread working has finished!

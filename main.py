from PyQt5 import QtWidgets, QtGui, QtCore
from gui.frame import Ui_MainWindow
import sys,time,enum
from funcs.playMusic import CloneThread

class TimerStatus(enum.Enum):
    init, counting, paused = 1, 2, 3


class Timer(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        # Window Settings
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._left_seconds = 5
        self._left_secondsB = self._left_seconds
        self.isLabelRed = False
        self.timesBlink = 3

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.show()


        # Close App
        self.ui.rightTB.clicked.connect(self.close)
        
        # Timer
        self.ui.minutesSpinBox.setValue(int(self._left_seconds/60))
        self.ui.minutesSpinBox.valueChanged.connect(self._edit_event)
        self.ui.redB.clicked.connect(self._start_event)
        self.ui.rightMB.clicked.connect(self._reset_event)
        self.ui.blueLB.clicked.connect(lambda x:self.increase_decrease(0))
        self.ui.blueRB.clicked.connect(lambda x:self.increase_decrease(1))
        
        self._status = TimerStatus.init
        
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self._countdown_and_show)
        self.showTime()

        self.blinkTimer = QtCore.QTimer(self)
        self.blinkTimer.timeout.connect(self.flashLbl)

        self.thread = QtCore.QThread()
        self.worker = CloneThread()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        
    
    def increase_decrease(self, num):
        if num:
            self.ui.minutesSpinBox.setValue(self.ui.minutesSpinBox.value()+5)
        else:
            self.ui.minutesSpinBox.setValue(self.ui.minutesSpinBox.value()-5)
        self.showTime()

    def _countdown_and_show(self):
        if self._left_seconds > 0:
            self._left_seconds -= 1
            self.showTime()
        else:
            self.timer.stop()
            #self.startButton.setText(ButtonText.start)
            self._status = TimerStatus.init
            self._left_seconds = self._left_secondsB
            self._reset_event()
            self.blinkTimer.start(1000)
            self.thread.start()
            

    def _start_event(self):
        if (self._status == TimerStatus.init or self._status == TimerStatus.paused) and self._left_seconds > 0:
            self.ui.blueLB.setDisabled(True)
            self.ui.blueRB.setDisabled(True)
            self._left_seconds -= 1
            self._status = TimerStatus.counting
            self.showTime()
            self.timer.start(1000)
            #self.startButton.setText(ButtonText.pause)
        elif self._status == TimerStatus.counting:
            
            self.timer.stop()
            self._status = TimerStatus.paused
            #self.startButton.setText(ButtonText.start)

    def _reset_event(self):
        self.ui.blueLB.setEnabled(True)
        self.ui.blueRB.setEnabled(True)
        self._status = TimerStatus.init
        self._left_seconds = self.ui.minutesSpinBox.value() * 60
        #self.startButton.setText(ButtonText.start)
        self.timer.stop()
        self.showTime()

    def _edit_event(self):
        if self._status == TimerStatus.init:
            self._left_seconds = self.ui.minutesSpinBox.value() * 60
            self.showTime()

    def showTime(self):
        total_seconds = min(self._left_seconds, 359940)  # Max time: 99:59:00
        hours = total_seconds // 3600
        total_seconds = total_seconds - (hours * 3600)
        minutes = total_seconds // 60
        seconds = total_seconds - (minutes * 60)
        if hours != 0:
            self.ui.label.setText("{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds)))
            self.ui.font.setPointSize(35)
            self.ui.label.setFont(self.ui.font)
        else:
            self.ui.label.setText("{:02}:{:02}".format(int(minutes), int(seconds)))
            self.ui.font.setPointSize(50)
            self.ui.label.setFont(self.ui.font)
    
    def flashLbl(self):
        if self.isLabelRed == False:
            if self.timesBlink == 0:
                self.timesBlink = 3
                self.blinkTimer.stop()
                self.showTime()
                return
            self.ui.label.setStyleSheet("color: rgb(255,0,0)")
            self.isLabelRed = True
            self.timesBlink -= 1
        else:
            self.ui.label.setStyleSheet("color: rgb(0,0,0)")
            self.isLabelRed = False

    # Move Screen
    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        self.oldPosition = event.globalPos()
    
    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        delta = QtCore.QPoint(event.globalPos()) - self.oldPosition
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPos()
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Timer()
    sys.exit(app.exec_())
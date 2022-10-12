# This Python file uses the following encoding: utf-8
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys, cv2, serial, time
from PyQt6 import uic
from mainwindow import Ui_MainWindow
from  pneumaticTest import Ui_PneumaticTest
from enum import Enum


# Global variables 
arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1)

class Thread(QThread):
    changePixmap = pyqtSignal(QImage)

    def run(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if ret:
                # https://stackoverflow.com/a/55468544/6622587
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                qformat = QImage.Format.Format_RGB888
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, qformat)
                p = convertToQtFormat.scaled(640, 480, Qt.AspectRatioMode.KeepAspectRatio)
                self.changePixmap.emit(p)

class Mode(Enum):
  MANUAL = 1
  AUTO = 2


class MainWindow(QMainWindow, Ui_MainWindow):
  def __init__(self, *args, **kwargs):

    # initialize window and load ui
    super(MainWindow, self).__init__(*args, **kwargs)
    uic.loadUi("mainwindow.ui", self)
    self.setWindowTitle("Vine Robot")
    self.setupUi(self)

    # initialize the pneumatic window
    self.pneumaticTestWindow = QMainWindow()
    self.ui = Ui_PneumaticTest()
    self.ui.setupUi(self.pneumaticTestWindow)

    # create a custom label for the video feedback
    self.label = QLabel(self)
    self.label.move(70, 10)
    self.label.resize(720, 320)
    th = Thread(self)
    th.changePixmap.connect(self.setImage)
    th.start()
    self.show()

    # initialize fields (slots)
    # cahnge to manual after testing
    self.mode = None
    self.temperature = None
    self.speed = None
    self.pressure = None
    self.orientation = None
    self.object_identified = None
    self.following_object = None

    # establish connections between signals and slots
    self.manual_mode_radioBtn.toggled.connect(lambda:self.setMode(self.manual_mode_radioBtn))
    self.auto_mode_radioBtn.toggled.connect(lambda:self.setMode(self.auto_mode_radioBtn))
    

  # Define Functions
  # function to set the video 
  @pyqtSlot(QImage)
  def setImage(self, image):
    self.label.setPixmap(QPixmap.fromImage(image))

  # function to set the mode based on the radio button - setter method
  def setMode(self, btn):
    if self.sender().isChecked():
      if self.sender().objectName() == 'auto_mode_radioBtn':
        self.mode = Mode.AUTO
      if self.sender().objectName() == 'manual_mode_radioBtn':
        self.mode = Mode.MANUAL
    print("selected mode ", self.mode)

  # getter method for the mode
  def getMode(self):
    return self.mode

  # Send data to arduino
  def write_read(self, x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

  # Allows user to enter a byte
  def byte_send(self, num):
    while True:
      # num = input("Enter a number: ")  # Taking input from user
      value = self.write_read(num)
      print(value)  # printing the value

  # methods for testing the valves 
  def testValve1(self):
    valveBtn = self.pneumaticTestWindow.sender()
    if valveBtn.isChecked():
      if valveBtn.objectName() == 'Valve1On':
        self.byte_send(1)
        print("sent byte to arduino, need one to test it")
      if valveBtn.objectName() == 'Valve1Off':
        self.byte_send(2)
        print("sent byte to arduino, need one to test it")


if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec())

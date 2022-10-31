from itertools import tee
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys, cv2, serial, time, datetime, os
from PyQt6 import uic
from mainwindow import Ui_MainWindow
from DebugWindow import Ui_DebugWindow
from MainController import Ui_MainController
from enum import Enum
from ball_tracking import Tracker

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

    # Initialize thread pool
    self.threadpool = QThreadPool()
    print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

    # initialize the debug window
    self.debugWindow = QMainWindow()
    self.debugUI = Ui_DebugWindow()
    self.debugUI.setupUi(self.debugWindow)

    # initialize controller window
    self.controller = QMainWindow()
    self.controllerUI = Ui_MainController()
    self.controllerUI.setupUi(self.controller)

    # create a custom label for the video feedback
    self.label = QLabel(self)
    self.label.move(70, 10)
    self.label.resize(720, 320)
    # th = Thread(self)
    # th.changePixmap.connect(self.setImage)
    # th.start()
    tracker = Tracker(self)
    tracker.changePixmap.connect(self.setImage)
    tracker.start()
    
    # finally show GUI
    self.show()

    ###############################################
    #         initialize fields (slots)
    ###############################################
    self.mode = None                # change to manual after testing
    self.temperature = None
    self.speed = None
    self.pressure = None
    self.orientation = None
    self.object_identified = None
    self.following_object = None

    ###############################################
    #        connect signals and slots
    ###############################################
    # Main Window connections
    self.debugAction.triggered.connect(lambda:self.openDebugWindow(self.debugWindow))
    self.Main_Controller_action.triggered.connect(lambda:self.openControllerWindow(self.controller))
    self.manual_mode_radioBtn.toggled.connect(lambda:self.setMode(self.manual_mode_radioBtn))
    self.auto_mode_radioBtn.toggled.connect(lambda:self.setMode(self.auto_mode_radioBtn))
    self.ConnectBtn.clicked.connect(lambda:self.setUpArduino(self.port_line.text()))
    
    # Test Window connections
    # Pneumatic Buttons
    self.debugUI.Valve1On.toggled.connect(lambda:self.testValve1(self.debugUI.Valve1On))
    self.debugUI.Valve2On.toggled.connect(lambda:self.testValve2(self.debugUI.Valve2On))
    self.debugUI.Valve3On.toggled.connect(lambda:self.testValve3(self.debugUI.Valve3On))
    self.debugUI.Valve4On.toggled.connect(lambda:self.testValve4(self.debugUI.Valve4On))
    self.debugUI.Valve5On.toggled.connect(lambda:self.testValve5(self.debugUI.Valve5On))
    self.debugUI.Valve1Off.toggled.connect(lambda:self.testValve1(self.debugUI.Valve1Off))
    self.debugUI.Valve2Off.toggled.connect(lambda:self.testValve2(self.debugUI.Valve2Off))
    self.debugUI.Valve3Off.toggled.connect(lambda:self.testValve3(self.debugUI.Valve3Off))
    self.debugUI.Valve4Off.toggled.connect(lambda:self.testValve4(self.debugUI.Valve4Off))
    self.debugUI.Valve5Off.toggled.connect(lambda:self.testValve5(self.debugUI.Valve5Off))
    # Ball valve buttons
    self.debugUI.Ball1OnRbtn.toggled.connect(lambda:self.testBall1(self.debugUI.Ball1OnRbtn))
    self.debugUI.Ball2OnRbtn.toggled.connect(lambda:self.testBall2(self.debugUI.Ball2OnRbtn))
    self.debugUI.Ball3OnRbtn.toggled.connect(lambda:self.testBall3(self.debugUI.Ball3OnRbtn))
    self.debugUI.Ball4OnRbtn.toggled.connect(lambda:self.testBall4(self.debugUI.Ball4OnRbtn))
    self.debugUI.Ball1OffRbtn.toggled.connect(lambda:self.testBall1(self.debugUI.Ball1OffRbtn))
    self.debugUI.Ball2OffRbtn.toggled.connect(lambda:self.testBall2(self.debugUI.Ball2OffRbtn))
    self.debugUI.Ball3OffRbtn.toggled.connect(lambda:self.testBall3(self.debugUI.Ball3OffRbtn))
    self.debugUI.Ball4OffRbtn.toggled.connect(lambda:self.testBall4(self.debugUI.Ball4OffRbtn))
    self.debugUI.BVallPause.toggled.connect(lambda:self.testBall1(self.debugUI.BVallPause))
    self.debugUI.BVallPause_2.toggled.connect(lambda:self.testBall2(self.debugUI.BVallPause_2))
    self.debugUI.BVallPause_3.toggled.connect(lambda:self.testBall3(self.debugUI.BVallPause_3))
    self.debugUI.BVallPause_4.toggled.connect(lambda:self.testBall4(self.debugUI.BVallPause_4))
    # Motor buttons
    self.debugUI.Motor1_fwd.toggled.connect(lambda:self.testMotor1(self.debugUI.Motor1_fwd))
    self.debugUI.Motor2_fwd.toggled.connect(lambda:self.testMotor2(self.debugUI.Motor2_fwd))
    self.debugUI.Motor3_fwd.toggled.connect(lambda:self.testMotor3(self.debugUI.Motor3_fwd))
    self.debugUI.Motor1_rev.toggled.connect(lambda:self.testMotor1(self.debugUI.Motor1_rev))
    self.debugUI.Motor2_rev.toggled.connect(lambda:self.testMotor2(self.debugUI.Motor2_rev))
    self.debugUI.Motor3_rev.toggled.connect(lambda:self.testMotor3(self.debugUI.Motor3_rev))
    self.debugUI.Motor1Off.toggled.connect(lambda:self.testMotor1(self.debugUI.Motor1Off))
    self.debugUI.Motor2Off.toggled.connect(lambda:self.testMotor2(self.debugUI.Motor2Off))
    self.debugUI.Motor3Off.toggled.connect(lambda:self.testMotor3(self.debugUI.Motor3Off))


    self.debugUI.send_speed1.clicked.connect(lambda:self.sendMotorSpeed1(self.debugUI.Motor1_speed.text()))
    self.debugUI.send_speed2.clicked.connect(lambda:self.sendMotorSpeed2(self.debugUI.Motor2_speed.text()))
    self.debugUI.send_speed3.clicked.connect(lambda:self.sendMotorSpeed3(self.debugUI.Motor3_speed.text()))

  ###############################################
  #            Define Functions
  ###############################################
  # functions to open the debug and controller window
  def openDebugWindow(self, window):
    window.show()

  def openControllerWindow(self, window):
    window.show()

  # initialize arduino by user input
  def setUpArduino(self, line):
    print(line)
    self.arduino = serial.Serial(
        port=line,
        baudrate=115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS
    )
    self.my_timer = QTimer()
    self.my_timer.timeout.connect(self.showTemp)
    self.my_timer.timeout.connect(self.showAcc)
    self.my_timer.timeout.connect(self.showPressure)
    self.my_timer.start(3000)  # 1 min intervall

    # worker = Worker(self.showTemp, self.showAcc)
    # self.threadpool.start(worker)

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

  # Write data to base control board
  def sendByte(self, _str):
      self.arduino.write(_str.encode())

  # read byte from the control board
  # TODO
  def readByte(self, int):
    line = self.arduino.readline().decode('utf-8')
    splitLine = line.split()

    temp = splitLine[0]
    print(splitLine)
    #temp = "24.55"
    acc = splitLine[1]
    pressure1 = splitLine[2]
    pressure2 = splitLine[3]
    pressure3 = splitLine[4]
    pressure4 = splitLine[5]
    pressure = []
    pressure.append(pressure1)
    pressure.append(pressure2)
    pressure.append(pressure3)
    pressure.append(pressure4)
    # print("pressure ", pressure)

    if int == 1:
        return str(temp)
    if int == 2:
        return str(acc)
    if int == 3:
        return pressure
    #add rest

  # show values from the pcb in display
  # TODO: might have to put these in a different thread
  

  def showAcc(self):
    accel = self.readByte(2)
    self.speed_val_rcvd.setText(accel)

  def showPressure(self):
    pressure = self.readByte(3)
    self.pressure_val_rcvd.setText(pressure[0])
    self.pressure_val_rcvd_2.setText(pressure[1])
    self.pressure_val_rcvd_3.setText(pressure[2])
    self.pressure_val_rcvd_4.setText(pressure[3])

  def showTemp(self):
    temperature = self.readByte(1)
    self.temp_val_rvcd.setText(temperature)


  # methods for testing the pneumatic valves
  # TODO: M change the byte you want to send inside the sendByte() 
  def testValve1(self, rbtn):
    btn = self.debugWindow.sender()
    if btn.isChecked():
      if btn.objectName() == 'Valve1On':
        self.sendByte("1\r")
        print("sent byte to arduino: valve 1 on")
      if btn.objectName() == 'Valve1Off':
        self.sendByte("2\r")
        # print("sent byte to arduino: valve 1 off")

  def testValve2(self, rbtn):
    btn = self.debugWindow.sender()
    if btn.isChecked():
      if btn.objectName() == 'Valve2On':
        self.sendByte("3\r")
        print("sent byte to arduino: valve 2 on")
      if btn.objectName() == 'Valve2Off':
        self.sendByte("4\r")
        # print("sent byte to arduino: valve 2 off")

  def testValve3(self, rbtn):
    btn = self.debugWindow.sender()
    if btn.isChecked():
      if btn.objectName() == 'Valve3On':
        self.sendByte("5\r")
        print("sent byte to arduino: valve 3 on")
      if btn.objectName() == 'Valve3Off':
        self.sendByte("6\r")
        # print("sent byte to arduino: valve 3 off")

  def testValve4(self, rbtn):
    btn = self.debugWindow.sender()
    if btn.isChecked():
      if btn.objectName() == 'Valve4On':
        self.sendByte("7\r")
        print("sent byte to arduino: valve 4 on")
      if btn.objectName() == 'Valve4Off':
        self.sendByte("8\r")
        # print("sent byte to arduino: valve 4 off")

  def testValve5(self, rbtn):
    btn = self.debugWindow.sender()
    if btn.isChecked():
      if btn.objectName() == 'Valve5On':
        self.sendByte("9\r")
        print("sent byte to arduino: valve 5 on")
      if btn.objectName() == 'Valve5Off':
        self.sendByte("10\r")
        # print("sent byte to arduino: valve 5 off")

  def testBall1(self, rbtn):
    btn = self.debugWindow.sender()
    if btn.isChecked():
      if btn.objectName() == 'Ball1OnRbtn':
        self.sendByte("11\r")
      if btn.objectName() == 'Ball1OffRbtn':
        self.sendByte("12\r")
      if btn.objectName() == 'BVallPause':
        self.sendByte("13\r")
        print("Ball valve 1 paused")

  def testBall2(self, rbtn):
    btn = self.debugWindow.sender()
    if btn.isChecked():
      if btn.objectName() == 'Ball2OnRbtn':
        self.sendByte("14\r")
      if btn.objectName() == 'Ball2OffRbtn':
        self.sendByte("15\r")
      if btn.objectName() == 'BVallPause_2':
        self.sendByte("16\r")
        print("Ball valve 2 paused")
    
  def testBall3(self, rbtn):
    btn = self.debugWindow.sender()
    if btn.isChecked():
      if btn.objectName() == 'Ball3OnRbtn':
        self.sendByte("17\r")
      if btn.objectName() == 'Ball3OffRbtn':
        self.sendByte("18\r")
      if btn.objectName() == 'BVallPause_3':
        self.sendByte("19\r")
        print("Ball valve 3 paused")

  def testBall4(self, rbtn):
    btn = self.debugWindow.sender()
    if btn.isChecked():
      if btn.objectName() == 'Ball4OnRbtn':
        self.sendByte("20\r")
      if btn.objectName() == 'Ball4OffRbtn':
        self.sendByte("21\r")
      if btn.objectName() == 'BVallPause_4':
        self.sendByte("22\r")
        print("Ball valve 4 paused")

  def testMotor1(self, rbtn):
    btn = self.debugWindow.sender()
    if btn.isChecked():
      if btn.objectName() == 'Motor1_fwd':
        self.sendByte("27\r")
      if btn.objectName() == 'Motor1_rev':
        self.sendByte("28\r")
      # add reverse button -->29
      if btn.objectName() == 'Motor1Off':
        self.sendByte("29\r")

  def testMotor2(self, rbtn):
    btn = self.debugWindow.sender()
    if btn.isChecked():
      if btn.objectName() == 'Motor2_fwd':
        self.sendByte("30\r")
      if btn.objectName() == 'Motor2_rev':
        self.sendByte("31\r")
        #  off button --> 32
      if btn.objectName() == 'Motor2Off':
        self.sendByte("32\r")

  def testMotor3(self, rbtn):
    btn = self.debugWindow.sender()
    if btn.isChecked():
      if btn.objectName() == 'Motor3_fwd':
        self.sendByte("33\r")
      if btn.objectName() == 'Motor3_rev':
        self.sendByte("34\r")
        #  off button --> 35
      if btn.objectName() == 'Motor3Off':
        self.sendByte("35\r")

# TODO: check how you want to do this and what it is that you need to send
  def sendMotorSpeed1(self, txt):
    self.sendByte(f"{txt}\r")
    print(f"sent this speed: {txt}")
  
  def sendMotorSpeed2(self, txt):
    self.sendByte(f"{txt}\r")
    print(f"sent this speed: {txt}")

  def sendMotorSpeed3(self, txt):
    self.sendByte(f"{txt}\r")
    print(f"sent this speed: {txt}")

if __name__ == "__main__":
  app = QApplication(sys.argv)
  # form = Form()
  window = MainWindow()
  window.show()
  # form.show()
  sys.exit(app.exec())
  


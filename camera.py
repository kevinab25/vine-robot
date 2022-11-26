import cv2
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class Camera(QThread):
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

        cv2.destroyAllWindows()

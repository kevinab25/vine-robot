# import the necessary packages
from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class Tracker(QThread):
  changePixmap = pyqtSignal(QImage)

  def run(self):
    greenLower = (29, 86, 6)
    greenUpper = (64, 255, 255)
    pts = deque(maxlen=64)
    
    vs = VideoStream(src=0).start()
    cap = cv2.VideoCapture(0)
    time.sleep(1)

    # keep looping
    while True:
        # grab the current frame
        frame = vs.read()
        # frame = cap.read()
        if frame is None:
            break
        # resize the frame, blur it, and convert it to the HSV
        # color space
        frame = imutils.resize(frame, width=640, height=480)
        blurred = cv2.GaussianBlur(frame, (11, 11), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # COLOR_BGR2HSV
        # COLOR_BGR2RGB

        h, w, ch = frame.shape
        bytesPerLine = ch * w

        # # construct a mask for the color "green", then perform
        # # a series of dilations and erosions to remove any small
        # # blobs left in the mask
        mask = cv2.inRange(hsv, greenLower, greenUpper)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)

        # # find contours in the mask and initialize the current
        # # (x, y) center of the ball
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        center = None
        # only proceed if at least one contour was found
        if len(cnts) > 0:
            # find the largest contour in the mask, then use
            # it to compute the minimum enclosing circle and
            # centroid
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            # only proceed if the radius meets a minimum size
            if radius > 10:
                # draw the circle and centroid on the frame,
                # then update the list of tracked points
                cv2.circle(frame, (int(x), int(y)), int(radius),
                          (0, 255, 255), 2)
                cv2.circle(frame, center, 5, (0, 0, 255), -1)
        # update the points queue
        pts.appendleft(center)

        # show the frame to our screen
        # cv2.imshow("Frame", frame)
        qformat = QImage.Format.Format_RGB888
        convertToQtFormat = QImage(frame.data, w, h, bytesPerLine, qformat)
        p = convertToQtFormat.scaled(640, 480, Qt.AspectRatioMode.KeepAspectRatio)
        self.changePixmap.emit(p)

    cv2.destroyAllWindows()
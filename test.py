import cv2
import numpy as np


rvideo_capture = cv2.VideoCapture(0)
lvideo_capture = cv2.VideoCapture(1)

if not rvideo_capture.isOpened():
    raise Exception("Could not open video device")

if not lvideo_capture.isOpened():
    raise Exception("Could not open video device")

ret, rframe = rvideo_capture.read()
rvideo_capture.release()

ret, lframe = lvideo_capture.read()
lvideo_capture.release()

cv2.imwrite('rtest.png', rframe)
cv2.imwrite('ltest.png', lframe)

imgL = cv2.imread('ltest.png',0)
imgR = cv2.imread('rtest.png',0)


stereo = cv2.StereoBM_create(numDisparities=160)
disparity = stereo.compute(imgL,imgR)
cv2.imwrite('disparity.png', disparity)
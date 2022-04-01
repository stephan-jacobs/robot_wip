import cv2
import numpy as np
from PIL import Image
import time

rvideo_capture = cv2.VideoCapture(0)
lvideo_capture = cv2.VideoCapture(1)

if not rvideo_capture.isOpened():
    raise Exception("Could not open video device")

if not lvideo_capture.isOpened():
    raise Exception("Could not open video device")

ret, rframe = rvideo_capture.read()
rvideo_capture.release()
cv2.imwrite('./rtest.png', rframe)

time.sleep(2)

ret, lframe = rvideo_capture.read()
rvideo_capture.release()

ret, lframe = lvideo_capture.read()
lvideo_capture.release()

cv2.imwrite('./ltest.png', lframe)

imgL=Image.open('ltest.png')
imgR=Image.open('rtest.png')

# imgL=imgL.rotate(-90)
# imgR=imgR.rotate(90)

imgL.save('ltest.png')
imgR.save('rtest.png')

imgL = cv2.imread('ltest.png',0)
imgR = cv2.imread('rtest.png',0)

for i in range(5,255,10):
    if i == 0:
        j = 1
    else:
        j = i
    stereo = cv2.StereoBM_create(numDisparities=16, blockSize=j)
    disparity = stereo.compute(imgL,imgR)
    cv2.imwrite('disparity'+str(j)+'.png', disparity)
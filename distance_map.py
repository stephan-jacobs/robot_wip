import cv2
import time
import datetime
import numpy as np
import matplotlib.pyplot as plt
import RPi.GPIO as GPIO
from MidasDepthEstimation.midasDepthEstimator import midasDepthEstimator

print("hello")

# Initialize depth estimation model
depthEstimator = midasDepthEstimator()

# Initialize webcam
camera = cv2.VideoCapture(0)
# cv2.namedWindow("Depth Image", cv2.WINDOW_NORMAL)

# Read frame from the webcam
print("Taking Picture")
ret, img = camera.read()
camera.release()
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Estimating depth")
start = time.time()
colorDepth = depthEstimator.estimateDepth(img)
print(colorDepth.shape)
cv2.imshow('depth', colorDepth)
cv2.waitKey(0)
cv2.destroyAllWindows()


bwDepth = np.mean(colorDepth, axis=2)/255
print(bwDepth.shape)
cv2.imshow('depth', bwDepth)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 
# print("Depth estimator took ", time.time() - start, " seconds")
# 
# #img_out = np.hstack((img, bwDepth))
# 
# cv2.imshow("Depth Image", bwDepth)
# cv2.waitKey(1)

# Run Ultrasound Distance Measure 
GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24

print("distance measurement in progress")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)

print("waiting for sensor to settle")
time.sleep(2)

GPIO.output(TRIG,True)
time.sleep(0.00001)
GPIO.output(TRIG,False)

while GPIO.input(ECHO)==0:
    pulse_start = time.time()

while GPIO.input(ECHO)==1:
    pulse_end = time.time()

pulse_duration = pulse_end - pulse_start

distance = pulse_duration * 17150

distance = round(distance, 2)

print("Distance:", distance, "cm")

GPIO.cleanup()

# Save file

x = datetime.datetime.now()

dts = x.strftime("%y%m%d_%H%M")

cv2.imwrite(f'./images/depth_img_{dts}_dist{distance}.png', bwDepth*255)
cv2.imwrite(f'./images/img_{dts}_dist{distance}.png', img)
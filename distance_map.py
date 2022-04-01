import cv2
import time
import numpy as np
import RPi.GPIO as GPIO
from MidasDepthEstimation.midasDepthEstimator import midasDepthEstimator

print("hello")

# Initialize depth estimation model
depthEstimator = midasDepthEstimator()

# Initialize webcam
camera = cv2.VideoCapture(0)
cv2.namedWindow("Depth Image", cv2.WINDOW_NORMAL)

# Read frame from the webcam
print("Taking Picture")
ret, img = camera.read()

print("Estimating depth")
start = time.time()
colorDepth = depthEstimator.estimateDepth(img)
bwDepth = np.mean(colorDepth, axis=2)

print("Depth estimator took ", time.time() - start, " seconds")

#img_out = np.hstack((img, bwDepth))

while True:
    cv2.imshow("Depth Image", bwDepth)

    # Press key q to stop
    if cv2.waitKey(1) == ord('q'):
        break

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
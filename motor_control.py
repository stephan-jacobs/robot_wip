import time
import keyboard
import math
from adafruit_motorkit import MotorKit
kit = MotorKit()

v_set = 0
print('Ready for input')
while True:
    if keyboard.is_pressed('w'):
        v_set += 0.4
    elif keyboard.is_pressed('s'):
        v_set -= 0.4
    elif keyboard.is_pressed('q'):
        break
    elif v_set:
        v_set -= math.copysign(0.2,v_set)
    time.sleep(0.0001)
    print('\n',v_set)
#     kit.motor1.throttle = v_set**2
    
kit.motor1.throttle = 0

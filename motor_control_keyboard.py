import time
import keyboard
import math
from adafruit_motorkit import MotorKit
kit = MotorKit()


v_set = 0
l_diff = 0
r_diff = 0
print('Ready for input')
while True:
    time.sleep(0.0001)
#     print('\n',v_set)
    set_throttle = math.copysign(round(1-1/math.exp(v_set**2),1),v_set)
    print(set_throttle)
    kit.motor1.throttle = set_throttle + l_diff
    kit.motor2.throttle = set_throttle + r_diff
    time.sleep(0.1)
    if keyboard.is_pressed('w'):
        v_set += 0.4
    elif keyboard.is_pressed('s'):
        v_set -= 0.4
    elif keyboard.is_pressed('a'):
        l_diff -= 0.1
        r_diff += 0.1
        v_set += 0.2
    elif keyboard.is_pressed('d'):
        l_diff += 0.1
        r_diff -= 0.1
        v_set += 0.2
    elif keyboard.is_pressed('q'):
        break
    
    if abs(v_set)>0.21 or abs(l_diff)>0.21 or abs(r_diff)>0.21:
#         v_set -= math.copysign(0.11,v_set)
        v_set = 0.8*v_set
        l_diff = 0.8*l_diff
        r_diff = 0.8*r_diff
        print('decay, vset=', v_set)
    else:
        v_set = 0.000000000
        l_diff = 0.00000000
        r_diff = 0.00000000
    
    
kit.motor1.throttle = 0.5
time.sleep(2)
kit.motor1.throttle = 0


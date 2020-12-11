from gpiozero import DistanceSensor, LED, Buzzer
import time

sensor = DistanceSensor(23,24,max_distance=1,threshold_distance=0.2)
led = LED(16)

def print_distance():
    print(sensor.distance) 

def is_swipe():
    return sensor.in_range

# while True:
#     print('Distance to nearest object is', sensor.distance, 'm')
#     if(sensor.in_range):
#         led.on()
#     else:
#         led.off()
#     time.sleep(0.5)
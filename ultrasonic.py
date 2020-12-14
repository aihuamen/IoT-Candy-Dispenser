from gpiozero import DistanceSensor, LED
import time

sensor = DistanceSensor(23,24,max_distance=1,threshold_distance=0.2)
led = LED(16)

def print_distance():
    print(sensor.distance) 

def is_swipe():
    return sensor.in_range

def run_distance():
    f = open('csvfile.csv','w')
    
    while True:
        try:
            f.write(str(sensor.distance)+'\n')
            print(sensor.distance)
            if(sensor.in_range):
                led.on()
                
            else:
                led.off()
                
            time.sleep(0.5)
        
        except KeyboardInterrupt:
            f.close()
            break

# run_distance()
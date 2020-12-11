import serial
import time

uart = serial.Serial("/dev/ttyACM0",115200,timeout=1)

def send_weight(weight):
    uart.close()
    uart.open()

    uart.write(weight.encode())

uart.close()
uart.open()

while True:
    try:
        uart.write("on\r\n".encode())
        time.sleep(2)
        uart.write("off\r\n".encode())
        time.sleep(2)
    
    except KeyboardInterrupt:
        # clean up on exit
        uart.close()
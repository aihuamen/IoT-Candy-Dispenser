import serial
import time

uart = serial.Serial("/dev/ttyACM0",115200,timeout=1)
print('uart connect!')

def send_weight(weight):
    uart.close()
    uart.open()

    uart.write(weight.encode())
    print(weight.encode())
    uart.close()


def test_on_off():
    uart.close()
    uart.open()

    while True:
        try:
            uart.write("on\r\n".encode())
            print('on\r\n'.encode())
            time.sleep(2)
            uart.write("off\r\n".encode())
            print('on\r\n'.encode())
            time.sleep(2)
        
        except KeyboardInterrupt:
            # clean up on exit
            uart.close()
            break

def read_weight():
    uart.close()
    uart.open()

    while True:
        weight = ''
        try:
            weight = uart.read_until('\r\n'.encode()).decode('utf-8')
            print(weight)
        
        except KeyboardInterrupt:
            # clean up on exit
            uart.close()
            break

# send_weight('50\r')
# read_weight()
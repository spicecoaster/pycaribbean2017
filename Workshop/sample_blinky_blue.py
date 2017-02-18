import machine
import time

blue_led=machine.Pin(2, machine.Pin.OUT)

for i in range(10):
    blue_led.low()
    time.sleep(0.5)
    blue_led.high()
    time.sleep(0.5)

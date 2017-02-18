import machine
import time

red_led=machine.Pin(0, machine.Pin.OUT)

for i in range(10):
    red_led.low()
    time.sleep(0.5)
    red_led.high()
    time.sleep(0.5)

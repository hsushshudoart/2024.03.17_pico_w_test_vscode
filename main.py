#machine.freq()  # get the current frequency of the CPU

import machine
import time
from machine import Pin

led25 = Pin("LED", Pin.OUT)
while True:
    print(machine.freq(),"MHz")
    led25.value(1)
    time.sleep(0.5)
    led25.value(0)
    time.sleep(1)
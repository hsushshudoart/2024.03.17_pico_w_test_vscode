#machine.freq()  # get the current frequency of the CPU

import machine
import time
from machine import Pin



led25 = Pin("LED", Pin.OUT)
counter = 0
n = 0

def blink_function(t1,t2):
    led25.value(1)
    time.sleep(t1)
    led25.value(0)
    time.sleep(t2)

    #n += 1


while True:
    print(machine.freq(),"MHz")
    
    '''
    led25.value(1)
    time.sleep(1)
    led25.value(0)
    time.sleep(1)
    '''
    if(n<=3):
        blink_function(0.5, 0.5)
        n += 1
        print(n)
    
    else:
        blink_function(3, 0.5)
        n += 1
        print(n)
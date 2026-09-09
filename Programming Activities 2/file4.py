# This program was created in Arduino Lab for MicroPython

import machine #module with microcontroller info
import time #module with time methods

led = machine.Pin(0, machine.Pin.OUT) #define everything


while True: #infinite loop to blink LED
  led.value(1) #turn led on
  time.sleep(0.25) #wait for 0.25s
  led.value(0) #turn led off
  time.sleep(0.25) #wait for 0.25s

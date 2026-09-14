# This program was created in Arduino Lab for MicroPython

import machine
import time

# define everything
light_sensor = machine.ADC(machine.Pin(1))  # A0 / GPIO1
yellow_led = machine.Pin(4, machine.Pin.OUT)  # A3 / GPIO4
green_led = machine.Pin(2, machine.Pin.OUT)  # A1 / GPIO2
button = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_UP)  # A4 / GPIO11

# light threshold
THRESHOLD = 65000

while True:
    # read the light sensor
    light_level = light_sensor.read_u16()

    # read the push button
    button_pressed = button.value() == 0

    # print the current readings
    print("Light level:", light_level, " Button:", button.value())

    # green LED turns on when light is above 65,000
    if light_level > THRESHOLD:
        green_led.value(1)
    else:
        green_led.value(0)

    # yellow LED turns on ONLY when:
    # button is pressed AND light level is above 65,000
    if button_pressed and light_level > THRESHOLD:
        yellow_led.value(1)
    else:
        yellow_led.value(0)

    time.sleep(0.1)
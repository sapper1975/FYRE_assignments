# Bryan, Kyle, and Gabby
# move servomotor 180 to 0 degrees and vice versa via button press
#9/16/26
#9/16/26
#Used to code entire project
from machine import Pin, PWM
import time

# 1. Setup Pins
button = Pin(3, Pin.IN, Pin.PULL_UP)
servo = PWM(Pin(11), freq=50)

# 2. PWM Duty Cycle Values for 0° and 180°
DUTY_0_DEG = 1638   # ~0.5ms pulse (0 degrees)
DUTY_180_DEG = 8192 # ~2.5ms pulse (180 degrees)

# 3. Initial Position State
is_at_zero = True
servo.duty_u16(DUTY_0_DEG)

print("System ready. Press button to toggle.")

# 4. Main Loop
while True:
    if button.value() == 0:
        if is_at_zero:
            print("Moving to 180°")
            servo.duty_u16(DUTY_180_DEG)
            is_at_zero = False
        else:
            print("Moving to 0°")
            servo.duty_u16(DUTY_0_DEG)
            is_at_zero = True
           
        # Debounce delay to prevent a single press from triggering multiple times
        time.sleep_ms(300)
       
    time.sleep_ms(10)
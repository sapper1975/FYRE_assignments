
#team names: Kyle, Bryan, Gabby
#Purpose of code: Test hand-fabricated moisture sensor and rain sensor.
#                 If either sensor detects significant moisture, move
#                 the servo motor to 90 degrees. When moisture is no
#                 longer detected, return the servo to 0 degrees.
#                 Pressing the button also returns the servo to 0 degrees.
#Date code was started: 9/23/26
#Last edit: 9/28/26
#Explanation of AI use: coded nearly entirely with AI, with manual
#                       adjustments and testing of the sensor circuit.


# --------------------------------------------------
# Arduino Nano ESP32 + Moisture + Rain Sensors
#
# Hand-fabricated moisture sensor:
# Analog output connected to GPIO14
#
# Rain sensor:
# Analog output connected to GPIO3
#
# Button:
# Connected to GPIO47
#
# Servo:
# Connected to GPIO12
#
# If either sensor detects significant moisture,
# the servo moves to 90 degrees.
#
# When neither sensor detects moisture, the servo
# returns to 0 degrees.
#
# If the button is pressed, the servo returns to 0 degrees.
# --------------------------------------------------


from machine import Pin, ADC, PWM
import time


# --------------------------------------------------
# 1. Setup ADC sensors
# --------------------------------------------------

# Hand-fabricated moisture sensor
# Connected to GPIO14
moisture_sensor = ADC(Pin(14))

moisture_sensor.atten(ADC.ATTN_11DB)
moisture_sensor.width(ADC.WIDTH_12BIT)


# Rain sensor
# Connected to GPIO3
rain_sensor = ADC(Pin(3))

rain_sensor.atten(ADC.ATTN_11DB)
rain_sensor.width(ADC.WIDTH_12BIT)


# --------------------------------------------------
# 2. Setup button
# --------------------------------------------------

# Button connected to GPIO47
button = Pin(47, Pin.IN, Pin.PULL_UP)


# --------------------------------------------------
# 3. Setup servo
# --------------------------------------------------

# Servo connected to GPIO12
servo = PWM(Pin(12), freq=50)


# --------------------------------------------------
# 4. Servo position functions
# --------------------------------------------------

def servo_0():
    # SG90 calibrated minimum position
    # Approximately 500 microsecond pulse

    servo.duty_ns(500000)

    print("SERVO: Moving to 0 degrees")


def servo_90():
    # SG90 maximum tested position
    # Approximately 2400 microsecond pulse
    #
    # For this project, this position represents
    # the desired 90-degree extension.

    servo.duty_ns(1750000)

    print("SERVO: Moving to 90 degrees")


# --------------------------------------------------
# 5. Sensor thresholds
# --------------------------------------------------

# Hand-fabricated moisture sensor:
# Normal = approximately 0.30 V
# Moisture = BELOW 0.10 V

MOISTURE_THRESHOLD = 0.1


# Rain sensor:
# Rain = BELOW 2.0 V

RAIN_THRESHOLD = 2.0


# --------------------------------------------------
# 6. Start sensor testing
# --------------------------------------------------

print("Moisture and rain sensor system ready.")
print("Moisture sensor: GPIO14")
print("Rain sensor: GPIO3")
print("Button: GPIO47")
print("Servo: GPIO12")
print("Moisture threshold: below {:.2f} V".format(MOISTURE_THRESHOLD))
print("Rain threshold: below {:.2f} V".format(RAIN_THRESHOLD))
print("--------------------------------")


# --------------------------------------------------
# 7. Start data collection
# --------------------------------------------------

reading_number = 1

while True:

    # ----------------------------------------------
    # Check button first
    # ----------------------------------------------

    if button.value() == 0:

        # Button is pressed
        servo_0()

        print("BUTTON PRESSED: Servo returned to 0 degrees.")

        # Wait until button is released
        while button.value() == 0:
            time.sleep(0.05)


    # ----------------------------------------------
    # Read hand-fabricated moisture sensor
    # ----------------------------------------------

    moisture_adc = moisture_sensor.read()

    moisture_voltage = (moisture_adc / 4095) * 3.3


    # ----------------------------------------------
    # Read rain sensor
    # ----------------------------------------------

    rain_adc = rain_sensor.read()

    rain_voltage = (rain_adc / 4095) * 3.3


    # ----------------------------------------------
    # Get time since program started
    # ----------------------------------------------

    time_ms = time.ticks_ms()


    # ----------------------------------------------
    # Print readings to serial console
    # ----------------------------------------------

    print(
        "Reading {}: Time: {} ms | "
        "Moisture: ADC {} | {:.3f} V | "
        "Rain: ADC {} | {:.3f} V".format(
            reading_number,
            time_ms,
            moisture_adc,
            moisture_voltage,
            rain_adc,
            rain_voltage
        )
    )


    # ----------------------------------------------
    # Check moisture sensor
    # ----------------------------------------------

    moisture_detected = moisture_voltage < MOISTURE_THRESHOLD


    # ----------------------------------------------
    # Check rain sensor
    # ----------------------------------------------

    rain_detected = rain_voltage < RAIN_THRESHOLD


    # ----------------------------------------------
    # Check whether either sensor detected moisture
    # ----------------------------------------------

    if moisture_detected or rain_detected:

        print("!!! MOISTURE DETECTED !!!")

        if moisture_detected:
            print("Hand moisture sensor triggered.")

        if rain_detected:
            print("Rain sensor triggered.")

        # Move servo to 90 degrees
        servo_90()

        print("--------------------------------")


    # ----------------------------------------------
    # If neither sensor detects moisture,
    # return servo to 0 degrees
    # ----------------------------------------------

    else:

        servo_0()

        print("No moisture detected. Servo returned to 0 degrees.")
        print("--------------------------------")


    # ----------------------------------------------
    # Increase reading number
    # ----------------------------------------------

    reading_number += 1


    # ----------------------------------------------
    # Wait before next reading
    # ----------------------------------------------

    time.sleep(0.25)

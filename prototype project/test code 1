#team names: Kyle, Bryan, Gabby
#Purpose of code: Test hand-fabricated moisture sensor by reading
#                 incoming analog voltage through GPIO14 and printing
#                 the readings to the console.
#Date code was started: 9/23/26
#Last edit: 9/23/26
#Explanation of AI use: coded nearly entirely with AI, with manual
#                       fine tuning of the servo pwm and voltage thresholds



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
# 3. Setup LED
# --------------------------------------------------

# LED connected to GPIO9
water_led = Pin(9, Pin.OUT)

# Start with LED off
water_led.value(0)


# --------------------------------------------------
# 4. Setup servo
# --------------------------------------------------

# Servo connected to GPIO12
servo = PWM(Pin(12), freq=50)


# --------------------------------------------------
# 5. Servo position functions
# --------------------------------------------------

def servo_0():
    # SG90 calibrated minimum position
    # Approximately 500 microsecond pulse

    servo.duty_ns(500000)

    print("SERVO: Moving to 0 degrees")


def servo_90():
    # For this project, 1,750,000 ns
    # represents the desired 90-degree extension.

    servo.duty_ns(1750000)

    print("SERVO: Moving to 90 degrees")


# --------------------------------------------------
# 6. Sensor thresholds
# --------------------------------------------------

# Hand-fabricated moisture sensor:
# Moisture = BELOW 0.10 V

MOISTURE_THRESHOLD = 2.5


# Rain sensor:
# Rain = BELOW 2.0 V

RAIN_THRESHOLD = 2.0


# --------------------------------------------------
# 7. Start sensor testing
# --------------------------------------------------

print("Moisture and rain sensor system ready.")
print("Moisture sensor: GPIO14 -> LED GPIO9")
print("Rain sensor: GPIO3 -> Servo GPIO12")
print("Button: GPIO47 -> Servo override")
print("Moisture threshold: below {:.2f} V".format(MOISTURE_THRESHOLD))
print("Rain threshold: below {:.2f} V".format(RAIN_THRESHOLD))
print("--------------------------------")


# --------------------------------------------------
# 8. Start data collection
# --------------------------------------------------

reading_number = 1

while True:

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
    # Check sensors
    # ----------------------------------------------

    moisture_detected = moisture_voltage < MOISTURE_THRESHOLD

    rain_detected = rain_voltage < RAIN_THRESHOLD


    # ----------------------------------------------
    # MOISTURE SENSOR -> LED ONLY
    # ----------------------------------------------

    if moisture_detected:

        water_led.value(1)

        print("MOISTURE DETECTED: LED ON")

    else:

        water_led.value(0)

        print("NO MOISTURE: LED OFF")


    # ----------------------------------------------
    # BUTTON -> SERVO OVERRIDE
    # ----------------------------------------------

    if button.value() == 0:

        # Button is pressed
        # Return servo to 0 degrees

        servo_0()

        print("BUTTON PRESSED: Servo returned to 0 degrees.")

        # Wait until button is released
        while button.value() == 0:
            time.sleep(0.05)


    # ----------------------------------------------
    # Print sensor readings
    # ----------------------------------------------

    time_ms = time.ticks_ms()

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
    # RAIN SENSOR -> SERVO ONLY
    # ----------------------------------------------

    if rain_detected:

        print("!!! RAIN DETECTED !!!")

        # Move servo to 90 degrees
        servo_90()

        print("Rain detected: Servo deployed to 90 degrees.")
        print("--------------------------------")


    else:

        # No rain detected
        # Return servo to 0 degrees

        servo_0()

        print("No rain detected. Servo returned to 0 degrees.")
        print("--------------------------------")


    # ----------------------------------------------
    # Increase reading number
    # ----------------------------------------------

    reading_number += 1


    # ----------------------------------------------
    # Wait before next reading
    # ----------------------------------------------

    time.sleep(0.25)


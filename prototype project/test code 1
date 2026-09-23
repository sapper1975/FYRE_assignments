#team names: Kyle, Bryan, Gabby
#Purpose of code: Test hand-fabricated moisture sensor by reading
#                 incoming analog voltage through GPIO14 and printing
#                 the readings to the console.
#Date code was started: 9/23/26
#Last edit: 9/23/26
#Explanation of AI use: coded nearly entirely with AI, with manual
#                       adjustments and testing of the sensor circuit.


# --------------------------------------------------
# Arduino Nano ESP32 + Hand-Fabricated Moisture Sensor
# Analog output connected to GPIO14
#
# Reads the moisture sensor continuously and prints
# the ADC reading and approximate voltage to the console.
# --------------------------------------------------


from machine import Pin, ADC
import time


# --------------------------------------------------
# 1. Setup ADC
# --------------------------------------------------

# Arduino Nano ESP32:
# Moisture sensor connected to GPIO14
moisture_sensor = ADC(Pin(14))

# Use the widest ADC input range
moisture_sensor.atten(ADC.ATTN_11DB)

# 12-bit ADC resolution
moisture_sensor.width(ADC.WIDTH_12BIT)


# --------------------------------------------------
# 2. Start sensor testing
# --------------------------------------------------

print("Moisture sensor test ready.")
print("Sensor: GPIO14")
print("ADC range: 0-4095")
print("Voltage range: approximately 0-3.3 V")
print("Taking readings every 1 second...")
print("--------------------------------")


# --------------------------------------------------
# 3. Start data collection
# --------------------------------------------------

reading_number = 1

while True:

    # Read the analog sensor
    adc_value = moisture_sensor.read()

    # Convert 12-bit ADC reading to approximate voltage
    voltage = (adc_value / 4095) * 3.3

    # Get time since program started
    time_ms = time.ticks_ms()

    # Print reading to serial console
    print(
        "Reading {}: Time: {} ms | ADC: {} | Voltage: {:.3f} V".format(
            reading_number,
            time_ms,
            adc_value,
            voltage
        )
    )

    # Increase reading number
    reading_number += 1

    # Wait 1 second before next reading
    time.sleep(0.25)

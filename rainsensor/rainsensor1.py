
# Arduino Nano ESP32 + LM393 Rain Sensor
# Analog output connected to A2 / GPIO3
#
# Takes 10 readings, saves them to rain_sensor.csv,
# then stops.
#
# Running the program again will ADD another 10 readings
# to the same CSV file.

from machine import Pin, ADC
import time

# --------------------------------------------------
# 1. Setup ADC
# --------------------------------------------------

# Arduino Nano ESP32:
# A2 = GPIO3
rain_sensor = ADC(Pin(3))

# Use the widest ADC input range
rain_sensor.atten(ADC.ATTN_11DB)

# 12-bit ADC resolution
rain_sensor.width(ADC.WIDTH_12BIT)


# --------------------------------------------------
# 2. Create / open CSV file
# --------------------------------------------------

filename = "rain_sensor4.csv"

# Check whether the file already exists
try:
    with open(filename, "r") as file:
        file_exists = True
except:
    file_exists = False


# Create the file and header if it doesn't exist
if not file_exists:
    with open(filename, "w") as file:
        file.write("reading,time_ms,adc_value,voltage_v\n")


# --------------------------------------------------
# 3. Find the next reading number
# --------------------------------------------------

# Start at reading 1
reading_number = 1

# Count existing lines in the CSV
try:
    with open(filename, "r") as file:
        lines = file.readlines()

        # Subtract 1 for the header
        reading_number = len(lines)

except:
    reading_number = 1


# --------------------------------------------------
# 4. Start data collection
# --------------------------------------------------

print("Rain sensor logger ready.")
print("Sensor: A2 / GPIO3")
print("Saving data to:", filename)
print("Taking 10 readings...")
print("--------------------------------")


for i in range(10):

    # Read the analog sensor
    adc_value = rain_sensor.read()

    # Convert 12-bit ADC reading to approximate voltage
    voltage = (adc_value / 4095) * 3.3

    # Get time since program started
    time_ms = time.ticks_ms()

    # Current overall reading number
    current_reading = reading_number + i

    # Print to serial console
    print(
        "Reading {}: Time: {} ms | ADC: {} | Voltage: {:.3f} V".format(
            current_reading,
            time_ms,
            adc_value,
            voltage
        )
    )

    # Append reading to CSV
    with open(filename, "a") as file:
        file.write(
            "{},{},{},{:.3f}\n".format(
                current_reading,
                time_ms,
                adc_value,
                voltage
            )
        )

    # Wait 1 second before next reading
    time.sleep(1)


# --------------------------------------------------
# 5. Finished
# --------------------------------------------------

print("--------------------------------")
print("10 readings complete.")
print("Data saved to:", filename)
print("Program stopped.")

#Python Degree Converter Made By t1mmylee on GitHub

import time

print("Enter your temperature")

time.sleep(1.1)
temperature = int(input("Temperature: "))
time.sleep(0.5)
unit = input("(C)elsius or (F)ahrenheit: ")

if unit.upper() == "C" or "c":
    converter = temperature * 9/5 + 32
    print("Temperature in F: " + str(converter))
if unit.upper() == "F" or "f":
    converter = temperature - 32 * 5/9
    print("Temperature in C: " + str(converter))
else:
    print("An error occurred, retry the code")


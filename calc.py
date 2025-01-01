#Python Degree Converter Made By t1mmylee on GitHub

import time
from colorama import Fore, Back, Style

print(Fore.CYAN + "Enter your temperature")

time.sleep(1.1)
temperature = int(input("Temperature: "))
time.sleep(0.5)
unit = input(Fore.CYAN + "(C)elsius or (F)ahrenheit: ")

if unit.upper() == "C" or "c":
    converter = temperature * 9/5 + 32
    print(Fore.YELLOW + "Temperature in F: " + str(converter))
elif unit.upper() == "F" or "f":
    converter = temperature - 32 * 5/9
    print(Fore.YELLOW + "Temperature in C: " + str(converter))
else:
    print(Fore.RED + "An error occurred, retry the code")

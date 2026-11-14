
import math
import random
import platform

number = random.randint(1, 100)

print("Random Number:", number)
print("Square Root (floored):", math.floor(math.sqrt(number)))
print("Operating System:", platform.system())
print("Python Version:", platform.python_version())

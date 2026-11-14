# Requires colorama; install with: pip install colorama

from colorama import Fore, Style, init

init()

print(Fore.GREEN + "Hello from Colorama!")
print(Fore.BLUE + "Python modules are fun!")
print(Style.RESET_ALL + "Back to normal text.")

# Requires colorama; install with: pip install colorama

from colorama import Fore, init

init()
grade = int(input("Enter your grade: "))

if grade >= 70:
    print(Fore.GREEN + "You passed!")
else:
    print(Fore.RED + "You failed. Keep trying!")

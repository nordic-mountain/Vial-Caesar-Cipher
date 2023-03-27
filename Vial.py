# Vial.py
import colorama
import os

colorama.init()
version = "1.0.3"

# ANSI escape codes for text colors
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
PURPLE = "\033[1;35m"
CYAN = "\033[1;36m"
RESET = "\033[0m"

startUpScreen = f"""
Welcome to
__     ___       _
\\ \\   / (_) __ _| |
 \\ \\ / /| |/ _\`| |
  \\ V / | | (_| | |
   \\_/  |_|\\__,_|_|
   
   A {RED+"brute force"+RESET} program for Caesar Ciphers.
   Made by {BLUE+"TheTechyKid"+RESET}. Version {GREEN+version+RESET}.
   All lights reserved."""

def Break(msg):
    output = ''

    for xy1 in range(0, 26):
        for letter in msg:
            x = ord(letter) + xy1
            y = chr(x)
                
            output += y
        print(f"#{xy1} "+output.upper()+"\n")
        output = ""

    for xy in range(0, 26):
        for letter in msg:
            x = ord(letter) - xy
            y = chr(x)
                
            output += y
        print(f"#{xy} "+output.upper()+"\n")
        output = ""

def Vial():
    num = 1
    
    while num>0:
        print(startUpScreen+"\n")
        msg = input(f"Your message \033[1;32m>\033[0m  ")

        Break(msg=msg)
    
        contin = input("Continue [\033[1;32mY\033[0m/\033[1;31mN\033[0m] \033[1;32m>\033[0m ").lower()
        if contin == "n":
            num = -1
        else:
            os.system("cls")
            continue

if __name__ == "__main__":
    Vial()
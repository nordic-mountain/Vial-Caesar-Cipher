# Vial.py
import platform
import colorama
import os

# Main varibles
colorama.init()
version = "1.0.4"

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

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def Break(msg):
    """The encoder"""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    msg = msg.lower()

    for key in range(len(alphabet)):
        output = ''
        
        for letter in msg:
            if letter in alphabet:
                index = alphabet.find(letter)
                index = (index + key)%(len(alphabet))

                if index < 0:
                    index = index + len(alphabet)
                    
                output = output + alphabet[index]
                
            else:
                output = output + letter
                    
        print(f"#{key} "+output)

def VialMain():
    num = 1
    
    while num>0:
        print(startUpScreen+"\n")
        msg = input(f"Your message \033[1;32m>\033[0m  ")

        Break(msg=msg)
    
        contin = input("Continue [\033[1;32mY\033[0m/\033[1;31mN\033[0m] \033[1;32m>\033[0m ").lower()
        if contin == "n":
            num = -1
        else:
            clear_screen()
            continue

if __name__ == "__main__":
    VialMain()
  

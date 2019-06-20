# A library of utilities for text games

import platform
import os

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')